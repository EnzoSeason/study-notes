# Optimization

## Edge-optimized endpoints

### AWS Global Infrastructure: Edge Locations

AWS Edge Locations are sites that **Amazon CloudFront** uses to cache copies of your content for faster delivery to users around the world.

Amazon CloudFront is put before the API Gateway.

### Amazon API Gateway Response Caching

Amazon API Gateway can cache your endpoint's responses.

When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time-to-live (TTL) period, in seconds. The default TTL value for API caching is 300 seconds. The maximum TTL value is 3600 seconds. TTL=0 means caching is disabled.

### AWS Lambda @ Edge

It is a feature of Amazon CloudFront that **lets you run code closer to users of your application**, which improves performance and reduces latency.

## Lambda function

### AWS Lambda Layers

You can configure your Lambda function to **pull in additional code and content** in the form of layers.

A layer is a ZIP archive that contains **libraries, a custom runtime, or other dependencies**.

With layers, you can use libraries in your function without needing to include them in your deployment package.

### AWS Lambda Performance and Pricing

Find the pricing calculator here: https://s3.amazonaws.com/lambda-tools/pricing-calculator.html

### AWS Lambda Power Tuning

AWS Lambda Power Tuning is an **AWS Step Functions state machine** that helps you optimize your Lambda functions in a data-driven way.

You can **provide any Lambda function as input** and the state machine will run it with multiple power configurations (from 128MB to 3GB), analyze execution logs and suggest you the best configuration to minimize cost or maximize performance.

Find the AWS Lambda Power Tuning project here: https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:451282441545:applications~aws-lambda-power-tuning

### AWS Lambda Best Practices

- Minimize **package size**

  Include the SDK that is used, Minimize storage/memory, etc.

- Minimize the **complexity of dependencies**

- Avoid using recursive code

  If we write the inifinit loop by accident, we can **set the concurrent execution limit to 0** and update the codes.

- Reuse **execution context**

  For example, we can handle the db connection outside the function handler.

  Don't save sensitive data in **execution context**.

- **Load test** the lamdba function to find out **optimal timeout value**.

To read a list of AWS Lambda Best Practices in detail click here: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
