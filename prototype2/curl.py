import requests

url = "AWS ENDPOINT"
headers = {"X-API-Key":"API KEY FOR AWS"}
data = '{"key":"API KEY FOR WEATHERSTATION"}'


r = requests.post(url = url, headers = headers, data = data) 


if (r.status_code == 200):
    print("Key Verified.")
    #f = open(str(keyFile), 'w')
    #f.write(key)
   # f.close()
    #verified = True
elif (r.status_code == 400):
    print("Invalid API key. Please try again.")
elif (r.status_code == 409):
    print("API key already taken. Please try again with an unused API key.")
else:
    print("Something went wrong with the server.")
