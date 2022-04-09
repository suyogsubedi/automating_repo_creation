from create_repo_github import create_repository
from create_repo_github import *
import os
import subprocess
import time
from selenium import webdriver

def local_functionalities():

    project_name = create_repository.this_project_name
    username = create_repository.this_username
    
    # Naviagte one step back, then create the project folder
    current_location = os.getcwd()
    os.chdir("..")
    print(os.getcwd())
    print("The name of your project on the local computer and on the github will be same")
    print("###############################################################################")
    os.mkdir(project_name)
    os.chdir(project_name)
    print("###############################################################################")
    print("Your project folder will be created one directory up than the current location")

    # Initialize the git repo
    initialize_git = "git init"
    subprocess.run(initialize_git, shell=True, check=True)

    generate_readme= "touch readme.md"
    subprocess.run(generate_readme,shell=True,check=True)
    # Writing on readme.md file
    subprocess.run(generate_readme,shell=True,check=True)
    readme = open("readme.md","a")
    readme.write("This project was bootstrapped using selenium \nHelp adding more feature to this project by contributing on https://github.com/suyogsubedi/automating_repo_creation  \nCreated By: Suyog")
    add_to_git = "git add ."
    subprocess.run(add_to_git, shell=True, check=True)
    git_commit = 'git commit -m "First Commit"'
    subprocess.run(git_commit,shell=True,check=True)
    branch = "git branch -M main"
    subprocess.run(branch,shell=True,check=True)
    print("I will wait for 10 seconds before executing the next line")
    time.sleep(10)
    github_add_origin = f"git remote add origin https://github.com/{username}/{project_name}.git"
    subprocess.run(github_add_origin,shell=True,check=True)
    push_to_github = "git push -u origin main"
    subprocess.run(push_to_github,shell=True,check=True)
    # showing the page 
    PATH ="/home/suyog/Projects/git_automation/chromedriver"
    driver = webdriver.Chrome(PATH)
    time.sleep(5)
    driver.get("https://github.com/{username}/{project_name}")
    
