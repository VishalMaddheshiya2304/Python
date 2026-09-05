file=open("hello.txt","w")
data=input("whatever you want to write :-  ")

file.write(data)
file.close()

file2=open("hello.txt","r")
print(file2.read())
file2.close()

file = open("hello.txt","a")
data=input("append new data ")
file.write(data)