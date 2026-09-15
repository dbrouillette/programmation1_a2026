# Auteur    :
# Sujet     : Démo du module `datetime`

import datetime
import locale   # pour afficher en français

# --- 2. Date du jour -------------------------------------------------------
print("=== Date du jour ===")
date_du_jour = datetime.date.today()
print("date_du_jour ->", date_du_jour)
print("date_du_jour.year ->", date_du_jour.year)
print("date_du_jour.month ->", date_du_jour.month)
print("date_du_jour.day ->", date_du_jour.day)

# --- 3. Date et heure actuelles ---------------------------------------------
print("\n=== Date et heure actuelles ===")
maintenant = datetime.datetime.now()
print("maintenant ->", maintenant)
print("maintenant.hour ->", maintenant.hour)
print("maintenant.minute ->", maintenant.minute)
print("maintenant.second ->", maintenant.second)

# --- 4. Formater une date ou une heure --------------------------------------
print("\n=== Formatage avec strftime ===")
print("maintenant.strftime('%d/%m/%Y %H:%M:%S') ->", maintenant.strftime("%d/%m/%Y %H:%M:%S"))
print("date_du_jour.strftime('%A %d %B %Y') ->", date_du_jour.strftime("%A %d %B %Y"))
# Force les noms de jours/mois en français pour %A et %B (voir section 4)
try:
    locale.setlocale(locale.LC_TIME, "fr_CA")
except locale.Error:
    print("Locale 'fr_CA' indisponible, les noms de jours/mois resteront en anglais.")
print("date_du_jour.strftime('%A %d %B %Y') ->", date_du_jour.strftime("%A %d %B %Y"))
print(f"Date julienne = {date_du_jour.strftime("%j")}e jour de l'année")
print(f"Représentation locale de la date et de l'heure avec %c = {maintenant.strftime("%c")}")

# --- 5. Exemple complet -----------------------------------------------------
print("\n=== Exemple complet ===")
print(f"Il est {maintenant.strftime('%H:%M')} le {maintenant.strftime('%d/%m/%Y')}")
