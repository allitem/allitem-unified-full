class Router:
    def route(self, task, repos):
        return [r for r in repos if task in r.get('tasks', [])]
