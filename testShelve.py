import shelve
sh = shelve.open("shelve1")
print(list(sh.keys()))
