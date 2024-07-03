try :
    a=int(input("enter the value of a"))
    b=int(input("enter the value/ of b"))
    c=a/b
    print("value of c:",a+b)

    x = [1,2,3,4]
    print(x[6])



except NameError:
    print("b value not mentioned")
except ZeroDivisionError:
    print("Arithmetic exceptions")
except IndexError:
    print("Array index ou of bounds")
except KeyError:
    print("key error")
except ValueError:
    print("value error")




