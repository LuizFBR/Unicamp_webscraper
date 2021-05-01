from bs4 import BeautifulSoup
import requests
import json

def readJson(json_path):
    with open(json_path) as json_file:
        return json.load(json_file)

def getURLContents(URL):
    content = ""
    try:
        content = requests.get(URL)
    except:
        print("Falha na requisição da URL")
    return content

def getSoup(URL):
    r = getURLContents(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup