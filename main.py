import httpx

# Definindo a URL para a requisição GET
url = "https://webhook.site/2649f6a6-303f-41e1-8444-1a6cbc9851fc"

# Fazendo a requisição GET
response = httpx.get(url)

# Verificando o status da resposta
if response.status_code == 200:
    # Processando os dados, caso a requisição tenha sido bem-sucedida
    print("Resposta recebida com sucesso!")
    print(response.text)  # Supondo que a resposta seja em formato JSON
else:
    print(f"Falha na requisição. Status code: {response.status_code}")
