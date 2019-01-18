import json
import boto3

ec2 = boto3.client('ec2')
def crash_instance(id):
    
    response = ec2.stop_instances(
        InstanceIds=[
            id,
        ]
    )
    return response

def lambda_handler(event, context):
    filters = [{'Name': 'tag:Name', 'Values': ['MAIN-ELB-Instance']}] 
    response = ec2.describe_instances(Filters=filters)
    print("EC2 RESPONSE--> ", response)
    reservation = response['Reservations'][0]
    instances = reservation['Instances'][0]
    id = instances['InstanceId']
    print("type-->: ", id)
    crash_instance(id)
    
    # instances = ec2.instances.filter(
    #     Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    # for instance in instances:
    #     # print(instance.id, instance.instance_type)
    #     res = instance.id, instance.instance_type
    #     print(res)
        
    return {
        "headers":{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        "statusCode": 200,
        "body": json.dumps("Instance: "+id+" is being killed!")
        }