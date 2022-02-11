from operator import concat
import os 
import csv
import sys
from interaction import *

class gitCloneFlash:
    def __init__(self):
        self
    
    def getGitOwnerAndRepository(self, listOfGitUrl):
  
        OwnerAndRepositoryList = {}
        for links in listOfGitUrl:
            if not ('https://github.com/') in links:
                listOfGitUrl.remove(links)
       
        for gitLink in listOfGitUrl:
            owner = gitLink.split('/')[3]
            OwnerAndRepositoryList[owner]= os.path.basename(gitLink).replace('.git', '')
            
        return OwnerAndRepositoryList
        
    def generateMooseModel(self, listOfCvsDatas):
        self.cloneRepositories(self.retrieveGitUrlFromCsvFile(listOfCvsDatas)) 
        repository = input(FamixImporterPath)
        self.checkPathExistence(repository)
        for folders in os.listdir(os.getcwd()):
            if(str(concat(folders, '.git')) in self.checkClonableFolder(listOfCvsDatas)):
                folderCurrentPath = os.getcwd()+'/'+folders
                self.executeFamixImporter(repository, folderCurrentPath, folders)   
            else:
                continue 
            
    def checkClonableFolder(self, listOfEachCsvFileRow):
        git = [url[1] for url in listOfEachCsvFileRow]
        new = []
        for element in git:
            if(element.endswith('.git')):
               element = element.split('/')[-1]
               new.append(element)
        return new
                       
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
        else:
           #self.cloneRepositories(self.retrieveGitUrlFromCsvFile(csvfilerows))
           #self.generateMooseModel(csvfilerows)   
           print(self.getGitOwnerAndRepository(self.retrieveGitUrlFromCsvFile(csvfilerows)))
        
        
        
        
    
                
            
        

      
if __name__ =='__main__':
    #? These line of codes will allow the system to accept some arguments to execute the script
    fileDirectory = sys.argv[1]
    gitclone = gitCloneFlash()
    gitclone.CloneFlash(fileDirectory)
         