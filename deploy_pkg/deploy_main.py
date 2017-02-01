import click
import boto3
from build_pkg import build_single
from upload_pkg import upload_single_to_s3
import json


@click.command()
@click.argument('target', default='', required=False)
@click.option('--publish', '-p', is_flag=True,
              help="specify if updated function should be published (versioned) by lambda")
@click.option('--raw', '-r', is_flag=True,
              help="specify if updated function should be published (versioned) by lambda")
def deploy(target, publish, raw):
    client = boto3.client('lambda')
    if target == "":
        print("endpoint not specified")
    else:
        if raw:
            build_single(target)
            upload_single_to_s3(target)
            res = update_lambda_endpoint(client, target, publish)
            print("Version: " + res['Version'])
        else:
            res = update_lambda_endpoint(client, target, publish)
            print("Version: " + res['Version'])

def update_lambda_endpoint(client, function_name, publish_flag):
    feedback = "publising new version" if publish_flag else "deploying to $LATEST"
    print(feedback)
    with open('ether-options.json') as data_file:
        settings = json.load(data_file)
    response = client.update_function_code(
        FunctionName=function_name,
        S3Bucket=settings["bucket"],
        S3Key=function_name,
        Publish=publish_flag
    )
    return response
