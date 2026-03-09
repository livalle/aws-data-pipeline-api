import requests
import boto3
import json
from datetime import datetime

API_URL = "https://jsonplaceholder.typicode.com/posts"
BUCKET = "aws-data-lake-li"

def ingest():

    response = requests.get(API_URL)
    data = response.json()

    s3 = boto3.client("s3")

    file_name = f"raw/posts_{datetime.now().strftime('%Y%m%d')}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=file_name,
        Body=json.dumps(data)
    )

    print("Upload successful")

if __name__ == "__main__":
    ingest()
