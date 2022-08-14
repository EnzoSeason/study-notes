# Compute

There are three types of compute options:

- virtual machines
- container services
- serverless

## Virtual machines

Amazon Elastic Compute Cloud (EC2) is a web service that provides **secure, resizable compute capacity** in the cloud. It allows you to provision **virtual servers called EC2 instances**.

### Amazon Machine Image (AMI)

When launching an EC2 instance, the first setting you configure is which operating system you want by selecting an **Amazon Machine Image (AMI)**.

The AMI is how you model and define your instance, while the EC2 instance is the entity you interact with, where you can install your web server, and serve your content to users.

One advantage of using AMIs is that they are reusable. An image creates an instance. And we can create an image from an instance, too.

### Amazon Virtual Private Cloud (VPC)

By default, your EC2 instances are placed in a network called the default Amazon Virtual Private Cloud (VPC).

Any resource you put inside the default VPC will be public and accessible by the internet.

### EC2 Instance Lifecycle

![ec2-lifecycle](./images/ec2-lifecycle.png)

- **stop** will lose all your data in the memory (RAM), while **stop-hibernate** won't. It will save them.

## Container services

A container is a standardized unit that **packages up your code and all of its dependencies**. This package is designed to **run reliably on any platform**, because the container creates its own independent environment.

### Container vs VM

![container-vs-vm](./images/container-vs-vm.png)

Containers share the same operating system and kernel as the host they exist on, whereas virtual machines contain their operating system. Therefore, containers are more lightweight.

While containers can provide speed, virtual machines offer you the full strength of an operating system and offer more resources, like package installation, a dedicated kernel, and more.

### Orchestrate Containers

In AWS, **containers run on EC2 instances**. Most companies and organizations run many containers on many EC2 instances across several Availability Zones.

AWS offers two container orchestration services:

- Amazon Elastic Container Service (ECS)
- Amazon Elastic Kubernetes Service (EKS).

| Term                                                        | ECS                   | EKS         |
| ----------------------------------------------------------- | --------------------- | ----------- |
| An EC2 instance with the ECS Agent installed and configured | container instance    | worker node |
| ECS Container                                               | task                  | pod         |
| technology                                                  | AWS native technology | Kubernetes  |
