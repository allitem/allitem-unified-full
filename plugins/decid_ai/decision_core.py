class DecidAI:
    def __init__(self):
        self.status = "ready"

    def decide(self, tasks):
        # Decision engine (rule-based + AI)
        print("Decid AI deciding task priorities...")
        prioritized = sorted(tasks, key=lambda x: x.get("priority",0), reverse=True)
        return prioritized

decid_agent = DecidAI()
