import requests

print(
    requests.post(
        "http://0.0.0.0:8080",
        json={
            "query": "what is meta's new product?"
        }
    ).json()
)