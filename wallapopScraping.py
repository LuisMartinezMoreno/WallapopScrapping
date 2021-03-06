import time
import ast
from tkinter import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from webFunctions import *
from jsonUtils import *


##---------------------------------------------------------------------------------

"""main function"""
def scraping(article, minPrice, distance):
    numArticlesToSearch = 9
    newArticles = {}
    articleName = article
    ##driver = webdriver.Chrome('/usr/bin/chromedriver')
    ##driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'))

    chrome_options = Options()
    '''chrome_options.add_argument('--headless') 
    chrome_options.add_argument('--no-sandbox')'''
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=chrome_options)
    driver.execute_script("document.body.style.zoom='50%'")
    website = generateWallapopUrl(article, minPrice, distance)
    ##website = "https://es.wallapop.com/app/search?keywords=nintendo%20ds&filters_source=quick_filters&longitude=-3.69196&latitude=40.41956&order_by=price_low_to_high&distance=50000&min_sale_price=20"
    driver.get(website)

    
    ##closing the button "aceptar
    time.sleep(10)
    boton = driver.find_element(By.ID,'didomi-notice-agree-button')
    boton.click()
    

    ##getting a list of the items
    articles = driver.find_elements(By.CLASS_NAME,'ItemCardList__item')
    articlesCropped = articles[0:numArticlesToSearch]
    time.sleep(10)

    root = Tk()
    screenHeight = root.winfo_screenheight()
    halfScreenHeight = screenHeight/2
    firstPosition = halfScreenHeight

    ##Proceses the elements in order to get the item data
    for article in articlesCropped:
        precio = article.find_element(By.CLASS_NAME,'ItemCard__price')
        precioTexto = precio.text
        itemPosition = precio.location['y'] 
        driver.execute_script("window.scrollTo(0,arguments[0])", itemPosition-200)
        divImage = article.find_element(By.CLASS_NAME,'ItemCard__image')
        image = divImage.find_element(By.CSS_SELECTOR, "img")
        imageUrl = image.get_attribute("src")
        imageItemId = getItemId(imageUrl)

        articleDict={"id":imageItemId,
        "price":precioTexto[0:-1],
        "link":imageUrl}

        currentIndex = articlesCropped.index(article)
        newArticles[currentIndex] = articleDict

    nombreArchivo = str(articleName).replace(" ","")
    ## if there is no error, we are in an exisitng json, so we have to compare and save the info updated
    if(openResultJSON(nombreArchivo) != "error"):
        compareJSON(numArticlesToSearch,newArticles,nombreArchivo,str(articleName))
        saveJSON(nombreArchivo,newArticles,False,numArticlesToSearch)

    else:##it is a new item to look for
        saveJSON(nombreArchivo,newArticles,True,numArticlesToSearch)

    driver.close()

'''main function, where the algorithm is being triggered'''
if __name__=="__main__":
    data = openMainJSON("itemsToLookFor")
    for x in data["items"]:
        scraping(x.get("name"),x.get("minPrice"),x.get("distance"))
    print("**THE END***")

