L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
L2=[]
element=0
freq=0
for i in range(0, len(L1)):
    compteur = 1
    for j in range(i+1, len(L1)):
        if L1[i]==L1[j]:
            compteur+=1
    L2.append(compteur)
    if compteur>freq:
        freq=compteur
        element=L1[i]

print("l’élément apparaissant le plus fréquemment dans une liste est :", element)
print("avec une frequence de:x", freq)

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
