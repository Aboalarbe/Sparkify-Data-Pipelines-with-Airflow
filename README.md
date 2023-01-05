# Sparkify Data Pipelines with Airflow on AWS

## Introduction

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.


## Author

- [@Mohamed S. Elaraby](https://github.com/Aboalarbe)


## Role Description

we will create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. and we also added data quality checks to run tests against the datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

## Data Description
The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

## Custom Operators Description

### Stage Operator
The stage operator is expected to be able to load any JSON formatted files from S3 to Amazon Redshift. The operator creates and runs a SQL COPY statement based on the parameters provided. The operator's parameters should specify where in S3 the file is loaded and what is the target table. The parameters should be used to distinguish between JSON file. Another important requirement of the stage operator is containing a templated field that allows it to load timestamped files from S3 based on the execution time and run backfills.

### Fact and Dimension Operators
With dimension and fact operators, you can utilize the provided SQL helper class to run data transformations. Most of the logic is within the SQL transformations and the operator is expected to take as input a SQL statement and target database on which to run the query against. You can also define a target table that will contain the results of the transformation. Dimension loads are often done with the truncate-insert pattern where the target table is emptied before the load. Thus, you could also have a parameter that allows switching between insert modes when loading dimensions. Fact tables are usually so massive that they should only allow append type functionality.

### Data Quality Operator
The final operator to create is the data quality operator, which is used to run checks on the data itself. The operator's main functionality is to receive one or more SQL based test cases along with the expected results and execute the tests. For each the test, the test result and expected result needs to be checked and if there is no match, the operator should raise an exception and the task should retry and fail eventually.

## Prequesite for this project

you should create Redshift Cluster on AWS and connect it with Airflow.
    
## DAG Description
In the DAG, add default parameters according to these guidelines

- The DAG does not have dependencies on past runs
- On failure, the task are retried 3 times
- Retries happen every 5 minutes
- Catchup is turned off
- Do not email on retry
![Main Dag](https://firebasestorage.googleapis.com/v0/b/plantsexpertsystem-f6812.appspot.com/o/example-dag.png?alt=media&token=56a2919b-e126-4b65-aced-87b442d0dea9)

## Data Model with Satr Schema

![Schema](https://firebasestorage.googleapis.com/v0/b/plantsexpertsystem-f6812.appspot.com/o/Untitled%20Workspace.png?alt=media&token=52f7a554-c5db-4f01-94d7-a46e38645fde)
this schema created using "creatly.com"


## Feedback

If you have any feedback, please reach out to us at mhuss073@uottawa.ca


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.credential.net/profile/mohamedaboalarbe/wallet)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammed-elaraby/)
