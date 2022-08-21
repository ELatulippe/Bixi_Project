# importing necessary modules
import requests, time
from io import BytesIO
from pathlib import Path
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Create a data directory
Path("BIXI_Data").mkdir(parents=True, exist_ok=True)


# Extract all  
url = "https://bixi.com/en/open-data"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
data_containter = soup.find("div", class_="container open-data-history")

url_links = []
for link in data_containter.find_all("a", class_="document-csv col-md-2 col-sm-4 col-xs-12", href=True):
    url_links.append((link.get_text(), link['href']))
    
# Download all zip files and content
for i, _ in enumerate(url_links):
    link = url_links[i][1]
    print(link)
    req = requests.get(link) 
    time.sleep(5)
    with  ZipFile(BytesIO(req.content), 'r') as zipObj:
        zipObj.extractall("./BIXI_Data/" + url_links[i][0])







