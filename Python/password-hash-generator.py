#Part 1
import hashlib
password = input("Please enter your password: ")
password = password.encode("utf-8")
myHash = hashlib.md5(password)
hashValue = myHash.hexdigest()
with open("/home/ec2-user/environment/passHash.txt","w") as passHash:
    passHash.write(hashValue +"\n")



#Part 2
aboutMyMacDictionary = {"Model":"Macbook pro","Processor":"2.4 GHz 9-core", "Memory":"16 GB"}
try:
    with open("/home/ec2-user/environment/aboutmymac.txt","w") as dicFile:
        for key, value in aboutMyMacDictionary.items():
            dicFile.write(key + " : "+ value + "\n")
except:
    print("Error")



#Part 3
dicFromFile = {}
try:
    with open("/home/ec2-user/environment/aboutmymac.txt","r") as myMac:
        for line in myMac:
            #Had to look up on brave how to get rid of the \n when printing the dictionary back to the screen
            #Brave gave me an AI response from multiple sources and suggested the strip method
            #Strip removes the blank spaces before and after a string along with any \n's
            key, value = line.strip().split(" : ")
            dicFromFile[key] = value
    print(dicFromFile)
except:
    print("Error")
