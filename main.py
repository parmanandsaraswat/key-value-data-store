#Importing the required libraries
from threading import Thread
import json
import sys
import os
import time
from pathlib import Path
path="datastore.json"
my_file = Path(path)

def create():
    key=input("Enter key: ")
    if len(key)>32:
        print("Error: Key length exceeded! The key is capped at 32 chars.") #Checking the length of the key
        return
    if my_file.exists():     #Checking if the file exists
        if os.path.getsize(path) <= (1073741824):       #Checking the size of the file 
            temp=open(path,"r")        #Opening the file
            d = dict(json.load(temp))         #Copying the contents of json file to a dictionary
    
            if key in d:          #Checking if key already exists in the file
                print("Key already exists! Enter new key")
                return
            else:
                n=int(input("Enter no of values: "))     #Getting the number of values for each key to create a JSONobject
                print("Enter the values in the form of key-value pair")     
                temp={}
                for i in range(1,n+1):
                    s=input("Enter key"+ str(i) +" and value: ")
                    s=s.split(":")
                    temp[s[0]]=s[1]
            
                d[key]={}
                d[key].update(temp)
                time_choice=input("Specify time limit?: (y/n) ")     #Checking whether the user wants to give the time limit
                if time_choice=='y':
                    timelimit=float(input("Enter Time Limit in minutes: "))
                    seconds=time.time()+(timelimit*60)
                    d[key].update({"time":seconds})
                else:
                    d[key].update({"time":0})
                json_object = json.dumps(d)
                if sys.getsizeof(json_object)>16000:            #Checking the size of the JSON object
                    print("JSON Object value-size exceeded!")
                    return
                with open(path, "w") as outfile:
                    outfile.write(json_object)           #Updating the file.
                outfile.close()
        else:
            print("Data-Store File size exceeded 1GB!")
            return
    else:                    #If the file does not exist
        d=dict()
        if key in d:
                print("Key already exists! Enter new key")
                return
        else:
            n=int(input("Enter the no of values: "))
            print("Enter the values in the form of key-value pair  ")
            temp={}
            for i in range(1,n+1):
                s=input("Enter key "+ str(i) +" and value: ")
                s=s.split(":")
                temp[s[0]]=s[1]
            d[key]={}
            d[key].update(temp)
            time_choice=input("Specify time limit?: (y/n) ")
            if time_choice=='y':
                timelimit=float(input("Enter Time Limit in minutes:"))
                seconds=time.time()+(timelimit*60)
                d[key].append(seconds)
            else:
                d[key].append(0)
            json_object = json.dumps(d)
            if sys.getsizeof(json_object)>16000:
                print("JSON Object value size exceeded!")
                return
            with open(path, "a+") as outfile:
                outfile.write(json_object)             #Creating and updating the file.
            outfile.close()
                
                
 #Read method               
def read():
    key=input("Enter key: ")
    if my_file.exists():
        temp=open(path,"r")
        d = json.load(temp)
        if key not in d:
            print("Error: Key does not exist in file. Enter a valid key")
        else:
            value=d[key]
            if d[key]['time']==0:
                print(value)
            else:
                if time.time()<d[key]['time']:           #Checking if the time limit specified by the user has expired or not 
                    print(value)
                else:
                    print("Error: ",key," has expired")
        temp.close()
    else:
        print("Empty data-store. Please enter values to read!")
        
#Delete method                
def delete():
    key=input("Enter key: ")
    if my_file.exists():
        temp=open(path,"r")
        d = json.load(temp)
        if key not in d:
            print("Error: Key does not exist in file. Enter a valid key")
        else:
            value=d[key]
            if('time'  not in d[key].keys()):
                del d[key]
            else:
                if d[key]['time']==0:
                    del d[key]
                    print("Key ",key," is successfully deleted")
                else:
                    if time.time()<d[key]['time']:              #Checking if the time limit specified by the user has expired or not.
                        del d[key]
                        print("Key ",key," is successfully deleted")
                    else:
                        print("Error: ",key," has expired")
            with open(path, 'w') as fp:
                json.dump(d, fp)
        temp.close()
    else:
        print("Empty file. Enter values to delete!")

#Update method      
def update():
    key=input("Enter key: ")
    if my_file.exists():
        temp=open(path,"r")
        d = json.load(temp)
        if key not in d:
            print("Error: Key does not exist in file. Enter a valid key")
        else:
            if time.time()>d[key]['time'] and d[key]['time']!=0:
                print("Error: ",key," has expired")
                return
            t=d[key].copy()          #Creating a copy of the value 
    
            del d[key]                   #Deleting the current key
            n=int(input("Enter no of values: "))
            print("Enter the values in the form of key-value pair ")
            temp={}
            for i in range(1,n+1):
                s=input("Enter key "+ str(i) +" and value: ")
                s=s.split(":")
                temp[s[0]]=s[1]
                #Inserting the updated key value pair
            d[key]=(t)
            d[key].update(temp)    #Updating the value 
            json_object = json.dumps(d)
            if sys.getsizeof(json_object)>16000:
                print("JSON Object value size exceeded!")
                return
            print("Key ",key," is succesfully updated" )
            with open(path, "w") as outfile:
                outfile.write(json_object)             #Updating the file.
            outfile.close()        
    else:
        print("Empty file! Enter values to update!")
            
        




print("\n\n\n***Methods availabele: ***\n1. create()\n2. read()\n3 .delete()\n4. update()") 

while 1:
    opt=int(input("\nEnter your  operation: "))    #Getting the choice of operation 
    if opt==1:
        create()                         
    elif opt==2:
        read()
    elif opt==3:
        delete()
    elif opt==4:
        update()
    else:
        print("EXIT")
        break
    break
#we can access these using multiple threads like
t1=Thread(target=(create or read or delete)) #as per the operation
t1.start()
time.sleep(10)
t2=Thread(target=(create or read or delete)) #as per the operation
t2.start()
time.sleep(10)