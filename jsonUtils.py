import json
import os
from types import SimpleNamespace
from unittest import result
from notificationsUtils import *

def openMainJSON(filename):
    dir = os.path.dirname(os.path.realpath(__file__))
    fullname = os.path.join(dir+"/"+filename+".JSON")
    fullname = "/home/pi/Desktop/WallapopScrapping-1/itemsToLookFor.JSON"
    file = open(fullname)
    data = json.load(file)
    return data

def openResultJSON(fileName):
    try:
        dir = os.path.dirname(os.path.realpath(__file__))
        fullname = os.path.join(dir,"results/"+fileName+".JSON")
        file = open(fullname)
        data = json.load(file)
        return data
    except:
        return "error"

def arrayToJSON(array):
    return json.dumps(array, separators=(',',':'),indent=4, sort_keys = True)

def saveJSON(name,jsonFile):
    dir = os.path.dirname(__file__)
    fullname = os.path.join(dir,"results/"+name+".JSON")
    with open(fullname,"w") as json_file:
        json.dump(jsonFile,json_file,indent = 4)

def compareJSON(limit, newJSON, nameArchive, articleName):
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
            if newId == oldId:
                if newPrice<oldPrice:
                    flag = True
                    solution = solution + "se ha rebajado el producto "+ str(i+1)+"\n"
            else:
                if newPrice < oldPrice:
                    flag = True
                    solution = solution +  "nuevo producto " + str(i+1) + "con precio mas bajo que el anterior"+"\n"
                if newPrice == oldPrice:
                    flag = True
                    solution = solution +  "nuevo producto "+str(i+1)+" con el mismo precio"+"\n"
                if newPrice > oldPrice:
                    flag = True
                    solution = solution +  "se ha añadido un nuevo producto "+str(i)+"mas caro..."+"\n"
        solution = solution +  "\n"
    if flag == True:
        sendNotification(solution) ##aqui se metería la notificacion
      

