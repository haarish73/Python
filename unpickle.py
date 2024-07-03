import pickle

with open("pickleFile.txt", 'rb') as fp:
    unpickle = pickle.load(fp)
print(unpickle)


