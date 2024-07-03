import shelve

sh = shelve.open("shelve1")

sh['one'] = 1
sh['Two'] = 2
sh['three'] = 3
sh.close()