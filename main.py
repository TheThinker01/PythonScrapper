import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# Web Scrapper that scrapes the images from the Unsplash website
# and stores them in a new directory by the name of the search term

def scrapper():
    search = input("Enter the terms to search for ")
    search = search.lower()
    # search often need parameters in the url , use:
    params = {"q": search}
    # Enter the url you want to scrap from
    url = ""
    r = requests.get(url,params)

    # Edit query to get the appropriate website and search term
    # query = "https://unsplash.com/s/photos/"+search

    # r = requests.get(query)
    print(r.url)

    # create new directory with the search terms as name
    dir_name = search.replace(" ", "_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # create the BeautifulSoup object
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    # Change appropriately according to website
    links = soup.findAll("img", {"class": "_2zEKz"})
    print(links)
    i = 1
    for item in links:
        try:
            img_url = item['src'].split("?")[0]
            print("Getting  : ", img_url)
            img_obj = requests.get(img_url)

            title = i
            i += 1
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./"+dir_name+"/"+str(title)+".JPEG")
            except:
                print("Couldnt Save Image")

        except:
            print("Request Error")
    scrapper()


scrapper()



