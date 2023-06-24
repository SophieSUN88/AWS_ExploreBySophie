# AWS GLUE Turotial
**Explore with Sophie**

## Preparation
1. IAM Role
- AmazonRDSFullAccess
- AmazonS3FullAccess
- AWSGlueServiceRole

2. LakeFormation
- Grant the permission to the database/all_tables in Catagory
- Register the s3 path

3. Data in S3
- use Faker library to generate data
- save data in json file
- check the IAM user to connect S3 programmly
- upload the file from local to s3 bucket

## Catalog and Crawler
1. create the table manually
2. create the table with cralwer
3. create the table with schema in registry


## ETL Job
### 1. Create a simple virtual ETL Job
- Resource: S3 bucket
- Transfor: rename, drop columns
- Target: S3 bucket

### 2. Create a ETL Job from S3 to RDS
1. Instance and RDS
- create an EC2
- create RDS Postgres
- create a table

2. Crawler the table in RDS Postgres
- create the connection to RDS
- create a crawler to generate the table from RDS to Catalog

3. create the ETL Job
- Resource: S3 bucket
- Transfor: rename, drop columns
- Target: RDS Postgres database

### 3. Other features
- [Bookmark](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html)
- [Schedules](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)


