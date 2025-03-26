import requests
from PIL import Image
from io import BytesIO

def api_user():
    url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response= requests.get(url)
    data= response.json()

    if data ['success']:
        api_username=data["data"] ["login"] [ "username"]
        api_pass=data["data"] ["login"] ["password"]
        api_country= data["data"] ["location"] ["country"]
        api_picture=data["data"] ["picture"] ["large"]
        return api_username, api_pass, api_country, api_picture
    
    else:
        raise Exception ("failed to featch user data")

def main():
    try:
        api_username, api_pass, api_country, api_picture = api_user()

        img_response = requests.get(api_picture)
        img = Image.open(BytesIO(img_response.content))

        print(f"user name: {api_username} | user password: {api_pass} | country:  {api_country} | picture: {api_picture} ")
        img.show()
        
    except Exception as e:
        print (str(e))
    
if __name__ == '__main__':
    main()
