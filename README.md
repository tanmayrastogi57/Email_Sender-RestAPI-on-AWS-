# AWS Lambda Email Sender

This project provides an AWS Lambda function designed to send emails using Gmail's SMTP server. The Lambda function is triggered via a REST API, allowing users to send emails through HTTP POST requests.

## Overview

The AWS Lambda function processes incoming HTTP POST requests containing email details and utilizes Gmail's SMTP server to send the email. The API Gateway integrates with this Lambda function to handle the REST API interactions.

## Features

- **Email Sending**: Sends emails via Gmail's SMTP server.
- **Error Handling**: Provides informative error messages for missing or incorrect input.
- **Logging**: Logs execution results and errors to facilitate debugging.

## Configuration

### Prerequisites

- **AWS Lambda**: Create and configure a Lambda function in the AWS Management Console.
- **Gmail Account**: Required for SMTP credentials.
- **API Gateway**: Configured to route HTTP POST requests to the Lambda function.

### Setup

1. **Update Email Credentials**:
   - Configure the SMTP credentials in the Lambda function code. Ensure to use secure methods for handling sensitive information, such as environment variables or AWS Secrets Manager.

2. **Deploy Lambda Function**:
   - Upload the Lambda function code to AWS Lambda.
   - Assign the necessary execution role and permissions.

3. **Configure API Gateway**:
   - Set up an API Gateway endpoint.
   - Route POST requests to the Lambda function.

## Usage

### Testing via AWS Lambda Console

1. **Create a Test Event**:
   - Navigate to the AWS Lambda Management Console.
   - Configure a test event with a JSON body that includes `receiver_email`, `subject`, and `body`.

2. **Run the Test**:
   - Execute the test to verify that the function performs as expected.

### Sending Requests via REST API

1. **Send HTTP POST Requests**:
   - Use tools like `curl`, Postman, or any HTTP client to send POST requests to the API Gateway endpoint.
   - Include a JSON payload with the email details.

## REST API Integration

The Lambda function is exposed through a REST API via API Gateway. This setup allows for external systems and users to interact with the Lambda function over HTTP. The API Gateway handles the routing of POST requests to the Lambda function and processes the responses.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes.


## Contact

For questions or feedback, please reach out to [tanmayrastogi57@gmail.com](mailto:tanmayrastogi57@gmail.com).
