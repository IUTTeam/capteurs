import requests
lala = requests.get("https://service.frfr.duckdns.org/request_data?type=temperature&temponDebut=0&temponFin=1000000000000")
print(lala.text)