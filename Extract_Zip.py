# Importing necessary modules
import requests, time
from io import BytesIO
from pathlib import Path
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Create a data directory
Path("BIXI_Data").mkdir(parents=True, exist_ok=True)

# Find all links of Zip files on the webpage
url = "https://bixi.com/en/open-data"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
data_containter = soup.find("div", class_="container open-data-history")

# Extract all zip files from href on webpage
for link in data_containter.find_all("a", class_="document-csv col-md-2 col-sm-4 col-xs-12", href=True):
    req = requests.get(link['href']) 
    print(link.get_text(), link['href'])
    time.sleep(5)
    with  ZipFile(BytesIO(req.content), 'r') as zipObj:
        zipObj.extractall("./BIXI_Data/" + link.get_text())






