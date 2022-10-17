import requests
import json

def getRepo(username):
    link = ("https://api.github.com/users/" + username + "/repos")
    data = requests.get(link)
    repo = json.loads(data.text)
    repos = []

    for Repo in repo:
        try:
            repos.append(Repo.get("name"))
        except:
            repos = []
    
    return repos

def getCommits(username,name):
    link = "https://api.github.com/repos/" + username + "/" + name + "/commits"
    data = requests.get(link)
    cmts = json.loads(data.text)
    num = len(cmts)

    return cmts

if __name__ == "__main__":
    username = input("Enter the username of the github account")
    repos = getRepo(username)
    for rep in repos:
        num = getCommits(username , repos)
        print("Name :- " + rep + "No of commits in the repo :- " + str(num))
        
