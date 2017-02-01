# ether

Ether is a opinionated AWS cli to help organise a aws lambda project. 
The focuses of this cli are 
     
 1. automatically packaging of functions so that file structure is maintained for import validation locally 
    and in lambda
 2. automated tooling for uploading to S3 to support other continues integration systems
 3. uploading, versioning, and releasing code in lambda. 
 4. updating and manipulating alias creation, and editing.
 
 

# Installation

Simply run:

    $ pip install ether.
    
Set up aws credentials using aws cli

    aws configure 


# Usage

## Build
The build command allows you to package a single or all endpoints into a zip file ready to be uploaded to lambda, s3
or intergrated into your own automated code management system.

 __Build a single target__

    $ ether build <target> 

 __options__
    
    Build all the endpoints
    
         $ ether build -all [other syntax  -a]
     

## Upload
 The upload command uploads to the s3 bucket specified in the ether-options.json
 This command uses the credentials that you have set up using aws-cli if you have not done this it will not work. 

__Single target__

    $ ether upload <target>
    
**Single target options**

upload does not build on call as ether does not assume what order you process your endpoints.

To build ***before*** uploading
    
    $ ether upload <target> --build [other syntax  -b]
 
 __All functions__

    $ ether upload --all [other syntax -a]
    
**All function options**

upload does not build on call as ether does not assume what order you process your endpoints.

   To build ***before*** uploading
    
    $ ether upload --all --build [other syntax  -b]

## Help commands
Currently not useful. But.

    $ ether --help

I did warn you

# Further information

I use and rely on the AWS Boto3 and the aws cli to handle authentication to the aws services. 
I would recommend that you create a dedicated IAM role for all of your automatic access to your 
aws account. 

Ether will not handle managing and credentials as it is rather easy once set up and ether will always 
try to implement the default configuration as specified my aws cli and boto3  

# Project goals 
1. Finish deploy to include the -all (publish version included)
1. Build new project setup.
2. Build alias control for function version
    1. Individual endpoints
    1. All endpoints (apply same alias) 
