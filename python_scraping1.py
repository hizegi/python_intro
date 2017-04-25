from urllib import urlopen
from bs4 import BeautifulSoup

# url = 'http://isitweekendyet.com'
# pageSource = urlopen(url).read()
#
# weekendSoup = BeautifulSoup(pageSource, 'html.parser')
# body = weekendSoup.body
# is_weekend = body.div.string.strip() == 'YES!'
# print is_weekend

# if isItWeekend.strip() == 'YES!':
#     print 'true'
# else:
#     print 'false'


#GA PROFILES EXERCISE

urlGA = 'https://gallery.generalassemb.ly'
pageSourceGA = urlopen(urlGA).read()
GASoup = BeautifulSoup(pageSourceGA, 'html.parser')
print GASoup

projects = GASoup.find_all('li', class_="projects")
projects

#Find first project in New York City
GASoup.find_all('a', href="/?metro=new-york-city")[0].parent.text.strip()

#Find all projects titles in New York City
nyc_projects = GASoup.find_all('a', href="/?metro=new-york-city")

#for project in nyc_projects:
    #print project.parent.text.strip()

#Which are all the unique locations that projects have come from?
metros = GASoup.find_all('a', class_="metro")
city_list = []
city_count_dict = {}

#Which are all the unique locations that projects have come from?
for metro in metros:
    if metro.text not in city_list:
        city_list.append(metro.text)

print city_list

#How many are from each location?
for metro in metros:
    if metro.text in city_count_dict:
        city_count_dict[metro.text] = city_count_dict[metro.text]+1
    else:
        city_count_dict[metro.text] = 1

print city_count_dict

# How many of each unique number?
# numbers = [1,3,4,5,6]
#
# number_dict = {}
# for number in numbers:
#     if number in number_dict:
#         number_dict[number] = number_dict[number]+1
#     else:
#         number_dict[number] = 1
# print number_dict


    # metro = project.text.strip()
    # unique_array = []
    # unique_array.append(metro)
    # #unique_array.reduce
    # my_set = set(unique_array)
    # print unique_array
