from operator import concat
import os 
import csv
import sys
from interaction import *


class gitCloneFlash:
    def __init__(self):
        self
    
    def getGitOwnerAndRepository(self, listOfGitUrl):
        extractOwnerAndRepositoryList = [gitUrl.split('/')[3::] for gitUrl in listOfGitUrl][1::]
        return extractOwnerAndRepositoryList
        
        #getOwnerAndRepositoryList = []
        #for i in extractOwnerAndRepositoryList:
        #    if i.endswith('.git'):
        #        i = i.replace('.git', '')
        #    getOwnerAndRepositoryList.append(i)
        #return getOwnerAndRepositoryList
        
    def generateMooseModel(self, listOfCvsDatas):
        self.cloneRepositories(self.retrieveGitUrlFromCsvFile(listOfCvsDatas)) #? clone the github repository
        repository = input(FamixImporterPath)
        self.checkPathExistence(repository)
        for docs in os.listdir(os.getcwd()):
            if(str(concat(docs, '.git')) in self.checkClonableFolder(listOfCvsDatas)):
                #? create a json model that's going to be used in Moose
                self.executeFamixImporter(repository, docs, docs)   
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
        #? This function retrieve all urls inside a list of csv file rows and gather them inside an array
        return [url[1] for url in listOfEachCsvFileRow]
    
    def checkPathExistence(self, path, changeDirectory = None):
        while(not os.path.exists(path)):
            path = input(WrongPathDirectory)
        if(changeDirectory == 'yes'):
            return os.chdir(path)
        return path

    def cloneRepositories(self, listOfEachCsvFileUrls):
        #? This function is going to clone via git all github repository urls inside the list of urls provided
        #? by listOfEachCsvFileUrls
        for url in listOfEachCsvFileUrls:
            os.system('git clone '+url)
            
    def checkFileExists(self, path):
        while not os.path.isfile(path):
            path = input(WrongPathDirectory)
        return path
    
    def executeFamixImporter(self, directory, folder, basename):
        return os.system('cd '+directory+' && ts-node src/ts2famix-cli.ts -i '+folder+'/**/*.ts -o '+ os.path.basename(basename)+'.json')
        
    def checkCsvFileExistance(self, fileDirectory):
        csvfileDatas = []
        try:
            with open(self.checkFileExists(fileDirectory), 'r') as f:
                csvreader = csv.reader(f)
                #? For each line of csv file , insert it inside the list of collected csv file rows
                for row in csvreader: 
                    csvfileDatas.append(row)
            return csvfileDatas
        except FileNotFoundError:
            self.checkFileExists(fileDirectory)
        
    
    def CloneFlash(self, fileDirectory):
        #? These line of codes will allow users to change directory to clone all github repositories 
        csvfilerows = self.checkCsvFileExistance(fileDirectory) #? list of collected csv file rows 
        
        repository = input(yesOrNoInput) #? ask user to change the current working directory
        
        while(repository.lower() not in  ('yes', 'no')):
            repository = input(WrongYesOrNoInput)
        
        if(repository.lower() == 'yes'):
            repository = input(repositoryPathInput)
            self.checkPathExistence(repository, 'yes') #? check if the current directory exists and if you need to change directory 
            self.generateMooseModel(csvfilerows)    
        else:
           self.cloneRepositories(self.retrieveGitUrlFromCsvFile(csvfilerows))
           self.generateMooseModel(csvfilerows)   
            #print(self.getGitOwnerAndRepository(self.retrieveGitUrlFromCsvFile(csvfilerows)))
        
        
        
        
    
                
            
        
       






      
if __name__ =='__main__':
    #? These line of codes will allow the system to accept some arguments to execute the script
    fileDirectory = sys.argv[1]
    gitclone = gitCloneFlash()
    gitclone.CloneFlash(fileDirectory)
         