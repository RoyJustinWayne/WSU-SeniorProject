import json
import boto3
import time

autoscaling = boto3.client('autoscaling')

def create_auto_scaling():
    response = autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='lambda-auto-scaling-group-test1',
    AvailabilityZones=[
        'us-east-1c',
        'us-east-1f',
    ],
    HealthCheckGracePeriod=120,
    HealthCheckType='ELB',
    LaunchConfigurationName='lambda-launch-config-test1',
    TargetGroupARNs=[
        'arn:aws:elasticloadbalancing:us-east-1:667671192261:targetgroup/my-targets-test2/5cc8bf82f10050be',
    ],
    MaxSize=2,
    MinSize=1,
)

    print("auto scaling response-->>",response)

def lambda_handler(event, context):
    

    create_auto_scaling()
    return {
        'statusCode': 200,
        'body': json.dumps('done')
    }
