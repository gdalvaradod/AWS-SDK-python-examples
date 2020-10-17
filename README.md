# Python Boto3 examples

## 1. List executions

File: ListExecutions.py

This example was taken from [AWS SDK Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_executions). But, if you run that code using AWS Lambda console, it won't work. The problem is the response. It returns incomplete and if you try to convert to json format, this throw an ident error because of datetime.

You have to add the next line:

**json.dumps(MyResponse, indent=4, sort_keys=True, default=str)**

This line prepare the response for Json format.
