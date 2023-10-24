from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
load_dotenv()
file_path = os.getenv('paz')
print(file_path)
def extract_urls_from_mhtml(file_path):
    mhtml_file = file_path+"python - ImportError_ No module named 'MySQL' - Stack Overflow.mhtml"
    with open(mhtml_file, 'r') as file:
        mhtml_content = file.readlines()
        url = mhtml_content[1][27:]
        return url


path = "where to save url file"
url = extract_urls_from_mhtml(file_path)
encoding  ="""
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL="""+url+"""
IconIndex=13
HotKey=0
IconFile=C:\Windows\System32\SHELL32.dll
"""
with open(path+'tes.url','w') as file:
    file.write(encoding)


print(extract_urls_from_mhtml(file_path))

