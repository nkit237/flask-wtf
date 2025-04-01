import requests
import os

base_path = './cities'

d = {
    'москва': ['moskva_1.jpg', 'moskva_2.jpg'],
    'нью-йорк': ['new_york_1.jpg', 'new_york_2.jpg'],
    'париж': ['paris_1.jpg', 'paris_2.jpeg']
}
token = 'y0__xD6l7ieBhij9xMghL261RKHwIpVquALjJfEC7oS92FdC35O4A'
url = 'https://dialogs.yandex.net/api/v1/skills/81d28706-d89e-45db-9365-97bfa52054fe/images'
for k in d:
    ids = []
    for city in d[k]:
        file = {'file': (city, open(os.path.join(base_path, city), 'rb'))}
        response = requests.post(url, files=file, headers={'Authorization': f'OAuth {token}'})
        ids.append(response.json()['image']['id'])
    d[k] = ids

print(d)

dic = {'москва': ['1540737/f03ce2157e43a919d3ff', '1521359/bfd3c7861b801cacb0e1'],
       'нью-йорк': ['1521359/abebbc67581e5f50ae1e', '1652229/2bf3679c659b9105f751'],
       'париж': ['1652229/1ac7c7cbc0cf4657da38', '1521359/9e3062ad3d163bb715be']}
