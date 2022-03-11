import requests
import json
#? On aura  besoin forks_count, open_issues_count, pull_requests
contributions = 'https://api.github.com/repos/trufflesuite/ganache/contributors' #? List d'éléments ['contributions']
#url = 'https://api.github.com/repos/altherthedeveloper26/employee-management.git/forks'
forks = "https://api.github.com/repos/trufflesuite/ganache" #? json ['forks_count']
pull_requests = 'https://api.github.com/repos/trufflesuite/ganache/pulls' #? ['number'] 
issues_number = 'https://api.github.com/repos/trufflesuite/ganache/issues' #? ['number']
commitsNumber = 'https://api.github.com/repos/trufflesuite/ganache/stats/contributors'
StarsNumber ='https://api.github.com/repos/trufflesuite/ganache/community/profile'



def getNumberOfForks(url):
    numberOfForks = requests.get(url)
    return type(numberOfForks.json()['forks_count'])

def getNumberOfStars(url):
    numberOfStars = requests.get(url)
    return numberOfStars.json()['stargazers_count']



def getCommitNumber(url):
    commitNumber = requests.get(url)
    for element in commitNumber.json():
        number = element['total']
    return type(number)

def getContributionsNumber(url):
    commitNumber = requests.get(url)
    for element in commitNumber.json():
        number = element['contributions']
    return type(number)

def getNumberOfPullRequest(url):
    pullRequestNumber = requests.get(url)
    for element in pullRequestNumber.json():
        number = element['number']
    return type(number)

def getIssueNumber(url):
    numberOfIssues = requests.get(url)
    for element in numberOfIssues.json():
        number = element['number']
    return type(number)


print('Stars number is {0}'.format(getNumberOfStars(forks)))
