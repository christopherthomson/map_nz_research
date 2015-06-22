import requests
from bs4 import BeautifulSoup
import tablib
import sys

BASE_URL = 'http://ir.canterbury.ac.nz/dspace-oai/request?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:ir.canterbury.ac.nz:10092/'

def scrape_oai(id_list):
    for id in id_list:
        url = BASE_URL + str(id)
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            dc = soup.find('oai_dc:dc')
            dc_children = [child.string for child in dc.findChildren()]
            yield dc_children
        except:
            continue

if __name__ == "__main__":
    for result in scrape_oai([1,1034,1035]):
        print result
