from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# Create a Flask app instance
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://ngivbt.atlassian.net/rest/api/3/issue"
    API_TOKEN = ""
    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "My first jira ticket",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "KAN"
            },
            "issuetype": {
                "id": "10013"
            },
            "summary": "First JIRA Ticket"
        },
        "update": {}
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
