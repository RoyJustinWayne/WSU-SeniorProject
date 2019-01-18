import boto3

class NewConnection(object):
    
    def elb_connect(self, **options):
        elb = boto3.client('elb')
        response=elb.create_load_balancer(options)
        return response
