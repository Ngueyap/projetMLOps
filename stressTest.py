import requests
import time

# URL de votre endpoint de prédiction
url = "http://127.0.0.1:5000/api/anime"

# Définir le payload de la requête
payload = {
    "description": "je suis un eleve dans une classe d assassins notre objectif est de tuer notre professeur",
    "title": "assasin",
    "genre": "flying DOG,iQIYI",
    "type": "TV",
    "producer":"aucun",
    "studio": "WAO World,domerica"
}

# Définir le taux de requêtes par seconde
num_requests = 10

# Define the interval between requests in seconds
interval = 6

# Boucle pour envoyer des requêtes à un taux constant
for i in range(num_requests):
    response = requests.post(url, json=payload)
    print(f'Response {i+1}: {response.json()}')
    time.sleep(interval)



