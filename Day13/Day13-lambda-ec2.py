import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = ec2.run_instances(
        ImageId='ami-07ebfd5b3428b6f4d',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        KeyName='pyclasskey',
        InstanceInitiatedShutdownBehavior='terminate',
        UserData="""#!/bin/bash 
                    sudo apt-get install apache2
                    sudo hostnamectl set-hostname mytestinstnace
                    """
    )
    print(response)

