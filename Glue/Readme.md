% AWS GLUE Turotial
**Explore with Sophie**

**Contents:**

[[_TOC_]]

# Preparation
## 1. IAM Role

## 2. LakeFormation

## 3. Instance and RDS
- create an EC2
- create RDS Postgres
- create a table

## 4. Data in S3
- upload

# Catalog and Crawler
1. create the table manually
2. create the table with cralwer
3. create the table with schema in registry
4. create the connection to RDS, and get the table from RDS with crawler

# ETL Job
## 1. Create a simple virtual ETL Job
- Resource: S3 bucket
- Transfor: rename, drop columns
- Target: S3 bucket
## 2. Create a ETL Job from S3 to RDS
- Resource: S3 bucket
- Transfor: rename, drop columns
- Target: RDS
## 3. Other features
- [Bookmark](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html)
- [Schedules](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)


