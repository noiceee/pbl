from plyer import notification
import requests
from bs4 import BeautifulSoup, Comment
import geocoder
import geopy
# from selenium import webdriver

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\\Coding\\Python\\pblProjectFE\\Notifs system\\icon.ico",
        timeout = 30
    )

def getData(url):
    r = requests.get(url)
    return r.text

soup = BeautifulSoup(getData("https://coronaclusters.in/"), 'html.parser')

# print(soup.title.get_text())

# data = soup.title.get_text().split()
# cases = data[2]
# deaths = data[5]

# print(cases)

g = geocoder.ip('me')
print(g.latlng)
geolocator = geopy.geocoders.Nominatim(user_agent = "geoapiExercises")
location = geolocator.reverse(g.latlng)
# location = geolocator.reverse(['19.0760', '72.8777'])
state = str(location).split(", ")[-3] #get's users state

for tr in soup.find_all('table')[0].find_all('tr'):
    trData = str(tr.get_text()).split()
    if trData[0] == state:
        totalCases = int(trData[1])
        casesNew = int(trData[2])
        deathsTotal = int(trData[3])
        deathsNew = int(trData[4])
        totalRecoveries = int(trData[5])
        activeCases = int(trData[6])
        lastUpdated = trData[8] + " " + trData[7]
        notifyMe(f"Covid-19 in {state}", "Cases : {:,}\nNew Cases : {:,}\nDeaths : {:,}\nNew Deaths : {:,}\nActive Cases : {:,}\
            \nLast Updated : {}".format(totalCases, casesNew, deathsTotal, deathsNew, activeCases, lastUpdated))
        break

# print(state, totalCases, casesNew, deathsTotal, totalRecoveries, activeCases, lastUpdated)








# def getData(url):
#     driver = webdriver.Firefox(executable_path=r'C:\Users\Anushka Singh\ShivaniTakuli\ShivaniTakuli\src\drivers\geckodriver.exe')
#     driver.get(url)
#     html = driver.page_source()
#     return html


# soup = BeautifulSoup(getData("https://www.mohfw.gov.in/"), 'html.parser')
# i = 0 
# stats = soup.find_all(string = lambda text : isinstance(text, Comment))[25]
# stats.extract()
# soup = BeautifulSoup(str(stats), 'html.parser')
# allData = ""
# for tr in soup.find_all('tr'):
#     allData += tr.get_text()
# allData = allData[1:].split("\n\n") #[1:] to eliminate additional next line character
# for item in allData:
#     print(item.split("\n"))
# for i in soup.find_all('table')[0].find_all():
#     print(i)