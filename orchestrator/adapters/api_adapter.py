import requests
def run(repo, payload):
    return requests.post(repo['endpoint'], json=payload).json()
