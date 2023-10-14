import requests
import json

def gapi(username):
    url = requests.get("https://api.github.com/users/"+username+"/repos")
    #check whether the username is valid or not

    if url.status_code != 200:
        print("This is not a valid username")
        return False
    url = url.json()
    l = len(url)
    if l == 0:
        print("There are no repositories in the account")
    #to get the number of commits
    for rep in url:
        commits = requests.get(rep['commits_url'].split("{")[0])
        commits = commits.json()
        print("Name : " + rep['name'] + "           Total number of commits is :- " + str(len(commits)))
if __name__ == '__main__':
    name = input("Enter the github username :- ")
    gapi(name)
    
