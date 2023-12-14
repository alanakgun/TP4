#Question 1
def tri_bulles(liste):
    n = len(liste)

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                print(liste)

ma_liste = [5, 2, 4, 8, 1, 3]

print(ma_liste)

tri_bulles(ma_liste)






#Question 2
tab = [5, 2, 4, 8, 1, 3]
tab_trie = sorted(tab)

print("Liste originale:", tab)
print("Liste triée:", tab_trie)

#Question 3
tab = [5, 2, 4, 8, 1, 3]
tab.sort()

print("Liste triée avec tab.sort():", tab)

