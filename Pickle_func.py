import pickle

new_data = {"Name":"Jiya", "Age":22}

#file = "data.pickle"
try:
 def save_object(obj, filename):
    """Serialize an object and save it to a file."""
    with open(filename, 'wb') as file:  # Open file for writing in binary mode
        pickle.dump(obj, file)  # Serialize the object and save it
        print("OBJECTS SAVED SUCCESFULLY")
except:
    print("Error in the function")


save_object(new_data, 'data.pickle')
    