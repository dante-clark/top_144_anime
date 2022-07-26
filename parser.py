from bs4 import BeautifulSoup

titles = []
scores = []
ranks = []
popularity = []
members = []


for i in range(0, 145):
    with open(f'./pages/{i}.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        scores.append(soup.find(class_='score-label').text)
        titles.append(soup.find(class_='title-name').find(name="strong").text)
        ranks.append(soup.find(class_='ranked').find(name="strong").text)
        popularity.append(soup.find(class_='popularity').find(name='strong').text)
        members.append(soup.find(class_='members').find(name='strong').text)

print(scores)
print(titles)
print(ranks)
print(popularity)
print(members)