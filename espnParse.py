import datetime
import requests
from bs4 import BeautifulSoup
import json

# Create dict for JSON Object
response = []
number = 10447
while number < 10492:
    print(str(number))
    # Prepare for parsing StackOverflow with BeautifulSoup
    urlNFL = 'http://www.espn.com/nfl/player/stats/_/id/' + str(number) + '/'
    page = requests.get(urlNFL)
    soup = BeautifulSoup(page.content, 'lxml')
    # Parse NFL url

    for position in soup.find_all('ul', class_='general-info'):
        pos = position.find('li', class_='first').string.strip()
        # Make changes to response for NFL

    for position in soup.find('h1'):
        name = position.string.strip()
        # Make changes to response for NFL
        response.append({'name': name, 'pos': pos})
    number = number + 1

# Write response to JSON file
postingsFile = 'URLResponseESPN.json'
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()