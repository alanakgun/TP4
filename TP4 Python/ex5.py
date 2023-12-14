def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(date):
    if len(date) != 8:
        return False

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if mois < 1 or mois > 12:
        return False

    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if est_bissextile(annee):
        jours_par_mois[2] = 29

    if jour < 1 or jour > jours_par_mois[mois]:
        return False

    return True

def verification_date(date):
    if est_date_valide(date):
        print(f"La date {date} est valide.")
    else:
        print(f"La date {date} n'est pas valide. Veuillez corriger votre saisie.")

date_utilisateur = input("Entrez une date (jjmmaaaa) : ")
verification_date(date_utilisateur)

