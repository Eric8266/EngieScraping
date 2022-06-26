import tabula as tb
import os


class PdfParser:
    #TODO add base path as global?
    def __init__(self, file, base_path):

        self.base_path = base_path
        self.file = file
        #TODO output df?
        self.output = []
        self.state = None


    #load new file
    def load_file(self, new_file):
        self.file = new_file
        pass


    #determine if old or new format
    def determine_oldnew(self, file) -> bool:
        #TODO some logic to determine if format is old or new, maybe name is easiest?
        if 1 + 1 == 2:
            return True
        else:
            return False



    #scrape relavant data
    def scrape(self):
        
        #TODO check online how to easily convert the list to DF
        raw_list = tb.read_pdf(self.file, pages=2)


        #TODO append scraped output to either df or list
        self.output.append("something")

        pass



    #do all of the above, and return a dict with the interesting data
    def run(self) -> dict:
        
        for file in "input directory""
            load_file(file)
            determine_oldnew(file)

        