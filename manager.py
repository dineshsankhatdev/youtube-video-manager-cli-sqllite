import sqlite3 
import os

con=sqlite3.connect("youtube_videos.db")
print("connection runing")
cursor=con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL)''')


def load_data():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------------------------")
    print(f" index : video name   - time")
    res=cursor.execute(''' SELECT * FROM videos''')
    for row in res.fetchall():
        print(f"({row[0]}) :  {row[1]} - {row[2]}")
    print("---------------------------------------------")
    
videos=load_data()

def list_all_videos():
    pass

def add_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_all_videos()
    name=input("Enter video Name: ")
    time=input("Enter video time: ")
    cursor.execute("INSERT INTO videos (name,time) VALUES(?,?)",(name,time))
    con.commit()
    
        
def update_video():
    pass
    
def delete_video():
    pass

def save_data(videos):
    pass

def con_close():
    print("connection close")
    con.close()