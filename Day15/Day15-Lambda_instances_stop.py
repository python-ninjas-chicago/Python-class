import boto3

ec2 = boto3.client('ec2')


def lambda_handler(event, context):
    instances_list = []
    ec2_response = ec2.describe_instances(DryRun=False, MaxResults=123)
    # print(ec2_response)
    for instance in ec2_response['Reservations']:
        instances_list.append(instance['Instances'][0]['InstanceId'])
    print(instances_list)
    try:
        response = ec2.stop_instances(InstanceIds=instances_list)
        print(response)
    except:
        print("no instances to stop")
