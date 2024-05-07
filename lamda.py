def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    data = json.dumps(event)
    payload = data
    print(payload)
    
    # Set the content type of the input data
    content_type = 'application/json'

    # Extract the input data from the incoming API Gateway event
    '''try:
        input_data = json.loads(event['body'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing input data'})
        }'''

    # Convert the input data to JSON format
    #payload = json.dumps(input_data)

    # Invoke the SageMaker endpoint
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType=content_type,
        Body=bytes(payload,'utf-8'))
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)
    
    return result
