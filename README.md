# GitcloneFlash ⚡️

GitcloneFlash is a script developed in python allowing users to clone all retrieved github typeScript repositories from a Csv file and create a json template which will be used in Moose to analyze the cyclomatic complexity of the cloned projects and also create a file csv containing the statistics of the different projects like: the number of stars, of commits, etc ...
![NPM](https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Warning

Github doesn't allow multiples requests at the same time, so make sure to put inside the CSV file only 10 repositories at the same time, otherwise you will  be facing some errors while compiling. If you get some errors when generating the stats for projects, try changing your internet connexion so your IP address will change and you will be able to generate the stats.

## Instructions

Install requests via pip depending on your OS

Inside the CSV file that you're going to provide, you  must follow this syntax: projectName, GitURl with .git extension.

## Example

Redux, https://github.com/reduxjs/redux.git

## NB
Keep in mind that you must provide only 100% typescript project like this project below:

TypeScript-Game, https://github.com/GuidovdRiet/typescript-game.git

And the Data folder above is just a folder including some CSV files that contain  projects for test purposes (All projects are not 100% typeScript)

If they ask you to provide the FamixTypeScriptImporter directory: you can provide the relative link like: 
```
/Download/FamixTypeScriptImporter
```

## Installation and Execution

You need to install [python](https://www.python.org/downloads/) to execute this script and you need to follow all installation instructions of [FamixTypeScriptImporter](https://github.com/Arezoo-Nasr/FamixTypeScriptImporter).
Make sure to be in the same directory than the script to execute this command.

```
python gitCloneFlash.py csvFileDirectory
```
