
from selenium import webdriver
from modules.helpers import *
import time



class Scraper:

    def __init__(self, driver, base_path, credentials):
        
        self.base_path = base_path
        self.username = credentials['username']
        self.password = credentials['password']
        self.driver = driver


    def wait_pageload(self):
        #TODO build pageload function
        #somehow assert that all assets on the page have loaded
        time.sleep(3)


    def login(self, ):

        self.driver.get(get_url("login"))
        wait_pageload()
        self.driver.find_element_by_xpath(get_xpath("username")).send_keys(self.username)
        self.driver.find_element_by_xpath(get_xpath("password")).send_keys(self.password)
        self.driver.find_element_by_xpath(get_xpath("login_btn")).click()

    

    def download_files(self):

        download_links = []

        #assert that the page has loaded
        #TODO clean this up, right now it works by stopping when it detects an error.. better to detect total number of list elements beforehand
        wait_pageload()
        for outer in range(2,18,2):
            try:
                #range 1-12 for the months in the year
                for inner in range(1,13):
                    try:
                        #TODO get the link from this element somehow
                        self.driver.find_element_by_xpath(construct_list_xpath(outer,inner))
                        #TODO add the actual URL
                        download_links.append("url")
                    except notfounderror:
                        #TODO what is the name of the error where path is not found
                        continue

            except notfounderror:
                continue
                        
        for link in download_links:
            #download links to a certain folder, wget or something?
            print("downloading files")
            #assert that the file has been downloaded and then log positive result




    