
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ngivbt.atlassian.net/rest/api/3/project"
API_TOKEN = ""
auth = HTTPBasicAuth("mail_id", API_TOKEN)

headers = {
    "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) #print in json format

output = json.loads(response.text)

name = output[0]["name"]

print(name)


