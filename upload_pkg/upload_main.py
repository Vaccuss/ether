import json
import boto3
import os
import click
from build_pkg import build_all
from build_pkg import build_single


@click.command()
@click.argument('target', default='', required=False)
@click.option('--all', '-a', is_flag=True, help="flag to specify uploading all the endpoints")
@click.option('--build', '-b', is_flag=True, help="flag to build_pkg all endpoints before upload_pkg commences")
def upload(target, all, build):
    if target == '':
        if build and not all:
            build_all()
        elif build and all:
            build_all()
            upload_all_to_s3()
        elif all and not build:
            upload_all_to_s3()
        elif not build and not all:
            print("please specify target or use -all(-a) \nsyntax: build <target> or (-all -a) optional (--build -b)")
    else:
        if build:
            build_single(target)
            upload_single_to_s3(target)
        elif all and not build:
            print("-all ignored uploading specific only")
            upload_single_to_s3(target)
        elif not build:
            upload_single_to_s3(target)


def upload_all_to_s3():
    print("Uploading...")
    with open('ether-options.json') as data_file:
        settings = json.load(data_file)
    resource = boto3.resource("s3")
    bucket = resource.Bucket(settings["bucket"])
    all_endpoints = get_built_code()
    for endpoint in all_endpoints:
        dr = os.path.join(os.getcwd(), ".build")
        bucket.put_object(Key=endpoint[:len(endpoint) - 4], Body=open(os.path.join(dr, endpoint), 'rb'))
    print("Uploading done")


def upload_single_to_s3(target):
    print("Uploading...")
    with open('ether-options.json') as data_file:
        settings = json.load(data_file)
    resource = boto3.resource("s3")
    bucket = resource.Bucket(settings["bucket"])

    if ".zip" not in target:
        target += ".zip"
    dr = os.path.join(os.getcwd(), ".build")
    bucket.put_object(Key=target[:len(target) - 4], Body=open(os.path.join(dr, target), 'rb'))

    print("Upload done")


def get_built_code():
    dr = os.path.join(os.getcwd(), ".build")
    items = os.listdir(dr)
    return items
