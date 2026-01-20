import yaml

class RepoRegistry:
    def __init__(self, path):
        with open(path) as f:
            self.repos = yaml.safe_load(f).get('repos', [])

    def all(self):
        return self.repos
