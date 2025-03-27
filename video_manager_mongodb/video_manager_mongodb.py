import pymongo
from bson import ObjectId

client= pymongo.MongoClient("mongodb+srv://421mrdark:421mrdark@cluster0.ntp5h.mongodb.net/", tlsAllowInvalidCertificates=True)

db= client["ytmanager"]
video_collection= db["videos"]

def list_video():
    for video in video_collection.find():
        print(f"id: {str(video['_id'])} | name: {video['name']} | url: {video['url']}")
        

def add_video(name, url):
    video_collection.insert_one({"name": name, "url": url})

def update_video(video_id, name, url):
    try:
        video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": name, "url": url}})
    except Exception as e:
        print(f"Error updating video: {e}")

def search_video(name):
    for video in video_collection.find({"name": {"$regex": name, "$options": "i"}}):
        print(f"id: {str(video['_id'])}, name: {video['name']}, url: {video['url']}")
        
def delete_video(video_id):
    try:
        video_collection.delete_one({"_id": ObjectId(video_id)})
    except Exception as e:
        print(f"Error deleting video: {e}")


def exit_video():
    print("Exiting...")
    exit()

def main():

    while True:

        print("Welcome to youtube manager | choose your option")
        print("1. list fo all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. search a video")
        print("5. delete a video")
        print("6. Exit")

        choice = input("Enter your option: ")

        if choice == '1':
            list_video()

        elif choice == '2':
            name=input("Enter your video name: ")
            url=input("Enter your url: ")
            add_video(name, url)

        elif choice == '3':
            video_id=input("Enter a video id: ")
            name=input("Enter updated video name: ")
            url= input("Enter a updated url: ")
            update_video(video_id, name, url)

        elif choice =='4':
            name=input("Enter updated video name: ")
            search_video(name)

        elif choice =='5':
            video_id=input("Enter a video id: ")
            delete_video(video_id)
        elif choice== '6':
            exit_video()

        else:
            print("Enter a valid choice.")

if __name__ == '__main__':
    main()