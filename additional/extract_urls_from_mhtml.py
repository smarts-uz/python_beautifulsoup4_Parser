from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv('paz')
print(file_path)
# def extract_urls_from_mhtml(file_path):
#     with open(file_path, 'r') as file:
#         mhtml_content = file.read()
#
#     soup = BeautifulSoup(mhtml_content, 'lxml')
#     urls = [a['href'] for a in soup.find_all('a', href=True)]
#
#     return urls
#
# # Replace 'your_file.mhtml' with the actual file path
# mhtml_file = file_path+'Python open() Function.mhtml'
# urls = extract_urls_from_mhtml(mhtml_file)
#
# for url in urls:
#     print(url)
def extract_urls_from_mhtml(file_path):
    mhtml_file = file_path+'how many files in folder python script - Search.mhtml'
    with open(mhtml_file, 'r') as file:
        mhtml_content = file.readlines()
        url = mhtml_content[1][27:]
        return url

print(extract_urls_from_mhtml(file_path))
