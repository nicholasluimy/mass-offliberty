import requests
from bs4 import BeautifulSoup
import urllib
import os

endpoint = "http://offliberty.com/off03.php"
# Your desired save location
os.chdir('XXX')
"""
input file. simple txt file with alternate lines of url and name, e.g

musicUrl.com
musicfile.mp3
secondurl.com
musicfile2.mp3
"""
with open('XXX',
          'rb') as inputfile:
    for line in inputfile:
        target = line
        name = inputfile.next().rstrip()
        payload = {'track': target,
                   'refext': endpoint}

        r = requests.post(endpoint, data=payload)
        parser = BeautifulSoup("<html>"+r.text+"</html>", "html.parser")
        treasure_spot = parser.a['href']
        getter = urllib.URLopener()
        treasure = getter.retrieve(treasure_spot, name)
        print(name)
        print(target)
