from urllib.request import urlopen 

# Creating the class for website extraction 
class Scrapedata():
    def __init__(self,url):
        #initialising the url attribute 
        self.url = url
        print(f"The scraper object has been initialised with url {self.url}")
        print("We are scraping the webpage....")
        #opening the url
        page = urlopen(self.url)
        print("Scraping complete, the scraped page is printed below")
        #reading the html and decoding it
        html = page.read()
        html = html.decode("utf-8")
        #saving the html file 
        with open("scraped_page.html", "w") as file:
            file.write(html)


        print(html)



if __name__ == "__main__":
    scraperobject = Scrapedata("https://www.rottentomatoes.com/browse/movies_at_home/genres:horror?page=1") 


