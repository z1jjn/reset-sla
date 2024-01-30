import requests
import json

JIRA_USERNAME = "replace with your email"
JIRA_API_TOKEN = "replace with your token"
headers = {
        "Content-Type": "application/json",
    }

def get_keys():
    endpoint = 'https://replace with your instance url.atlassian.net/rest/api/3/search'
    jql_query = "replace with your query"
    auth = (JIRA_USERNAME, JIRA_API_TOKEN)
    headers = {
        "Content-Type": "application/json",
    }
    params = {
        "jql": jql_query,
        "fields": ["key"],
        "maxResults": 1000,
    }
    response = requests.get(endpoint, params=params, headers=headers, auth=auth)
    if response.status_code == 200:
        data = response.json()
        issue_keys = [issue['key'] for issue in data.get('issues', [])]
        return issue_keys
    else:
        raise Exception("Error fetching data from Jira.")

if __name__ == "__main__":
    auth = (JIRA_USERNAME, JIRA_API_TOKEN)
    url = 'https://replace with your instance url.atlassian.net/rest/servicedesk/1/servicedesk/sla/admin/task/destructive/reconstruct?force=true' 
    payload = get_keys()
    json_payload = json.dumps(payload)
    response = requests.post(url, data=json_payload, headers=headers, auth=auth)
    if response.status_code == 200:
        print("Request was successful!")
        print("Response:", response.text)
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)