import requests
from bs4 import BeautifulSoup

class Plan:
    def __init__(self, grade="", urltoday="https://adolf-reichwein-schule.de/fileadmin/home/nichtImMenue/vertretungsplan/schueler/heute/subst_001.htm", urltomorrow="https://adolf-reichwein-schule.de/fileadmin/home/nichtImMenue/vertretungsplan/schueler/morgen/subst_001.htm"):
        self.__CLASS = grade
        self.__URLTODAY = urltoday
        self.__URLTOMORROW = urltomorrow
        self.__FORMAT_IN = ["day", "date", "hour", "room", "type", "class", "teacher", "ver_teacher", "task"]

    def getToday(self):
        DATA = []
        website = requests.get(self.__URLTODAY)
        bs = BeautifulSoup(website.content, 'html.parser')

        raw_list = bs.find_all('td', class_='list')

        matching = [s for s in raw_list if self.__CLASS in str(s)]
        if len(matching) > 0:
            matching = matching[0]
        else:
            return [["Error: Class not found!"]]
        index_start = raw_list.index(matching)
        raw_list.pop(index_start)
        obj = raw_list[index_start]
        while not "inline_header" in str(obj):
            new_list = []
            for i in range(len(self.__FORMAT_IN)):
                new_list.append(raw_list[index_start].text)
                raw_list.pop(index_start)
            DATA.append(new_list)
            obj = raw_list[index_start]

        return DATA
    def getTomorrow(self):
        DATA = []
        website = requests.get(self.__URLTOMORROW)
        bs = BeautifulSoup(website.content, 'html.parser')

        raw_list = bs.find_all('td', class_='list')

        matching = [s for s in raw_list if self.__CLASS in str(s)]
        if len(matching) > 0:
            matching = matching[0]
        else:
            return [["Error: Class not found!"]]
        index_start = raw_list.index(matching)
        raw_list.pop(index_start)
        obj = raw_list[index_start]
        while not "inline_header" in str(obj):
            new_list = []
            for i in range(len(self.__FORMAT_IN)):
                new_list.append(raw_list[index_start].text)
                raw_list.pop(index_start)
            DATA.append(new_list)
            obj = raw_list[index_start]

        return DATA