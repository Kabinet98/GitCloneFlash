import requests

first_url = 'https://api.github.com/repos/alterthedeveloper26/employee-management/contributors'
url = 'https://api.github.com/repos/altherthedeveloper26/employee-management.git/forks'
def getNumberOfForks(url):
    numberOfForks = requests.get(url)
    return numberOfForks.json()

print(getNumberOfForks(first_url))