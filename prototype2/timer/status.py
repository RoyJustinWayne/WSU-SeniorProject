import urllib.request
print(urllib.request.urlopen("loadbalancer_endpoint").getcode())