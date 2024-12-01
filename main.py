import urllib.parse
import json

def lambda_handler(event, context):
    """
    AWS Lambda handler to process x-www-form-urlencoded input.
    """
    try:
        # Log the event for debugging
        print("Received event:", json.dumps(event))

        # Ensure the content type is x-www-form-urlencoded
        content_type = event.get("headers", {}).get("Content-Type", "")
        if content_type != "application/x-www-form-urlencoded":
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Unsupported Content-Type"})
            }

        # Parse the body
        body = event.get("body", "")
        if not body:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Empty body"})
            }

        # Decode x-www-form-urlencoded data
        parsed_data = urllib.parse.parse_qs(body)

        # Log the parsed data
        print("Parsed data:", parsed_data)

        # Process the data (example)
        response_data = {"message": "Data received successfully", "data": parsed_data}

        return {
            "statusCode": 200,
            "body": json.dumps(response_data)
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }


if __name__ == "__main__":
    # Example test case
    test_event = {
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "body": "key1=value1&key2=value2"
    }
    print(lambda_handler(test_event, None))
