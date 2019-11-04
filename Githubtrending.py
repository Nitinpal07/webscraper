import requests
from bs4 import BeautifulSoup

page = requests.get("https://github.com/trending")

soup = BeautifulSoup(page.text, 'html.parser')

repos = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

individual_repos = repos.find_all(class_="Box-row")

print(len(individual_repos))

for eachrepo in individual_repos:
    repo = eachrepo.find_all('a')

    name = repo[1].get('href').split('/')

    repo_stars = repo[2].find(class_='octicon octicon-star').parent.text.strip()
    print('git profile name:', name[1])
    print('git repo name:', name[2])
    print('starts on repo:', repo_stars)
    print('-----------------------------------------------------------------------------------------------------------')
