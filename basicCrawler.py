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
GITHUB_TOKEN_2 = os.getenv("GITHUB_TOKEN_2", "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")

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN_2}"
}


# Save dirctory
SAVE_DIR = "/mnt/d/1stp_cursor/cursorrules_files"
os.makedirs(SAVE_DIR, exist_ok=True)


'''
# Create SQLite database
conn = sqlite3.connect("cursorrules0221.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursorrules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fileID UNIQUE,
        file_name TEXT,
        file_url TEXT,
        raw_url TEXT UNIQUE,
        repo_name TEXT,
        repo_owner TEXT,
        repo_url TEXT,
        stars INTEGER,
        forks INTEGER,
        watchers INTEGER,
        contributors INTEGER,
        last_updated TEXT,
        issues INTEGER,
        releases INTEGER,
        commits INTEGER,
        languages TEXT,
        owner_followers INTEGER,
        owner_public_repos INTEGER,
        owner_created_at TEXT
    );
""")
conn.commit()




# Generate unique ID for each file with raw_url
def gen_fileID(raw_url):
    # 获取raw_url的有效部分：去掉通用前缀、替换'/'为'_'
    # valid_part = raw_url.replace("https://raw.githubusercontent.com/", "")
    # valid_part = valid_part.replace("/", "_")
    fileID = hashlib.sha1(raw_url.encode()).hexdigest();
    return fileID
    



# Get metadata of repository
def get_repo_metadata(raw_url, owner, repo):
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_data = requests.get(repo_url, headers=HEADERS)
    # Print repo_data. Check if the number of contributors and commits are right.
    # Check API requests
    if repo_data.status_code != 200:
        print(f"Error fetching repo metadata: {repo_data.status_code}")
        return {}
    
    repo_json = repo_data.json()
    print(f"\nRepo json: {repo_json}")
    
    languages_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    # languages_data = requests.get(languages_url, headers=HEADERS)
    # languages_json = languages_data.json() if languages_data.status_code == 200 else {}
    languages_data = json.loads(metadata["languages"])
    for lang, percent in languages_data.items():
        cursor.execute("INSERT INTO languages (raw_url, file_id, language, percentage) VALUES (?, ?, ?, ?)",(raw_url, file_id, lang, percent))

    
    # Calculate the percentage of languages 
    total_bytes = sum(languages_json.values()) if languages_json else 0
    languages = json.dumps({lang: round(size / total_bytes * 100, 2) for lang, size in languages_json.items()}) if total_bytes > 0 else "{}"
    

    
    return {
        "stars": repo_json.get("stargazers_count", 0),
        "forks": repo_json.get("forks_count", 0),
        "watchers": repo_json.get("subscribers_count", 0),
        "contributors": repo_json.get("contributors", 0),
        "last_updated": repo_json.get("updated_at", ""),
        "issues": repo_json.get("open_issues_count", 0),
        "releases": repo_json.get("has_releases", 0),
        "commits": repo_json.get("has_downloads", 0),
        "languages": languages
    }



# Get reputation of the owner
def get_user_info(username):
    user_url = f"https://api.github.com/users/{username}"
    user_data = requests.get(user_url, headers=HEADERS)

    if user_data.status_code != 200:
        return {"followers": 0, "public_repos": 0, "created_at": ""}

    user_json = user_data.json()
    print(f"\nUser json: {user_json}")
    
    
    return {
        "owner_followers": user_json.get("followers", 0),
        "owner_public_repos": user_json.get("public_repos", 0),
        "owner_created_at": user_json.get("created_at", "")
    }
'''


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
            

