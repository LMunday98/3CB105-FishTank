from pprint import pprint
import boto3


def put_movie(log_number, water_level_max, water_temp, date, time, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('3CB105-FishTank')
    response = table.put_item(
       Item={
            'log_number': log_number,
            'water_level_max': water_level_max,
            'water_temp': water_temp,
            'date': date,
            'time': time
        }
    )
    return response


if __name__ == '__main__':
    log = put_movie(2, False, 20, "07/12/1998", "12:30", 0)
    print("Put log succeeded:")
    pprint(log, sort_dicts=False)
