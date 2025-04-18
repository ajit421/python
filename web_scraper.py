import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/pulse/top-10-simple-python-projects-beginners-source-code-priyanka-yadav-0gp2c/?trackingId=kT57qqynQJmShDwygm4RzQ%3D%3D'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for heading in soup.find_all('h1'):
    print(heading.text)
