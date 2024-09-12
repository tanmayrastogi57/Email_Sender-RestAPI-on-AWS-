# main2.py

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration for Gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your email'
SENDER_PASSWORD = 'your gmail app key'

# Function to send email
def send_email(receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise e

# AWS Lambda handler

def lambda_handler(event, context):
    try:
        # Check if 'body' is present in the event
        if 'body' not in event or not event['body']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No body in request'})
            }

        # Parse the body (assuming it's JSON)
        data = json.loads(event['body'])
        receiver_email = data.get('receiver_email')
        subject = data.get('subject')
        body = data.get('body')

        if not receiver_email or not subject or not body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        send_email(receiver_email, subject, body)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully!'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
