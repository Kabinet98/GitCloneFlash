url = 'https://github.com/alterthedeveloper26/employee-management.git'

def getGitOwnerAndRepository(gitUrl):
    extractOwnerAndRepositoryList = gitUrl.split('/')[3::]
    getOwnerAndRepositoryList = []
    for i in extractOwnerAndRepositoryList:
        if i.endswith('.git'):
            i = i.replace('.git', '')
        getOwnerAndRepositoryList.append(i)
    return getOwnerAndRepositoryList

print(getGitOwnerAndRepository(url))