# Get metadata of repository
def get_repo_metadata(owner, repo):
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_data = requests.get(repo_url, headers=HEADERS)
    # Check API requests
    if repo_data.status_code != 200:
        print(f"Error fetching repo metadata: {repo_data.status_code}")
        return {}
    
    repo_json = repo_data.json()
    
    languages_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    languages_data = requests.get(languages_url, headers=HEADERS)
    languages_json = languages_data.json() if languages_data.status_code == 200 else {}
    
    # Calculate the percentage of languages 
    total_bytes = sum(languages_json.values()) if languages_json else 0
    languages = json.dumps({lang: round(size / total_bytes * 100, 2) for lang, size in languages_json.items()}) if total_bytes > 0 else "{}"
    
    # releases_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    # commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    # contributors_url = f"https://api.github.com/repos/{owner}/{repo}/contributors" 
    # releases_data = requests.get(releases_url, headers=HEADERS)
    # commits_data = requests.get(commits_url, headers=HEADERS)
    # contributors_data = requests.get(contributors_url, headers=HEADERS) 
    
    return {
        "stars": repo_json.get("stargazers_count", 0),
        "forks": repo_json.get("forks_count", 0),
        "watchers": repo_json.get("subscribers_count", 0),
        "contributors": repo_json.get("contributors", 0),
        "last_updated": repo_json.get("updated_at", ""),
        "issues": repo_json.get("open_issues_count", 0),
        "releases": repo_json.get("has_releases", 0),
        "commits": repo_json.get("has_downloads", 0),
        "languages": languages
    }



# Get reputation of the owner
def get_user_info(username):
    user_url = f"https://api.github.com/users/{username}"
    user_data = requests.get(user_url, headers=HEADERS)

    if user_data.status_code != 200:
        return {"followers": 0, "public_repos": 0, "created_at": ""}

    user_json = user_data.json()
    return {
        "owner_followers": user_json.get("followers", 0),
        "owner_public_repos": user_json.get("public_repos", 0),
        "owner_created_at": user_json.get("created_at", "")
    }



            

            

            

            

            

            

            
        return results
    elif response.status_code == 403:
        print("Rate limit exceeded. Sleeping for 60 seconds...")
        time.sleep(60)
        return search_cursorrules_files(page, per_page)
    else:
        print(f"GitHub API Error: {response.status_code} - {response.text}")
        return []



# Save data to SQLite
'''
def save_to_db(metadata_list):
    for metadata in metadata_list:           
        # gen_fileID(raw_url)
        fileID = gen_fileID(metadata["raw_url"])
        
        print("\n[Check the table tags and count the number:] ", fileID, metadata["file_name"], metadata["file_url"], metadata["raw_url"],
            metadata["repo_name"], metadata["repo_owner"], metadata["repo_url"],
            metadata["stars"], metadata["forks"], metadata["watchers"],
            metadata["contributors"], metadata["last_updated"],
            metadata["issues"], metadata["releases"], metadata["commits"],
            metadata["languages"],
            metadata["owner_followers"], metadata["owner_public_repos"], metadata["owner_created_at"])
        
        
        cursor.execute("""
        INSERT INTO cursorrules (fileID, file_name, file_url, raw_url, repo_name, repo_owner, repo_url, stars, forks, watchers, contributors, last_updated, issues, releases, commits, languages, owner_followers, owner_public_repos, owner_created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            fileID, metadata["file_name"], metadata["file_url"], metadata["raw_url"],
            metadata["repo_name"], metadata["repo_owner"], metadata["repo_url"],
            metadata["stars"], metadata["forks"], metadata["watchers"],
            metadata["contributors"], metadata["last_updated"],
            metadata["issues"], metadata["releases"], metadata["commits"],
            metadata["languages"],
            metadata["owner_followers"], metadata["owner_public_repos"], metadata["owner_created_at"]
        ))
    conn.commit()
    print("Save Data In The Database Successfully!\n")



# Download .cursorrules files
# Download the file via file url
# Then save the file via another function
def download_file(file_url, file_path): 
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Download Successfully: {file_path}")
        else:
            print(f"Download Failed: {file_url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"Exception Occurred: {e}")
        

'''


def main():
    # 1. Search Github, get response (json)
    # def search_cursorrules_files(page=1, per_page=100, created_since=None):
    metadata_list = search_cursorrules_files(1, 2)   
    
    # 2. Save data to the tables (cursorruls and languages)
    # def save_to_db(metadata_list):
    # save_to_db(metadata_list)
    
    # conn.close
    
    





main()
    
    
    
    

