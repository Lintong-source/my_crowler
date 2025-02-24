import requests
import os

# GITHUB_TOKEN: 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
# GITHUB_TOKEN_2: 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
GITHUB_TOKEN_2 = os.getenv("GITHUB_TOKEN_2")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN_2}"
}

response = requests.get("https://api.github.com/rate_limit", headers=HEADERS)
print(response.json())


#在终端中运行以下命令，直接检查GitHub API能否返回JSON数据。 如果返回了，说明爬虫的查询语句是正确的，能爬到数据。
#curl -H "Accept: application/vnd.github.v3+json" \
#-H "Authorization: token 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" \
#"https://api.github.com/search/code?q=filename:.cursorrulesORfilename:.cursorruleORfilename:cursorrulesORfilename:cursorrule&per_page=10&page=1"
# 最终用这个查到了(q=in:file代表只查询文件名，不匹配文件内容)：
#curl -H "Accept: application/vnd.github.v3+json" \
#-H "Authorization: token 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" \
#"https://api.github.com/search/code?q=in:file%20filename:.cursorrules%20OR%20filename:.cursorrule%20OR%20filename:cursorrules%20OR%20filename:cursorrule&per_page=10&page=1"
