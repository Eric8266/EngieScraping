from selenium import webdriver
import os


def initialize_driver(base_path) -> webdriver:
    
    
    #TODO add options like headless mode and other stuff
    driver = webdriver.Chrome(executable_path=base_path + "\\src\\dependencies\\chromedriver.exe")

    return driver







