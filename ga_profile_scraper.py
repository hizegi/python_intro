#lets us grab HTML + XML
from bs4 import BeautifulSoup
# let's us open url pages
from urllib import urlopen

# First Step: declare the url
url = 'https://gallery.generalassemb.ly'
page_source = urlopen(url).read()
# soup object
soup = BeautifulSoup(page_source, "html.parser")

# Find the first project in New York City
nyc_project = soup.find_all('a', href="/?metro=new-york-city")
# print nyc_project[0].parent.text

all_nyc_project = soup.find_all('a', href="/?metro=new-york-city")

metros = soup.find_all('a', class_="metro")
# print metros

#Which are all the UNIQUE locations
city_list = []
for metro in metros:
    if metro.text not in city_list:
        city_list.append(metro.text)

# print city_list

#How many are from each location?

city_count_dict = {}

for metro in metros:
    if metro.text in city_count_dict:
        city_count_dict[metro.text] = city_count_dict[metro.text] + 1
    else:
        city_count_dict[metro.text] = 1

print city_count_dict
