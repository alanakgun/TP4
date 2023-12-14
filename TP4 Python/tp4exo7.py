#Question 1
binome = ('login1', 'login2')
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

#Question 2
nouveau_login = input("Entrez le nouveau login : ")
binome = (binome[0], nouveau_login)
print(f"Le binôme a été mis à jour. Maintenant, l'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

#Question 3
del binome[1]

#Question 4
troisieme_login = input("Entrez le troisième login : ")
binome = binome + (troisieme_login,)
print(f"Le binôme a été mis à jour. Maintenant, les étudiants {binome[0]}, {binome[1]} et {binome[2]} sont en trinôme.")
