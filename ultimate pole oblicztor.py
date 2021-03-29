import time

def pole_rownoleglobok(a,h):
    return a*h

def pole_romb(e,f):
    return (e*f)/2

def pole_trojkat(a,h):
    return (a*h)/2

def pole_trapez(a,b,h):
    return ((a+b)*h)/2

print("Ultimate pole obliczator")
print("     ")
print("Czego pole chcesz obliczyć?")
co=input("r=równoległobok , ro=romb , t=trójkąt , tr=trapez ")

if co=="r":
    ar=float(input("Podaj podstawę: "))
    hr=float(input("Podaj wysokość: "))  
    print("Pole równoległoboku wynosi: ")
    print(pole_rownoleglobok(ar,hr))   
    x=input("Wciśnij Enter aby wyjść")
elif co=="ro":
    er=float(input("Podaj pierwszą przekątną: "))
    fr=float(input("Podaj drugą przekątną: "))
    print("Pole rombu wynosi: ")
    print(pole_romb(er,fr))
    x=input("Wciśnij Enter aby wyjść")
elif co=="t":
    ar=float(input("Podaj podstawę: "))
    hr=float(input("Podaj wysokość: "))
    print("Pole trójkąta wynosi: ")
    print(pole_trojkat(ar,hr))
    x=input("Wciśnij Enter aby wyjść")
elif co=="tr":
    ar=float(input("Podaj pierwszą podstawę: "))
    br=float(input("Podaj druga podstawę: "))
    hr=float(input("Podaj wysokość: "))
    print("Pole trapezu wynosi: ")
    print(pole_trapez(ar,br,hr))
    x=input("Wciśnij Enter aby wyjść")