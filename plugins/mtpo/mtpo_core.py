class MTPO:
    def __init__(self):
        self.status = "ready"

    def schedule_tasks(self, tasks):
        # จัดลำดับ task แบบ parallel / conditional
        print(f"MTPO scheduling tasks: {tasks}")
        results = [{"task": t, "status":"scheduled"} for t in tasks]
        return results

mtpo_agent = MTPO()
