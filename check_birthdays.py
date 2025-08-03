import boto3
import json
from datetime import datetime

AWS_REGION = "us-east-1"
S3_BUCKET = "nikhil-birthday-reminder-bucket-09092001"  # Replace with your bucket name
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:764273270390:birthday-reminder-topic"  # Replace with your topic ARN

s3_client = boto3.client("s3", region_name=AWS_REGION)
sns_client = boto3.client("sns", region_name=AWS_REGION)

def check_birthdays(force_send=False):
    today = datetime.now().strftime("%m-%d")

    # List all objects in S3 under 'birthdays/'
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix="birthdays/")
    if 'Contents' not in response:
        print("No birthday data found.")
        return

    for obj in response['Contents']:
        file_obj = s3_client.get_object(Bucket=S3_BUCKET, Key=obj['Key'])
        data = json.loads(file_obj['Body'].read().decode('utf-8'))

        # Match month-day or force send for testing
        bday_md = datetime.strptime(data['birthday'], "%Y-%m-%d").strftime("%m-%d")
        if bday_md == today or force_send:
            message = f"🎉 Happy Birthday, {data['name']}!"
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="Birthday Reminder",
                Message=message
            )
            print(f"Sent birthday wish to {data['email']}")

if __name__ == "__main__":
    # Change force_send to True to test instantly
    check_birthdays(force_send=True)
