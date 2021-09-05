import requests
import json
URL="http://localhost:8000/new/"
#its python data
data={
    'name':'ANM',
    'roll':101,
    'city':'Software Developer'
}

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)#tis returns gthe response which will store variable r
mydata=r.json()
print(mydata)