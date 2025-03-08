from fastapi import FastAPI
import requests

app = FastAPI()

# Dummy function to fetch Salesforce cases (Replace with actual API calls)
def fetch_salesforce_cases():
    return [
        {"id": "SF001", "title": "Login issue", "description": "User unable to login"},
        {"id": "SF002", "title": "Payment failure", "description": "Card declined"},
    ]

# Dummy function to fetch Jira issues (Replace with actual API calls)
def fetch_jira_issues():
    return [
        {"id": "JIRA-101", "title": "Login not working", "description": "Users facing login failure"},
        {"id": "JIRA-102", "title": "Payment gateway error", "description": "Payment not processing"},
    ]

# Simple Matching Logic (Find similar titles)
def find_similar_cases(new_case):
    salesforce_cases = fetch_salesforce_cases()
    jira_issues = fetch_jira_issues()
    
    matches = []
    
    for case in salesforce_cases + jira_issues:
        if new_case.lower() in case["title"].lower():
            matches.append(case)
    
    return matches

@app.get("/match-case/{case_title}")
def match_case(case_title: str):
    matches = find_similar_cases(case_title)
    
    return {"case_title": case_title, "matches": matches}
