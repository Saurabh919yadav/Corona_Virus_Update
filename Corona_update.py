import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_ = "maincounter-number")

print("In The World :")
print("Total Cases : ", data[0].text.strip())
print("Total Deaths : ", data[1].text.strip())
print("Total Recovered : ", data[2].text.strip())
print("\n")
print("<===================================================================================>")
print("\n")

url = "https://www.worldometers.info/coronavirus/country/india/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_ = "maincounter-number")

print("In India :")
print("Total Cases : ", data[0].text.strip())
print("Total Deaths : ", data[1].text.strip())
print("Total Recovered : ", data[2].text.strip())