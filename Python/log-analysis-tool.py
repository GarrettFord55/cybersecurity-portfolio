#Part 1
def uniqueMessages():
    try:
        myList = []
        with open("/home/ec2-user/environment/Applog.txt","r") as myMessages:
            for line in myMessages:
                message = line.strip().split("-")[2]
                if message in myList:
                    continue
                else:
                    myList.append(message)
        for item in myList:
                print(item) 
    except:
        with open("/home/ec2-user/environment/finalProjExceptions.txt","a") as error:
            error.write("An error occured when displaying unique messages."+ "\n")

#Part 2
def uniqueIP():
    try:
        with open("/home/ec2-user/environment/Applog.txt","r") as myMessages:
            countList = []
            userOctet = input("Enter an ip address octet value: ")
            for line in myMessages:
                ipAddress = line.strip().split("-")[1]
                firstOctet = ipAddress.strip().split('.')[0]
                lastOctet = ipAddress.strip().split('.')[3]
                if firstOctet == userOctet or lastOctet == userOctet:
                    if ipAddress in countList:
                        continue
                    else:
                        countList.append(ipAddress)
            print("The total number of unique IP addresses listed is in the file is " + str(len(countList)))
            print("The unique IP addresses are:")
            for item in countList:
                print(item)
    except:
        with open("/home/ec2-user/environment/finalProjExceptions.txt","a") as error:
            error.write("An error occured when displaying the ip addresses."+ "\n")

#Part 3
def numberNodes():
    try:
        with open("/home/ec2-user/environment/Applog.txt","r") as myMessages:
            myDic = {}
            for line in myMessages:
                node = line.strip().split("-")[0]
                if node in myDic:
                    myDic[node] += 1
                else:
                    myDic[node] = 1
            for key, value in sorted(myDic.items()):
                print(key, value)
    except:
        with open("/home/ec2-user/environment/finalProjExceptions.txt","a") as error:
            error.write("An error occured when displaying the number of nodes."+ "\n")
while True:
    print("\n===== MENU =====")
    print("1. Extract Unique Messages")
    print("2. Find Unique IPs by Octet")
    print("3. Count Node Occurrences")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        uniqueMessages()
    elif choice == "2":
        uniqueIP()
    elif choice == "3":
        numberNodes()
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
