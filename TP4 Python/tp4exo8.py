dic={}
dic['firstname']='Alan'
dic['name']='AKGÜN'
dic['PROMO']='2023'
dic['group']='RT121'
print("votre nom est",dic['name']," prénom est",dic['firstname'],"vous faites partie de la promo",dic['PROMO'],"et votre groupe est",dic['group'])
print("Question 6--------------------------------------------------------------------- :")
print("les cles du dictionnaires sont:")
for i in dic.keys():
  print(f"-{i}")
print("les valeurs du dictionnaires sont:")
for j in dic.values():
  print(f"-{j}")
print("les valeurs du dictionnaires sont:")
for k in dic.items():
  print(f"-{k}")

