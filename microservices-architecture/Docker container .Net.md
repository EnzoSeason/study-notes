Use .NET 7, with Linux or Windows Containers, for your containerized Docker server application when:

-   You have cross-platform needs. For example, you want to use both Linux and Windows Containers.
-   Your application architecture is based on microservices.
-   You need to start containers fast and want a small footprint per container to achieve better density or more containers per hardware unit in order to lower your costs.

The available images are: 

| Image | Comments |
| ------ | ------- |
| mcr.microsoft.com/dotnet/runtime:7.0 | .NET 7 multi-architecture |
| mcr.microsoft.com/dotnet/aspnet:7.0 |   ASP.NET Core 6.0 multi-architecture |
| mcr.microsoft.com/dotnet/sdk:7.0 | Dev image|

You can find all the available docker images in [dotnet-docker](https://github.com/dotnet/dotnet-docker)


