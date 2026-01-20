from fastapi import FastAPI
from orchestrator.core.registry import RepoRegistry
from orchestrator.core.router import Router
from orchestrator.core.event_bus import EventBus

app = FastAPI()
registry = RepoRegistry('orchestrator/config/repos.yaml')
router = Router()
event_bus = EventBus()

@app.post("/execute")
def execute(task: str, payload: dict):
    targets = router.route(task, registry.all())
    # Publish event for QVNT or SC
    event_bus.publish(task, payload)
    return {"task": task, "targets": targets, "payload": payload}
