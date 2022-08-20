# Monitoring

The act of **collecting, analyzing, and using data to make decisions or answer questions about your IT resources and systems** is called monitoring.

## Metrics

Each **individual data point** that is created by a **resource** is a **metric**. Metrics that are collected and analyzed over **time** become **statistics**.

The metrics can be:

- CPU utilization
- network utilization
- disk performance
- memory utilization
- logs created by the applications running on top of EC2

## Alarm

To set up an alarm you need to choose:

- the metric
- the threshold
- the time period

For example, if you wanted to set up an alarm for an EC2 instance to trigger when the **CPU utilization goes over a threshold of 80%**, you also need to specify the time period the CPU utilization is over the threshold. For example if it is **over 80% for 5 minutes or longer**, when there is a potential resource issue.