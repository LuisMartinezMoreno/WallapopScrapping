import json
import os
from types import SimpleNamespace

def openMainJSON(filename):
    try:
        fullname = filename + ".JSON"
        file = open(fullname)
        data = json.load(file)
        return data
    except:
        return "error"

def openResultJSON(fileName):
    try:
        dir = os.path.dirname(__file__)
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
        
