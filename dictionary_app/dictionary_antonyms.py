import requests
def get_antonym(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
       data = response.json()
        

    print(data[0]['meanings'][0]['definitions'][0])
get_antonym('hot')