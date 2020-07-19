from os import chdir, path
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
try :
    from facebook_scraper import get_posts
except:
    install(facebook_scraper)
    from facebook_scraper import get_posts


page_id = input('# Input Facebook Page ID, Or press Enter for "mwrifb" :')
if not len(page_id): page_id = 'mwrifb'

num_pages = input('# Input Number of Pages to get, Or press Enter for 1  :')
if not len(num_pages): num_pages = 1

print('\n# Getting',num_pages,'page(s) from http://www.facebook.com/'+page_id+'\n')

chdir(path.dirname(path.abspath(__file__)))

for post in get_posts(page_id, pages=num_pages):
    with open('FBDataDump.txt', 'a', encoding='utf8') as myfile:
        myfile.write(repr(post))
