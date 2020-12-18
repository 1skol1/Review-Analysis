''' We import the necessary packages & input the sitemap address which has all the category links.
 Without using user agent header it displays Err : 403(Forbidden)'''


import requests as req
from bs4 import BeautifulSoup
import csv

url = "https://www.capterra.com/sitemap_categories.xml"
my_headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
r = req.get(url, headers = my_headers)
status = r.status_code
article = r.text
soup = BeautifulSoup(article,'html.parser')

# print status to confirm the site has been loaded
print(status)

# We search directly with the tags as the site is XML.
category_link = soup.find_all('loc')
last_modified = soup.find_all('lastmod')
change_frequency = soup.find_all('changefreq')
priority = soup.find_all('priority')

#Save it all in CSV file
with open('capterra_categories.csv', mode='w') as csv_file:
    fieldnames = ['Category Name', 'Category Link', 'Last Modified','Change Frequency', 'Priority']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for a,b,c,d in zip(category_link,last_modified,change_frequency,priority):
      lm = b.text
      cf = c.text
      p = d.text
      cat_link = a.text
      cat_name = cat_link.split('/')[3]
      cat_name = cat_name.split('-')
      name = ""
      for i in cat_name:
        name += i + " "
      writer.writerow({'Category Name': name , 'Category Link': cat_link, 'Last Modified': lm ,'Change Frequency': cf ,'Priority': p })  

