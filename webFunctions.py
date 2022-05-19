"""This function gives the product url, change the coordinates in order to get products close to you"""
def generateWallapopUrl(article, minPrice, distance):
    resultUrl = "https://es.wallapop.com/app/search?keywords="
    articleFixed = article.replace(" ","%20")
    resultUrl = resultUrl + articleFixed + "&filters_source=quick_filters&longitude=-3.69196&latitude=40.41956&order_by=price_low_to_high&distance="+str(distance)+"&min_sale_price="+str(minPrice)
    return resultUrl

"""Here we generate the url product of wallapop"""
def generateItemUrl(article, imageItemId):
    articleUrlAble = str(article).replace(" ","-")
    result = "https://es.wallapop.com/item/"+articleUrlAble+"-"+imageItemId
    print("RESULT:  "+result)
    return result

"""Auxiliary method to give the itemId for getting the url"""
def getItemId(imageUrl):
    text = imageUrl
    croppedLeft = text.split("c10420p")
    croppedRight = croppedLeft[1].split("/")
    cropped = croppedRight[0]
    return cropped