from bs4 import BeautifulSoup
from urllib import urlopen
import matplotlib.pyplot as plt
URL = "http://www.accuweather.com/en/us/new-york-ny/10007/month/349727?monyr=9/01/2016"
source = urlopen(URL).read()
weather_soup = BeautifulSoup(source)
temp_spans = weather_soup.select(".small-temp")
temperatures = []
for temp_span in temp_spans:
    temperatures.append(temp_span.text[1:-1])
print temperatures


x = range(1, len(temperatures) + 1)
plt.plot(x,temperatures)
plt.show()
# from urllib import urlopen
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
#
# url = "http://www.accuweather.com/en/us/new-york-ny/10007/month/349727?monyr=9/01/2016"
# weather_source = urlopen(url).read()
# weather_soup = BeautifulSoup(weather_source)
# temp_spans = weather_soup.select(".small-temp")
#
# temperatures = []
# for temp_span in temp_spans:
#     temperatures.append(temp_span.text[1:-1])
# print temperatures
#
# #Clean up string, remove first and last character
# # for temp in temp_spans:
# #     temp = temp.text[1:-1]
# #     int(temp)
# #     print temp
#
#
# x = range(1, len(temperatures) + 1)
# plt.plot(x,temperatures)
