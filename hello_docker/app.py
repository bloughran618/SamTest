import json

# import requests
import logging

logging.getLogger().setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info(f"This is the event: {event}")

    if event.get("hello"):

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"sup {event.get('hello')}",
            }),
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "sup dawg",
            }),
        }
