import json
import logging
import requests
import boto3
from datetime import date, datetime


def lambda_handler(event, context):
    
    sFilter = str(event["params"]["path"]["status"])
    STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:549193514663:stateMachine:OrderSystemStateMachine'
    sfn = boto3.client('stepfunctions')
    
    try:
        response = sfn.list_executions(
            stateMachineArn = STATE_MACHINE_ARN,
            statusFilter=sFilter,
            maxResults=100
        )
        obj_dump = json.dumps(response.get("executions"), indent=4, sort_keys=True, default=str) //Prepare format to json
        obj_final = json.loads(obj_dump)
    except:
        msj = '{"message": "Error", "Detail": "El estatus ingresado no existe"}'
        msj = json.loads(msj)
        return msj
    
    return obj_final
