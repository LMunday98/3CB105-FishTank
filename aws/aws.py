import boto3


def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='3CB105-FishTank',
        KeySchema=[
            {
                'AttributeName': 'log_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'water_temp',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'log_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'water_temp',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


if __name__ == '__main__':

    session = boto3.session(
      region_name = 'eu-west-2',
      aws_access_key_id=AKIA3SOP7ROQ3BZJJ6UI,
      aws_secret_access_key=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)

    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)
