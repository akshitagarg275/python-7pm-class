# API Handling
# Application Programming Interface
'''
HTTP Methods
GET -> To retrieve the data
POST -> To send the data to the server
PUT -> To Update the data
DELETE -> To Delete the data
'''

import requests
import json

try: 

    url = "https://randomuser.me/api/"
    # url = ""
    res = requests.get(url)

    # print(res.status_code)
    # print(res.text)
    data = json.loads(res.text)
    # print(type(data))
    fname = data['results'][0]['name']['first']
    lname = data['results'][0]['name']['last']
    email = data['results'][0]['email']
    # print(fname)
    # print(lname)
    print(email)
    

except BaseException as e:
    print("ERROR: ",e)