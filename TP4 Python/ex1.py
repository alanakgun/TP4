tab=[]
m = float(input("Valeur de nombre:"))
for i in range(0, 10):
    tab.append(round(m*i,2))


for i in range(len(tab)):
    print("{}*{}={}".format(m,i,tab[i]))
