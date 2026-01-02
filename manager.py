import sqlite3 
import os

con=sqlite3.connect("youtube_videos.db")
print("connection runing")
cursor=con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL)''')
    
def list_all_videos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------------------------")
    print(f" index : video name   - time")
    res=cursor.execute(''' SELECT * FROM videos''')
    for row in res.fetchall():
        print(f"({row[0]}) :  {row[1]} - {row[2]}")
    print("---------------------------------------------")

def add_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_all_videos()
    name=input("Enter video Name: ")
    time=input("Enter video time: ")
    cursor.execute("INSERT INTO videos (name,time) VALUES(?,?)",(name,time))
    con.commit()
        
def update_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_all_videos()
    index=int(input("Enter Video number to update: "))
    new_name=input("Enter the Updated video name :")
    new_time=input("Enter the Updated video time :")
    cursor.execute("UPDATE videos SET name= ? ,time=? WHERE id=?",(new_name,new_time,index))
    con.commit()
    
def delete_video():
    pass

def save_data(videos):
    pass

def con_close():
    print("connection close")
    con.close()