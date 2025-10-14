import requests

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        '''
        print(type(data))
        print(len(data))
        print(type(data[0]))
        print(data[0].keys())
        print(type(data[0]['meanings']))
        print(type((data[0]['meanings'][0])))
        print((data[0]['meanings'][0].keys()))
        '''
        meanings = data[0]['meanings'][0]['definitions'][0]['definition']
        return meanings
    else:
        return None

def main():
    print("📘 Simple Dictionary App")
    print("-------------------------")
    while True:
        word = input("Enter a word (or type 'exit to quit): ").strip().lower()
        if word == "exit":
            print("Goodbye!")
            break
        else:
            meaning = get_meaning(word)

            if meaning:
                print(f"Meaning of '{word}' : {meaning}")
            else:
                print(f"Sorry, the word '{word}' is not found.")

if __name__ == "__main__":
    main()