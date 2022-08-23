# Importing necessary modules
import requests, time
import os, shutil
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

# Change subdirectory for Zip files of years 2014, 2015, 2016, 2017
years = [2014,2015,2016, 2017]
for year in years:
    if year == 2017: 
        source_dir = f"./BIXI_Data/Year {year}/{year}/"
        target_dir = f"./BIXI_Data/Year {year}/" 
    else: 
        source_dir = f"./BIXI_Data/Year {year}/BixiMontrealRentals{year}/"
        target_dir = f"./BIXI_Data/Year {year}/"

    file_names = os.listdir(source_dir)
        
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    os.rmdir(source_dir)

# Rename stations.csv from Year 2020 to Stations_2020.csv
os.rename('./BIXI_Data/Year 2020/stations.csv','./BIXI_Data/Year 2020/Stations_2020.csv')
os.rename('./BIXI_Data/Year 2021/2021_stations.csv','./BIXI_Data/Year 2021/Stations_2021.csv')


