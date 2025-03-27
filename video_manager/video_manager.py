import json

def save_data_helper(videos):
    try:
        file_path = "output.json"
        with open('file_path', 'w') as file:
            json.dump(videos, file, indent=2)
    except IOError as e:
        print(f"Error saving data: {e}")
        return False
    return True

def load_data():
    try:
        file_path = "output.json"
        with open('file_path', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
        return []
    except IOError as e:
        print(f"Error reading file: {e}")
        return []

# Function to list all the videos
def list_All_Video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} {video['name']}, {video['url']}")
    print("\n") # to separate the videos
    print("Total number of videos: ", len(videos))
    print("*" * 100) # to separate the videos

# Function to add a video
def add_video(videos):
    name = input("Enter the name of the video: ")
    url = input("Enter the url of the video: ")
    videos.append({'name': name, 'url': url })
    save_data_helper(videos)

# Function to update a video
def update_video(videos):
    list_All_Video(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the name of the video: ")
        url = input("Enter the url of the video: ")
        videos[index-1] = {'name': name, 'url': url}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

# Function to search a video
def search_video(videos):
    search = input("Enter the name of the video you want to search: ")
    found = False
    for index, video in enumerate(videos, start=1):
        if search.lower() in video['name'].lower():
            print(f"{index} {video['name']}, {video['url']}")
            found = True
    if not found:
        print("Video not found")

# Function to delete a video
def delete_video(videos):
    list_All_Video(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")

# Function to exit the video manager
def exit_video_manager():
    print("Exiting the Youtube Manager")
    exit()

# Main function to run the program
def main():
    videos = load_data()
    while True:
        print("\n Welcome to Youtube video Manager | choose an option: ")
        print("1. list of all youtube video: ")
        print("2. Add a video: ")
        print ("3. update a video: ")
        print("4. search a video: ")
        print("5. Delete a video: ")
        print("6. Exit: ")

        choice = input("Enter an option: ")
        # based on the choice, call the respective function

        if choice == '1':
            list_All_Video(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            search_video(videos)
        elif choice == '5':
            delete_video(videos)
        elif choice == '6':
            exit_video_manager()
        else:
            print("Invalid option, please try again")

if __name__ == '__main__':
    main()

