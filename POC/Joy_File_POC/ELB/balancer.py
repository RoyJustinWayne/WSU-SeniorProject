import json 
from connection import NewConnection

class LoadBalancer(object):

    __availabilityZone = "us-east-2"
    __securityGroup = ""
    __name = "default_name"

    def __init__(self, protocol, port, **instance):
        self.protocol=protocol
        self.port=port
        if 'instanceProtocol' in instance:
            self.instanceProtocol = instance['instanceProtocol']
        else:
            self.instanceProtocol = "HTTP"
        if 'instancePort' in instance:
            self.instancePort = instance['instancePort']
        else:
            self.instancePort = 80

    def setBalancerName(self, name):
        self.__name = name
        return self.__name

    def setupListener(self):
        """Set up listeners for application load balancer"""

        self.Listeners = {
                'Protocol':self.protocol,
                'LoadBalancerPort':self.port,
                'InstanceProtocol': self.instanceProtocol,
                'InstancePort': self.instancePort
        }
        return self.Listeners

    def setAvailabilityZone(self, zone):
        """defines an availability zone for the load balancer"""
        self.__availabilityZone = zone
        return self.__availabilityZone

    def setSubnet(self, **subnets):
        """will work on this later"""
        pass

    def setSecurityGroups(self, group):
        """grabs the id of the security group and assigns it to the balancer"""
        self.__securityGroup = group
        return self.__securityGroup

    def setTags(self, **tags):
        """setter to specify tags if user wants tag their balancer"""
        if 'Key' in tags and 'Value' in tags:
            self.tags = tags
            return self.tags

    def commit(self):
        """finally commit all the data and create an elb"""
        res = NewConnection()
        self.__url = res.elb_connect(
            LoadBalancerName= self.__name,
            Listeners=[
                self.Listeners,
            ],
            AvailabilityZones=[
                self.__availabilityZone,
            ],
            Subnets=[
                'subnet-1',
                'subnet-2'
            ],
            SecurityGroups=[
                self.__securityGroup,
            ],
            Tags=[
                self.tags,
            ]
        )
        return self.__url

    def getURL(self):
        """returns DNS name in the event of a successful creation"""
        return self.__url
    