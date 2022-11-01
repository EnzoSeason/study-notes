# Hadoop Big Data principles

## Moving programs to data

Since it's expensive to move big data to a centralized machine, we move the programs to the machine where data lives. The process is as followed:

1. We put data on the **clusters** of servers

  Data is saved in HDFS files in **blocks**.

2. Big data engine **allocates the processes to the servers** based on their performance.

3. We program in Hadoop or Spark, and package the codes in JAR file (since Hadoop or Spark runs in JVM). 

4. Engine finds the paths to the data, **split them in pieces**, and sends the pieces to processes.

5. Once the process receives the task, it will check if it has the corresponded program. If not, it will download it. Then, it executes the task.