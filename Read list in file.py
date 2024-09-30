filepath = "List.txt"
data = [1,2,3,4]

with open(filepath,"w") as filehandle:
    filehandle.write(str(data))

with open(filepath,"r") as filehandle:
    readData = filehandle.read()
    print(f"data read is {readData} \n Its type is { type(readData)} and \nleangth is {len(readData)} ")
    tempvar =  readData [1:len(readData)-1].replace(" ",'')
    print(tempvar)
    listPlaceholder =   tempvar.split(",")
    recoveredList =  listPlaceholder
    print(f"Recovered list is {recoveredList}\n Its type is {type(recoveredList)}")