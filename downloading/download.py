import random as rand
import urllib as req


class downloading:
    url = ""
    name = rand.randrange(1,1000)
    fullname = str(name) + ".jpg"

    def __init__(self, url):
        self.url = url



    def download_image(self):
        #retrieves image from url
        req.urlretrieve(self.url, self.fullname)


    def download_file(self):
        #open url
        response = req.urlopen(self.url)
        #read contents of webpage
        csv = response.read()
        #convert the data into strings
        csv_str = str(csv)
        #split the strings into readable format
        csv_lines = csv_str.split("\\n")
        #create a destination for the file
        destination = r'sample.csv'
        #open the destination and write to file
        fx = open(destination, "w")
        #foreach line of strings write to file
        for line in csv_lines:
            fx.write(line + "\n")
        #close the file writing process
        fx.close()    


        




unsplashImage = "https://images.unsplash.com/photo-1463414689943-2aca18b2242b?ixlib=rb-0.3.5&s=e27e912be672bb7e428a8b2f483979a2&auto=format&fit=crop&w=1189&q=80"
csvFile = "http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"
getImage = downloading(csvFile)
getImage.download_file()