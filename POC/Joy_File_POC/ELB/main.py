from balancer import LoadBalancer

def driver():
    load = LoadBalancer("HTTP", 80)
    print(load.setupListener())
    print(load.setAvailabilityZone('us-west-2'))
    print(load.setSecurityGroups("7892o83jj2"))
    print(load.setTags(Key="Key!!", Value="Value!!"))
    print(load.commit())

if __name__=='__main__':
    driver()
    