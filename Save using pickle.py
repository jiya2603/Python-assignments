import pickle 

list1=[1,2,3,4,5,6]
fileName = "data.pickle"

try:
    with open(fileName, "wb") as filehandle:
     pickle.dump(list1, filehandle)
     print("Object saved succesfully")
except:
    print("error while saving the object")
  