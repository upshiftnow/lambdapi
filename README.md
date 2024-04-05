# Deploying Lambda Function to AWS with CodePipeline

## Objective

The problem at hand involves deploying a Lambda function to AWS using CodePipeline, with specific dependencies. The objective is to create a streamlined process for deploying a Lambda function that retrieves the current temperature in New York City using an external API.

## Tools Required

To achieve the objective, the following tools and services are required:

- AWS Account: Provides access to AWS services.
- AWS Lambda: Used to run serverless functions.
- Amazon S3: Used for storage and deployment artifacts.
- Python: Programming language used to write the Lambda function.
- Amazon CodeCommit: Version control service for storing and managing code.
- AWS Cloud9: Cloud-based integrated development environment (IDE) for code editing and debugging.
- AWS CodeBuild: Fully managed build service for compiling, testing, and packaging code.
- AWS CodePipeline: Fully managed continuous integration and continuous delivery (CI/CD) service for automating the deployment pipeline.

## Lambda Function

The provided Lambda function retrieves the current temperature in New York City using an external API. Here's a brief overview of the function:

- **Function**: lambda_handler
- **Description**: Retrieves current temperature in NYC from an external API.
- **Dependencies**: Uses the `requests` library to make HTTP requests.
- **Runtime**: Python 3.10

## Deployment Setup

The deployment setup includes the following components:

### `requirements.txt`

Contains the list of Python dependencies required by the Lambda function.

### Deployment Process
Push the Lambda function code to Amazon CodeCommit.
Configure AWS CodePipeline to monitor the CodeCommit repository.
Configure AWS CodeBuild to build the Lambda function code and package it.
Configure AWS CodePipeline to deploy the packaged Lambda function to AWS Lambda.
Access the deployed Lambda function endpoint to retrieve the current temperature in New York City.
