import requests
from translator import translate_to_hindi

def joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    responce=requests.get(url)
    data=responce.json()

    new_joke=data["data"] ["content"]
    return new_joke

def main():

    # api_joke=joke()
    # print(f" NEW joke: --> {api_joke}")

    text = joke()
    hindi_text = translate_to_hindi(text)
    print(f"English: {text}")
    print(f"Hindi: {hindi_text}")

if __name__ == '__main__':
    main()