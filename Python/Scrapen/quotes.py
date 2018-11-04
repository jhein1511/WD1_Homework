from BeautifulSoup import BeautifulSoup as BS
from urllib2 import urlopen
import random


marriage_csv = open("marriage_quotes.csv", "w")

url = 'http://quotes.yourdictionary.com/theme/marriage/'
html = urlopen(url).read()
soup = BS(html)

all_marriage_quotes = soup.findAll("p", attrs={"class": "quoteContent"})

five_marriage_quotes = random.sample(all_marriage_quotes, 5)


for quote in five_marriage_quotes:
    print(quote.text)
    marriage_csv.write(quote.text+"\n")

marriage_csv.close()



