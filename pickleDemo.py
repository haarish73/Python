import pickle

fp = open('pickleFile.txt', 'wb')
cn = ["dhoni", "virat", "siraj"]
pickle.dump(cn, fp)
fp.close()
