import os

from modules.driver import initialize_driver
from modules.scraper import Scraper
from modules.credentials import get_credentials



if __name__ == "__main__":

    #TODO add logging
    #TODO create a venv
    #TODO github BUT DONT HARDCODE CREDENTIALS!!
    #TODO get upgraded webdriver (for chrome 103)

    #start webdriver
    base_path = os.getcwd()

    driver = initialize_driver(base_path)
    driver.get('www.google.com')
    
    # scraper = Scraper(driver, base_path, get_credentials())
    # scraper.login()
    # scraper.download_files()



    parser = Parser(base_path)
    parser.run()

    #at this point you can call parser.output() toget the raw output
    # we also define a method that exports the data to excel/csv
    
    print(parser.output())
    parser.export_to_excel()



