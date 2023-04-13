from os import system
from sys import exit

loc = "~/walpap/"
name = "wal.jpg"

def setwalloc(loc2):
    global loc
    loc = loc2

def setwalname(name2):
    global name
    name = name2

def setwal(type):
    optionsInWords = ["--set-auto","--set-centered","--set-scaled","--set-zoom","--set-tiled"]
    try:
        type = int(type)
        type = optionsInWords[type]
    except Exception as e:
        pass
    if system(f"nitrogen {type} {loc}/{name}") == 0:
        return 0
    else:
        return 1

def download(url):
    try:
        system(f"rm -r {loc}")
    except Exception as e:
        pass
    system(f"mkdir {loc}")
    system(f"cd {loc} && wget ./ \"{url}\" &> /dev/null")
    system(f"cd {loc} && mv ./* ./{name}")
    
def generateURLByUser(user):
    if user == "":
        exit(1)
    else:
        return f"https://source.unsplash.com/user/{user}"

def generateURLBySearch(user):
    if user == "":
        exit(1)
    else:
        return f"https://source.unsplash.com/random/?{user}"
if __name__ == "__main__":
    print("Hi, this is a Unsplash wallpaper generator program written in python.")
