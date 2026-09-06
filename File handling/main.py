from pathlib import Path
import os


def createfile():
    try:
        name=input("please Enter your filename:- ")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data=input("Enter your fileData:- ")
                fs.write(data)
            print("File created Successfully") 
        else:
            print("file with this name already exists")           
    except Exception as err:
        print(f"an error occurr  {err} ")  
              
def readfile():
     try:
            name=input("please Enter your filename:- ")
            path=Path(name)
            if path.exists():
                with open(path,"r") as fs:
                    data= fs.read(data)
                print(data) 
            else:
                print("file with this name not  exists")           
     except Exception as err:
            print(f"an error occurr  {err} ")  
            
def upadatefile():
    pass
def deletefile():
    pass



print("press 1 for creating file")
print("press 2 for Read a file")
print("press 3 for update file")
print("press 4 for delete file")


a = int(input("\n tell your action :- "))


if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    upadatefile()
if a==4:
    deletefile()