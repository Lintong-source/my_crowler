import requests
import os
import time
import sqlite3
import json
import re
import hashlib

# GITHUB_TOKEN: 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
# GITHUB_TOKEN_2: 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
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


# GitHub API configuration
GITHUB_API_URL = "https://api.github.com/search/code"
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "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")

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {'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'}"
}


# Save dirctory
SAVE_DIR = "/mnt/d/1stp_cursor/cursorrules_files"
os.makedirs(SAVE_DIR, exist_ok=True)



# Define GitHub Search
def search_cursorrules_files(page, per_page):
    # Replace the spaces ' ' with '20%' when checking query sentences directly with the curl command
    query = "in:file filename:.cursorrules OR filename:.cursorrule OR filename:cursorrules OR filename:cursorrule"
    query += " -repo:alpgul/Cursorrules-Database -repo:PatrickJS/awesome-cursorrules"

    params = {"q": query, "sort": "indexed", "order": "desc", "per_page": per_page, "page": page}
    response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)
    print(f"GitHub API Response: {response.status_code} - {response.text}\n")

    

    
    results = []
    if response.status_code == 200:
        for item in response.json().get("items", []):
            fileSHA = item["sha"]
            raw_url = item["html_url"].replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            repo = item["repository"]
            owner = repo["owner"]
            
            print("\n[Check the table tags and count the number:] \n")
            print(f"## 1. fileSHA: {fileSHA}\n")
            ## 1. fileSHA: 3f3d035b90d4c5b4709033dd178d421932ddba21
            
            print(f"## 2. file_url: {item["url"]}\n")
            ## 2. file_url: https://api.github.com/repositories/40187375/contents/.cursorrules?ref=1e7af4a0066b6df6eab65abc6c4e6050612100a0
            
            print(f"## 3. raw_url: {raw_url}\n")
            ## raw_url: https://raw.githubusercontent.com/MultiQC/MultiQC/1e7af4a0066b6df6eab65abc6c4e6050612100a0/.cursorrules
            
            #print(f"## 4. file_last_updated: {raw_url}\n")
            ## 4. ?
            
            print(f"## 5. repo_name: {repo["name"]}\n")
            ## repo_name: MultiQC
            
            print(f"## 6. repo_id: {repo["id"]}\n")
            ## repo_id: 40187375
            
            print(f"## 7. repo_url: {repo["url"]}\n")
            ## repo_url: https://api.github.com/repos/MultiQC/MultiQC
            
            print(f"## 8. repo_stars: {repo["stargazers_url"]}\n")
            ## repo_stars: https://api.github.com/repos/MultiQC/MultiQC/stargazers
            
            print(f"## 9. repo_forks: {repo["forks_url"]}\n")
            ## repo_forks: https://api.github.com/repos/MultiQC/MultiQC/forks
            
            #print(f"## 10. repo_watchers: {repo[""]}\n")
            ## 10. ?
            
            print(f"## 11. repo_contributors: {repo["contributors_url"]}\n")
            ## repo_contributors: https://api.github.com/repos/MultiQC/MultiQC/contributors
            
            #print(f"## 12. repo_last_updated: {repo[""]}\n")
            ## 12. ?
            
            print(f"## 13. repo_issues: {repo["issues_url"]}\n")
            ## repo_issues: https://api.github.com/repos/MultiQC/MultiQC/issues{/number}
            
            print(f"## 14. repo_releases: {repo["releases_url"]}\n")
            ## repo_releases: https://api.github.com/repos/MultiQC/MultiQC/releases{/id}
            
            print(f"## 15. repo_subscribers: {repo["subscribers_url"]}\n")
            ## repo_subscribers: https://api.github.com/repos/MultiQC/MultiQC/subscribers
            
            #print(f"## . repo_pull_request: {owner["id"]}\n")
            ## . ?
            
            print(f"## 16. repo_languages: {repo["languages_url"]}\n")
            ## repo_languages: https://api.github.com/repos/MultiQC/MultiQC/languages
            
            print(f"## 17. owner: {owner["login"]}\n")
            ## owner: MultiQC
            
            print(f"## 18. owner_ID: {owner["id"]}\n")
            ## owner_ID: 18548644
            
            print(f"## 19. owner_followers: {owner["followers_url"]}\n")
            ## owner_followers: https://api.github.com/users/MultiQC/followers
            
            print(f"## 20. owner_public_repos: {owner["repos_url"]}\n")
            ## owner_public_repos: https://api.github.com/users/MultiQC/repos
            
            print(f"## 21. owner_stars: {owner["starred_url"]}\n")
            ## owner_stars: https://api.github.com/users/MultiQC/starred{/owner}{/repo}
            
            #print(f"## 22. owner_created_at: {owner["id"]}\n")
            ## 22. ?
            
            #print(f"## 23. owner_forks: {owner["id"]}\n")
            ## 22. ?


search_cursorrules_files(1, 2)   

