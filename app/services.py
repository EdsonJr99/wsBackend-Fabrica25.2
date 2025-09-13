import requests

def buscar_livros_google(query, max_results=5):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query, "maxResults": max_results}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get("items", [])
    return []