import json
import os

def mkdir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
mkdir("temp")

if os.path.isfile("score.json"):
    with open("score.json","r") as f:
        score=json.load(f)
else:
    print("Error: can't load score matrix in score.json")
    exit(0)


with open("temp/score.txt","w") as f:
    n=len(score["chars"])
    f.write(str(n)+'\n')
    for c in score["chars"]:
        f.write(str(c)+' ')
    f.write('\n')
    for l in score["matrix"]:
        for i in l:
            f.write(str(i)+' ')
        f.write('\n')
    f.write(str(score["gap"])+'\n')
    f.write(str(score["extension"]))