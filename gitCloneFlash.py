from operator import concat
import os 
import csv
import sys
import platform
from interaction import *
import requests
class gitCloneFlash:
    def __init__(self):
        self
    
    def defineFormatAndGetRequestFrom(self, text, url, repository):
        return requests.get(str(text).format(url, repository))
    
    def getGitOwnerAndRepository(self, listOfGitUrl):
        OwnerAndRepositoryList = {}
        for links in listOfGitUrl:
            if not ('https://github.com/') in links:
                listOfGitUrl.remove(links)
       
        for gitLink in listOfGitUrl:
            owner = gitLink.split('/')[3]
            OwnerAndRepositoryList[owner] = os.path.basename(gitLink).replace('.git', '')
            
        return OwnerAndRepositoryList
    
    def getGitRepositoryStats(self, listOfGitUrl):
        header = ['Repository_Name', 'Contributions_Number', 'Forks_count', 'Pull_Request_Number', 'Issues_Number', 'Commits_Number', 'Stars_Number'];
        data = []
        listOfOwnerAndRepository = self.getGitOwnerAndRepository(listOfGitUrl)
        contributorsNumber = ''
        pullRequestNumber = ''
        issueNumber = ''
        commitsNumber = ''
        
        for ownerName, repositoryName in listOfOwnerAndRepository.items():
            getContributors = self.defineFormatAndGetRequestFrom('https://api.github.com/repos/{0}/{1}/contributors', ownerName, repositoryName)
            getNumberOfForks = self.defineFormatAndGetRequestFrom('https://api.github.com/repos/{0}/{1}', ownerName, repositoryName)
            getNumberOfPullRequests = self.defineFormatAndGetRequestFrom('https://api.github.com/repos/{0}/{1}/pulls', ownerName, repositoryName)
            getIssueNumber = self.defineFormatAndGetRequestFrom('https://api.github.com/repos/{0}/{1}/issues', ownerName, repositoryName)
            getCommitsNumber = self.defineFormatAndGetRequestFrom('https://api.github.com/repos/{0}/{1}/stats/contributors', ownerName, repositoryName)
            
            starsNumber = getNumberOfForks.json()['stargazers_count']
            forksNumber = getNumberOfForks.json()['forks_count']
            
            for contributors in getContributors.json():
                contributorsNumber = contributors['contributions']
            
            for pullRequest in getNumberOfPullRequests.json():
                pullRequestNumber = pullRequest['number']
            
            for issuesNumber in getIssueNumber.json():
                issueNumber = issuesNumber['number']
            
            for commits in getCommitsNumber.json():
                commitsNumber = commits['total']
            
            data.append(
                
                {'Repository_Name':repositoryName ,
                 'Contributions_Number':contributorsNumber if contributorsNumber else 0,
                 'Forks_count':forksNumber if forksNumber else 0,
                 'Pull_Request_Number':pullRequestNumber if pullRequestNumber else 0, 
                 'Issues_Number': issueNumber if issueNumber else 0, 
                 'Commits_Number': commitsNumber if commitsNumber else 0,
                 'Stars_Number': starsNumber if starsNumber else 0,
                 }
            )
        
        with open('RepositoriesStats.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
            
        return 'The Csv Stats file has been created in the following directory : {0} '.format(os.getcwd())
        
    def generateMooseModel(self, listOfCvsDatas):
        self.cloneRepositories(self.retrieveGitUrlFromCsvFile(listOfCvsDatas)) 
        repository = input(FamixImporterPath)
        self.checkPathExistence(repository)
        for folders in os.listdir(os.getcwd()):
            if(str(concat(folders, '.git')) in self.checkClonableFolder(listOfCvsDatas)):
                if(platform.system() =='Windows'):
                    pathSlash = r'\\'
                else: pathSlash = '/'
                folderCurrentPath = os.getcwd() + pathSlash + folders
                self.executeFamixImporter(repository, folderCurrentPath, folders)   
            else:
                continue 
            
    def checkClonableFolder(self, listOfEachCsvFileRow):
        git = self.retrieveGitUrlFromCsvFile(listOfEachCsvFileRow)
        folders = []
        for element in git:
            if(element.endswith('.git')):
               element = element.split('/')[-1]
               folders.append(element)
        return folders
                       
    def retrieveGitUrlFromCsvFile(self, listOfEachCsvFileRow):
        return [url[1] for url in listOfEachCsvFileRow]
    
    def checkPathExistence(self, path, changeDirectory = None):
        while(not os.path.exists(path)):
            path = input(WrongPathDirectory)
        if(changeDirectory == 'yes'):
            return os.chdir(path)
        return path

    def cloneRepositories(self, listOfEachCsvFileUrls):
        for url in listOfEachCsvFileUrls:
            os.system('git clone '+url)
            
    def checkFileExists(self, path):
        while not os.path.isfile(path):
            path = input(WrongPathDirectory)
        return path
    
    def executeFamixImporter(self, directory, folder, basename):
        return os.system('cd '+directory+' && ts-node src/ts2famix-cli.ts -i "'+folder+'/**/*.ts" -o '+ os.path.basename(basename)+'.json')


    def checkCsvFileExistance(self, fileDirectory):
        csvfileDatas = []
        try:
            with open(self.checkFileExists(fileDirectory), 'r') as f:
                csvreader = csv.reader(f)
                for row in csvreader: 
                    csvfileDatas.append(row)
            return csvfileDatas
        except FileNotFoundError:
            self.checkFileExists(fileDirectory)
        
    
    def CloneFlash(self, fileDirectory):
        csvfilerows = self.checkCsvFileExistance(fileDirectory) 
        repository = input(yesOrNoInput) 
        while(repository.lower() not in  ('yes', 'no')):
            repository = input(WrongYesOrNoInput)
        if(repository.lower() == 'yes'):
            repository = input(repositoryPathInput)
            self.checkPathExistence(repository, 'yes') 
            self.generateMooseModel(csvfilerows)
            print(self.getGitRepositoryStats(self.retrieveGitUrlFromCsvFile(csvfilerows)))
        else:
            self.cloneRepositories(self.retrieveGitUrlFromCsvFile(csvfilerows))
            self.generateMooseModel(csvfilerows)   
            print(self.getGitRepositoryStats(self.retrieveGitUrlFromCsvFile(csvfilerows)))
           
        
      
if __name__ =='__main__':
    #? These line of codes will allow the system to accept some arguments to execute the script
    fileDirectory = sys.argv[1]
    gitclone = gitCloneFlash()
    gitclone.CloneFlash(fileDirectory)
         