from user_details import user_details
# importing necessary selenium things
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



def create_repository():
    username,password,project_name = user_details()

    PATH ="/home/suyog/Projects/git_automation/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://github.com/login")
    
    username_field = driver.find_element(By.ID,"login_field")
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID,"password")
    password_field.send_keys(password)
    # Sending the username and password for validation
    username_field.send_keys(Keys.RETURN)
    # Navigating to the page where i can create new repo
    driver.get("https://github.com/new")

    # Now, I will fill the field where i will enter the project name
    new_repo_name = driver.find_element(By.ID,"repository_name")
    new_repo_name.send_keys(project_name)
    time.sleep(5)
    # Click on the create repo
    create_repo_xpath = '//*[@id="new_repository"]/div[4]/button'
    driver.find_element(By.XPATH, create_repo_xpath).click()
    # Returning the projectname
    # To access the project name from other function 
    create_repository.this_project_name = project_name   
    create_repository.this_username = username
print("-----------------------------------------------")
create_repository()

