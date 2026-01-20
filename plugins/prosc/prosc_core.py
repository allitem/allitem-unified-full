from plugins.mtpo.mtpo_core import mtpo_agent
from plugins.ceo_ai.ceo_core import ceo_agent
from plugins.decid_ai.decision_core import decid_agent

class PROSC:
    def __init__(self):
        self.status = "ready"

    def orchestrate(self, tasks, reports):
        # 1. MTPO schedule
        scheduled = mtpo_agent.schedule_tasks(tasks)
        # 2. Decid AI decide
        prioritized = decid_agent.decide(scheduled)
        # 3. CEO AI evaluate
        commands = ceo_agent.evaluate_and_command(reports)
        return {"scheduled": scheduled, "prioritized": prioritized, "commands": commands}

prosc_agent = PROSC()
