import steamapi
steamapi.core.APIConnection(api_key="Enter the api key from steam here in string format", validate_key=True)

steamids=[]
steamusernames = []

userinput = "data"
while userinput != "":
    userinput = input("Enter steamid: ")
    if userinput == "":
        userinput = input("Enter steam64id: ")
        if userinput == "":
            break
        temp = steamapi.user.SteamUser(userinput)
    else:
        temp = steamapi.user.SteamUser(userurl=userinput)
        
    steamids.append(temp)
    userinput = input("Enter username: ")
    steamusernames.append(userinput)

for id in range(0,len(steamids)):
    print("---------------------------------------")
    print("Gathering friends for " + str(steamids[id]))
    player = steamids[id].friends
    for ids in steamusernames:
        for x in player:
            x = str(x)
            if x == ids:
                print (steamids[id]  , "is friends with" , x)

