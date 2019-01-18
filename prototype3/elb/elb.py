import json
import boto3

elb = boto3.client('elb')
ec2 = boto3.client('ec2')

def getVpcIds():
    response = ec2.describe_vpcs(
    
)   
    json_resp = json.dumps(response)
    json_load = json.loads(json_resp)
    vpcs = json_load['Vpcs'][0]
    vpc_id = vpcs['VpcId']
    return vpc_id

def getSubnets(id):
    response = ec2.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                id,
            ],
        },
    ],
)
    json_resp = json.dumps(response)
    json_load = json.loads(json_resp)
    Subnets = json_load['Subnets']
    print("subnets response---->",Subnets)
    list_sub = []
    for r in Subnets:
        print("Subnets-->", r['SubnetId'])
        list_sub.append(r['SubnetId'])
    # print(list_sub)     
    return list_sub    
    
def create_load_balancer(sub, s_group):
    response = elb.create_load_balancer(
        LoadBalancerName='lambda-ELB-test',
        Listeners=[
            {
                'Protocol': 'HTTP',
                'LoadBalancerPort': 80,
                'InstanceProtocol': 'HTTP',
                'InstancePort': 80
            },
        ],
        Subnets=[
            sub[0],
            sub[1],
        ],
        SecurityGroups=[
            s_group,
        ],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'NAME_lambda_ELB_test1'
            },
        ]
    )
    print("ELB Response: ",response)
    
def lambda_handler(event, context):
    
    id = getVpcIds()
    print("vpc_id--->", id)
    subnets = getSubnets(id)
    print(subnets)
    security_group_ID = "sg-3435467iukdfgdf" 
    create_load_balancer(subnets, security_group_ID)
    return {
        'statusCode': 200,
        'body': json.dumps('done')
    }
