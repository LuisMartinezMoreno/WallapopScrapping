import json
import os
from notificationsUtils import *
from webFunctions import *


''' Opens the JSON where the items to compare are
    Parameter: filename : name of the file without extension
'''
def openMainJSON(filename):
    dir = os.path.dirname(os.path.realpath(__file__))
    fullname = os.path.join(dir+"/"+filename+".JSON")
    file = open(fullname)
    data = json.load(file)
    return data

''' Opens the JSONs where the results of the items are
    Parameter: filename : name of the file without extension
'''
def openResultJSON(fileName):
    try:
        dir = os.path.dirname(os.path.realpath(__file__))
        fullname = os.path.join(dir,"results/"+fileName+".JSON")
        file = open(fullname)
        data = json.load(file)
        return data
    except:
        return "error"

'''transforms an array to a JSON'''
def arrayToJSON(array):
    return json.dumps(array, separators=(',',':'),indent=4, sort_keys = True)

'''saves the JSON with an indicated name
    Parameters: name : name of the file without extension
                jsonFile: if it is an update of an existing json
                flag: indicating if it is a new item (true)
                limit: the ammount of items to look for
'''
def saveJSON(name,jsonFile, flag, limit):
    dir = os.path.dirname(__file__)
    fullname = os.path.join(dir,"results/"+name+".JSON")
    with open(fullname,"w") as json_file:
        json.dump(jsonFile,json_file,indent = 4)
    if flag == True: ##if there is a new item...
        resume = name +"\n"
        oldArchive = openResultJSON(name)
        for i in range(limit):
            oldPrice = oldArchive[str(i)]["price"]
            oldUrl = oldArchive[str(i)]["link"]
            oldUrl = generateItemUrl(name,getItemId(oldUrl))
            resume = resume + str(i)+" price: "+oldPrice+" url: "+oldUrl+"\n"
        sendNotification(resume) 

'''function where the old JSON and the new one is being compared in order to notify if there is a new deal'''
def compareJSON(limit, newJSON, nameArchive, articleName):
    resume = ""
    flag = False
    solution = "--"+articleName+"\n"
    oldArchive = openResultJSON(nameArchive)
    for i in range(limit):
        if solution != "":
            newObject = newJSON[i]
            oldPrice = oldArchive[str(i)]["price"]
            oldId = oldArchive[str(i)]["id"]
            newPrice = newObject["price"]
            newId = newObject["id"]
            newUrl = newObject["link"]
            resume = resume + str(i)+" price: "+newPrice+" url: "+newUrl+"\n"
            if newId == oldId:
                if int(float(newPrice)) < int(float(oldPrice)):
                    flag = True
                    solution = solution + "se ha rebajado el producto "+ str(i+1)+"\n"
            else:
                if int(float(newPrice)) < int(float(oldPrice)):
                    flag = True
                    solution = solution +  "nuevo producto " + str(i+1) + "con precio mas bajo que el anterior"+"\n"
                if int(float(newPrice)) == int(float(oldPrice)):
                    flag = True
                    solution = solution +  "nuevo producto "+str(i+1)+" con el mismo precio"+"\n"
                if int(float(newPrice)) > int(float(oldPrice)):
                    flag = True
                    solution = solution +  "se ha añadido un nuevo producto "+str(i)+"mas caro..."+"\n"
        solution = solution +  "\n"
    if flag == True:##if there is a new deal we send a notification
        solution = solution+"\n"+resume
        sendNotification(solution) 
      

