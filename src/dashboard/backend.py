import requests

class DashboardBackend:
    def __init__(self):
        self.api_url = "https://api.github.com/repos/your-repo"

    def fetch_commits(self):
        response = requests.get(f"{self.api_url}/commits")
        return response.json()

    def fetch_pull_requests(self):
        response = requests.get(f"{self.api_url}/pulls")
        return response.json()

    def fetch_issues(self):
        response = requests.get(f"{self.api_url}/issues")
        return response.json()

backend = DashboardBackend()
print(backend.fetch_commits())