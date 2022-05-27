from asyncio import as_completed
import json
import boto3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = 'https://api.getemail.io/ge-tools/test-process-csv-records'
WORKERS = 10

def process_csv(url, req_body):
    try:
        response = requests.post(url, req_body)
        return response
    except requests.exceptions.RequestException as e:
       err_message = str(e)
       print(err_message)
       raise Exception(err_message)

def runner(datas):
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        result = []
        futures = []
        for data in datas:
            req_body = json.dumps(data)
            futures.append(executor.submit(process_csv, url, req_body))

        for task in as_completed(futures):
            try:
                res = task.result()
                result.append({"status_code": res.status_code, "res": res.text})
            except Exception as exc:
                raise exc
        return result
def lambda_handler(event, context):
    datas = event['result']['datas']
    response = runner(datas)
    return response
