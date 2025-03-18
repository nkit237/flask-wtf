from datetime import datetime

from requests import get, post, delete

print(get('http://localhost:8080/api/jobs').json())

print(get('http://localhost:8080/api/jobs/1').json())
print(get('http://localhost:8080/api/jobs/1000').json())
print(get('http://localhost:8080/api/jobs/fdfgdfgfd').json())

print(post('http://localhost:8080/api/jobs', json={}).json())

print(post('http://localhost:8080/api/jobs', json=dict(
        job='Неполная работа',
)).json())

print(post('http://localhost:8080/api/jobs', json=dict(
        team_leader=1,
        job='Название работы',
        work_size=5,
        collaborators='3',
        start_date=str(datetime.now().date()),
)).json())

print(delete('http://localhost:8080/api/jobs/999').json())
print(delete('http://localhost:8080/api/jobs/1').json())