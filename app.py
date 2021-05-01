from bs4 import BeautifulSoup
import requests
import json
from helpers import readJson, getSoup

def parseDisciplines(URL):
    soup = getSoup(URL)
    discipline_spans = soup.find_all("span", class_="label label-default")
    # disciplines = discipline_spans.find_all(text=True, recursive=False)
    disciplines = []
    for div in discipline_spans:
        disciplines.append(div.findAll(text=True)[0])
    return disciplines

def getDisciplinesPerInstitute(disciplines, institute_url):
    disciplines_payload = parseDisciplines(institute_url)
    for discipline in disciplines:
        is_found = 'disponível neste semestre'
        if discipline not in disciplines_payload:
            is_found = 'não disponível neste semestre'
        print("Disciplina %s %s" % (discipline, is_found))

def getInstitutesPerSemester(institutes, semester_url):
    for institute in institutes.keys():
        institute_url = semester_url + institute
        print("Pegando dados do/da instituto/faculdade: %s" % (institute))
        getDisciplinesPerInstitute(institutes[institute], institute_url)
        print()

def getSemestersData(config):
    for semester in config.keys():
        year = semester[:4]
        semester_index = semester[5]
        url_semester = "https://www.dac.unicamp.br/portal/caderno-de-horarios/%s/%s/S/G/" % (year,semester_index)
        print("Pegando dados do semestre: %s" % (semester))
        getInstitutesPerSemester(config[semester], url_semester)

def main():
    config = readJson('./disciplinas.json')
    getSemestersData(config)

if __name__ == "__main__":
    main()
    #parseDisciplines('https://www.dac.unicamp.br/portal/caderno-de-horarios/2021/1/S/G/IC')