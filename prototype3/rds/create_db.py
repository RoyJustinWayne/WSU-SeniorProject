import json
import boto3

rds = boto3.client('rds')

def create_db():
    response = rds.create_db_instance(
    DBName='db1',
    DBInstanceIdentifier='lambda-db1',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.small',
    Engine='MySQL',
    MasterUsername='wsu',
    MasterUserPassword='masterpass',
    AvailabilityZone='us-east-2a',
    BackupRetentionPeriod=0,
    Port=3306,
    MultiAZ=False,
    EngineVersion='5.7',
    AutoMinorVersionUpgrade=True,
    LicenseModel='general-public-license',
    PubliclyAccessible=True,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'lambda_db_instanceVal'
        },
    ],
    StorageType='gp2',
    StorageEncrypted=True,
    KmsKeyId='c7j34oj5-5d76-43u5-97bb-e93ku98153a0',
    CopyTagsToSnapshot=True|False,
    EnableIAMDatabaseAuthentication=False,
    EnablePerformanceInsights=False
)


def lambda_handler(event, context):
    
    create_db()
    return {
        'statusCode': 200,
        'body': json.dumps('completed')
    }
