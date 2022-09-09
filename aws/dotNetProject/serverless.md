# Serverless

## Intro to Lambda function

Lambda runs the codes only we needed. It's also highly scalable.

There are some concepts:

- Function: packing of codes that process events
- Event: JSON-formatted docment containing data
- Concurrency: number of requests a function is serving at any given time
- Trigger: resource or configuration that invokes a function

### Execution Environment

When you create a Lambda function, you specify configuration information, such as **the amount of memory** and **maximum execution time** that you want to allow for your Lambda function.

It takes time to set up an execution context and do the necessary "bootstrapping", which adds **some latency each time the Lambda function is invoked**. You typically see this latency when a Lambda function **is invoked for the first time or after it has been updated**.

If AWS Lambda chooses to reuse the context when the Lambda function is invoked again. This execution context reuse approach has the following implications: **Objects declared outside of the function's handler method remain initialized, providing additional optimization when the function is invoked again**.

### Lambda Permissions

- Execution Permissions

  A lambda function’s execution permissions are controlled by an IAM Role. This Role will contain policies that either allow or deny specific API calls to be made.

- Resource-based Policies

  They control access to invoking and managing a lambda function. You can use it to grant use permissions to **other accounts** or **other AWS services**.

### Lambda Execution

When your code executes in Lambda, the service will spin up a **micro-virtual machine** that will download your code and all the dependencies required and then execute it. The technology used for those micro-VMs is called **Firecracker** which is an open source virtualization technology.

AWS created this technology with Lambda in mind as well as for multi-tenant container which is being used in the AWS Fargate service.

Each execution context provides **512 MB of additional disk space in the /tmp directory**. The directory content remains when the execution context is frozen, providing transient cache that can be used for multiple invocations. AWS keeps it warm for 15 min. Provisioned concurrency will keep the execution context warm, but user will be billed for it.

### Lambda Push/Pull Model

- Push Model: It is where **a trigger sends an event to lambda**, which then invokes your lambda function. When the push model is used, the resource-based policy must allow the trigger to invoke the lambda function.

- Pull Model: AWS Lambda **pulls the event from the event source**, and then invokes the lambda function.

  e.g. Instead of having SQS invoke the lambda every time it gets a message, the messages build up in the queue and you define an Event Source Mapping as the trigger for the lambda function.

### Asynchronous vs Synchronous Lambda Functions

For most REST API operations, the client will want a response from the Lambda function so it makes sense to have Lambda executed synchronously during those times.

In the case of a long-latency operation, it would make sense to invoke it asynchronously and use another mechanism to let the client know that the operation is completed. For example, S3 invokes Lambda asynchronously.

### Versioning and Aliases

You can publish a new version of your AWS Lambda function when you create new or update existing functions. **Each version of a lambda function gets it’s own unique Amazon Resource Name (ARN).** You can then use these ARNs to use different versions of the Lambda function for different purposes.

You also have the ability to create aliases for AWS Lambda functions. Aliases are essentially pointers to one specific Lambda version.
