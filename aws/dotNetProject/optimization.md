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