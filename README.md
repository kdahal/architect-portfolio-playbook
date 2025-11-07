# Architect Portfolio Playbook

A compact, practical repository that maps **Technical Needs**, **Business Needs**, and **Leadership Skills** into tangible artifacts you can show in interviews or demos.

This repository contains:
- A small API-first service (FastAPI) demonstrating API-first design, Docker, and CI/CD.
- A Python simulation demonstrating systems modeling and troubleshooting.
- An automation toolkit for analyzing support tickets (pattern recognition).
- Kubernetes deployment manifest and CI workflow.
- Documentation and runbooks to demonstrate leadership, escalation, and process improvement.

## Why this repo
This repo was designed to demonstrate the core competencies hiring managers look for in Solution/Software/DevOps Architect roles:
- **Technical**: Python, Docker/K8s, Cloud-friendly infra, automation, API-first design, optional AI/NLP hooks.
- **Business**: Customer satisfaction and support scalability via automation and runbooks; data-driven product feedback.
- **Leadership**: Escalation playbooks, cross-team collaboration docs, patterns identification scripts, and strategic problem solving.

## Quickstart (local)
1. Run the API:
   ```bash
   cd apps/api-first-fastapi
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app:app --reload

