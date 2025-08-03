from flask import Flask, render_template, request
import json
import os
from datetime import datetime
import boto3

app = Flask(__name__)

# Local folder for temporary data storage
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# AWS Config
S3_BUCKET = "nikhil-birthday-reminder-bucket-09092001"  # Replace with your S3 bucket
AWS_REGION = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:764273270390:birthday-reminder-topic"  # Replace with your SNS Topic ARN

# AWS Clients
s3_client = boto3.client("s3", region_name=AWS_REGION)
sns_client = boto3.client("sns", region_name=AWS_REGION)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    birthday = request.form['birthday']

    data = {
        "name": name,
        "email": email,
        "birthday": birthday
    }

    filename = f"{name.lower().replace(' ', '_')}_{datetime.now().timestamp()}.json"
    local_path = os.path.join(DATA_FOLDER, filename)

    # Save locally
    with open(local_path, 'w') as f:
        json.dump(data, f)

    # Upload to S3
    try:
        s3_client.upload_file(local_path, S3_BUCKET, f"birthdays/{filename}")
    except Exception as e:
        return f"❌ Upload to S3 failed: {str(e)}"

    # Subscribe user to SNS topic
    try:
        sns_client.subscribe(
            TopicArn=SNS_TOPIC_ARN,
            Protocol='email',
            Endpoint=email
        )
    except Exception as e:
        return f"❌ SNS subscription failed: {str(e)}"

    return f"✅ {name}, your birthday has been saved! Please confirm the SNS email to get reminders."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
