import requests


def default() -> None:
    print(requests.get('http://localhost:8000/').json())


default()
