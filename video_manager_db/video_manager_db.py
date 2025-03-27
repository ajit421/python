import sqlite3

conn = sqlite3.connect('youtube_video.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS video
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               url TEXT NOT NULL)
''')
conn.commit()

def list_video():
    try:
        print("\n")
        print(" * " * 100)
        cursor.execute("SELECT * FROM video")
        results = cursor.fetchall()
        if results:
            print("\nID  |  Name  |  URL")
            print("-" * 50)
            for row in results:
                video_id = row[0] if row[0] is not None else 'N/A'
                name = row[1] if row[1] is not None else 'N/A'
                url = row[2] if row[2] is not None else 'N/A'
                print(f"{str(video_id):<4}|  {str(name):<20}|  {str(url)}")
        else:
            print("\nNo videos found in database.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def add_video(name, url):
    try:
        cursor.execute("INSERT INTO video (name, url) VALUES (?, ?)", (name, url))
        conn.commit()
        print("Video added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding video: {e}")

def update_video(video_id, new_name, new_url):
    try:
        cursor.execute("UPDATE video SET name = ?, url = ? WHERE id = ?", 
                      (new_name, new_url, int(video_id)))
        if cursor.rowcount > 0:
            conn.commit()
            print("Video updated successfully!")
        else:
            print(f"No video found with ID {video_id}")
    except sqlite3.Error as e:
        print(f"Error updating video: {e}")
    except ValueError:
        print("Invalid video ID. Please enter a number.")

def search_video(name):
    try:
        cursor.execute("SELECT * FROM video WHERE name LIKE ?", ('%' + name + '%',))
        results = cursor.fetchall()
        if results:
            print("\nFound videos:")
            print("\nID  |  Name  |  URL")
            print("-" * 50)
            for row in results:
                print(f"{row[0]:<4}|  {row[1]:<20}|  {row[2]}")
        else:
            print("\nNo videos found with that name.")
    except sqlite3.Error as e:
        print(f"Error searching video: {e}")

def delete_video(video_id):
    try:
        cursor.execute("DELETE FROM video WHERE id = ?", (int(video_id),))
        if cursor.rowcount > 0:
            conn.commit()
            print("Video deleted successfully!")
        else:
            print(f"No video found with ID {video_id}")
    except sqlite3.Error as e:
        print(f"Error deleting video: {e}")
    except ValueError:
        print("Invalid video ID. Please enter a number.")

def main():
    while True:
        print("\n welcome to video manager db | choose an option: ")
        print("1. list of all youtube video: ")
        print("2. Add a new video: ")
        print("3. update a video: ")
        print("4. search a video: ")
        print ("5. Delete a video: ")
        print("6. Exit: ")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            url = input("Enter the url: ")
            add_video(name, url)
        elif choice == '3':
            video_id = input("Enter the video ID: ")
            name = input("Enter the new video name: ")
            url = input("Enter the new video url: ")
            update_video(video_id, name, url)
        elif choice == '4':
            name = input("Enter video name if you want to search: ")
            search_video(name)
        elif choice == '5':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again")

    conn.close()

if __name__ == '__main__':
    main()