def SimpleInteret(p,r,t):
    return (p*r*t)/100

p,r,t = map(int,input("Enter Principal, Rate and Time (separated by space): ").split())


si = SimpleInteret(p,r,t)
print(si)   