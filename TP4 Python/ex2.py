nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0

notes = []

for i in range(nombreEtudiants):
    while True:
        try:
            note = float(input(f"Entrez la note de l'étudiant {i + 1} (entre 0 et 20) : "))
            if 0 <= note <= 20:
                notes.append(note)
                moyenne += note
                break
            else:
                print("Veuillez saisir une note valide entre 0 et 20.")
        except ValueError:
            print("Veuillez saisir un nombre valide.")


if nombreEtudiants > 0:
    moyenne /= nombreEtudiants


print(f"\nLa moyenne de classe est : {moyenne:.2f}")
for i in range(nombreEtudiants):
    print("{}| {} | {}".format(i,notes[i], round(moyenne-notes[i],2)))