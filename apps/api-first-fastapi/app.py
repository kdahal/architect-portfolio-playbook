from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid

app = FastAPI(title="ArchitectPlaybook API", version="0.1.0")

class Issue(BaseModel):
    id: Optional[str]
    title: str
    description: str
    priority: Optional[str] = "medium"
    tags: Optional[List[str]] = []

store = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/issues", response_model=Issue)
def create_issue(issue: Issue):
    issue.id = str(uuid.uuid4())
    store[issue.id] = issue.dict()
    return issue

@app.get("/issues/{issue_id}", response_model=Issue)
def get_issue(issue_id: str):
    issue = store.get(issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue
