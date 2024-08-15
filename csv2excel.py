import datetime
import pandas as pd


def int2alpha(valeur: int) -> str:
    valeur -= 1
    entier, reste = divmod(valeur, 26)
    if entier:
        return chr(64+entier) + chr(65+reste)
    return chr(65+reste)


def int2colonne(valeur: int) -> str:
    caractere = int2alpha(valeur)
    return f"{caractere}:{caractere}"


def log(*datas):
    temps = datetime.datetime.now()
    print(f"{temps}", end=" - ")
    print(*datas, flush=True)


codeMiMax: int = 10
numPaiementMax: int = 10
numIFMax: int = 10
debut = datetime.datetime.now()

dtypes = {
    "Identifiant unique de la demande d'aide": "string",
    "Liste des Dossiers": "string",
    "Code de la région de la demande d'aide": "string",
    "Code autorité de gestion": "string",
    "Date de dépôt de la demande d'aide": "string",
    "Code statut de la demande": "string",
    "Horodatage de génération du flux": "string",
    "Identifiant unique du GO PEI": "string",
    "Identifiant unique du GAL": "string",
    "Identifiant unique du Projet Coopération": "string",
    "Nouvelles installations d'irrigation": "object",
    "Modernisation installations d'irrigation existantes": "object",
    "Recyclage de l'eau": "object",
    "Haut débit": "object",
    "Méthanisation": "object",
    "Montant payé brut part UE irrigation biométhane": "float64",
    "Montant payé brut cofinancé, part nationale et UE, irrigation biométhane": "float64",
    "Montant payé brut top-up irrigation biométhane": "float64",
    "code MUP": "string",
    "Montant calculé top-up pour la demande d'aide": "float64",
    "Montant calculé cofinancé, part nationale et UE, pour la demande d'aide": "float64",
    "Identifiant unique du bénéficiaire de l'aide (GUID)": "string",
    "Exploitant agricole": "object",
    "Code du genre du bénéficiaire de l'aide": "string"
}

indexPaiement: int = 1 + len(dtypes)
for index in range(1+numPaiementMax):
    dtypes.update({
        f"Code type de paiement {index}": "string",
        f"Date de paiement {index}": "string",
        f"Montant payé brut Top-up associé {index}": "float64",
        f"Montant payé brut Top-up dissocié {index}": "float64",
        f"Montant payé brut part nationale cofinancée associée {index}": "float64",
        f"Montant payé brut part nationale cofinancée dissociée {index}": "float64",
        f"Montant payé brut part UE {index}": "float64"
    })

indexCodeMi: int = 1 + len(dtypes)
for index in range(1+codeMiMax):
    dtypes.update({
        f"Code de l’indicateur Mi {index}": "string",
        f"Quantité collectée de l’indicateur Mi {index}": "float64",
        f"Identifiant unique du bénéficiaire final (GUID) {index}": "string",
        f"Code du genre du bénéficiaire final {index}": "string"
    })

dtypes.update({
    "code MUP.1": "string",
    "Quantité collectée MU": "float64",
    "Montant des intérêts et gains générés": "float64",
    "Montant des ressources restituées FEADER": "float64",
    "Montant des ressources restituées": "float64",
})

indexProduitFinancier: int = 1 + len(dtypes)
for index in range(1+numIFMax):
    dtypes.update({
        f"Code du produit financier {index}": "string",
        f"Montant des coûts et frais de gestion attribution directe fonds à participation {index}": "float64",
        f"Montant des coûts et frais de gestion attribution directe fonds spécifiques {index}": "float64",
        f"Montant des coûts et frais de gestion appel d'offre fonds à participation {index}": "float64",
        f"Montant des coûts et frais de gestion appel d'offre fonds spécifiques {index}": "float64",
        f"Montant des dépenses éligibles {index}": "float64",
        f"Montant des ressources mobilisées {index}": "float64",
        f"Identifiant unique du bénéficiaire final (GUID) {index}.1": "string"
    })

dtypes.update({
    "Montant non payé suite à des sanctions": "float64",
    "Montant recouvré": "float64"
})

nb_colonnes_total: int = len(dtypes)

if False:
    from_filename = "Ddrp_Synapse_V2.2.csv"
    to_filename = "Ddrp_Synapse_V2.2.xlsx"
else:
    from_filename = "dix_lignes.csv"
    to_filename = "dix_lignes.xlsx"

# Lecture du fichier CSV
log("Lecture du fichier CSV:", from_filename)
df = pd.read_csv(
    from_filename, 
    sep=";", 
    header=0, 
    dtype=dtypes,
    index_col=False, 
    low_memory=False, 
    encoding="utf-8")

log("Taille des données:", f"""{nb_colonnes_total}x{df["Identifiant unique de la demande d'aide"].count()}""")

# Transforme le format string (datetime UTC) en format Excel datetime 
df["Horodatage de génération du flux"] = \
    pd.to_datetime(df["Horodatage de génération du flux"], 
        utc=True).dt.tz_localize(None)

# Enregistrement du fichier Excel
log("Enregistrement du fichier Excel:", to_filename)

with pd.ExcelWriter(to_filename, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name='Synapse', index=False)

    log("Formatage des données")
    workbook = writer.book
    worksheet = writer.sheets['Synapse']

    # Formats personnalisés
    format_RightColBorder = workbook.add_format({'right': 3})
    format_LeftColBorder = workbook.add_format({'left': 3})
    format_numerique = workbook.add_format({'num_format': '#,##0.00'})

    # Figer la première colonne et la première ligne
    worksheet.freeze_panes(1, 1)

    # Formatage des colonnes
    worksheet.set_column('A:B', 20)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('G:G', 30)

    # GO PEI ...
    worksheet.set_column('H:J', 16)

    # code MUP
    worksheet.set_column('S:S', 22)
    worksheet.set_column('T:U', 12, format_numerique)

    # GUID
    for colonne in ["V"]:
        worksheet.set_column(f"{colonne}:{colonne}", 45)

    worksheet.set_column('EP:EP', 22)
    worksheet.set_column("ER:ET", 12, format_numerique)

    # Appliquer les formats
    for num_colonne in range(1+numPaiementMax):
        # Paiements
        worksheet.set_column(int2colonne(indexPaiement + 7*num_colonne), 
            cell_format=format_LeftColBorder)

        # Date de paiement
        worksheet.set_column(int2colonne(1+indexPaiement + 7*num_colonne), 12)

        # Montants du paiement
        worksheet.set_column(
            int2alpha(indexPaiement+2+num_colonne*7) + ":" + 
            int2alpha(indexPaiement+6+num_colonne*7), 
            12, format_numerique)

    for num_colonne in range(1+codeMiMax):
        # code Mi
        worksheet.set_column(int2colonne(indexCodeMi + 4*num_colonne), 
            cell_format=format_LeftColBorder)

        # GUID final
        worksheet.set_column(int2colonne(indexCodeMi+2 + 4*num_colonne), 45)

    for num_colonne in range(1+numIFMax):
        # Produit Financier
        worksheet.set_column(int2colonne(indexProduitFinancier + 8*num_colonne), 
            cell_format=format_LeftColBorder)

        # GUID final
        worksheet.set_column(int2colonne(7+indexProduitFinancier + 8*num_colonne), 45)

        # Produit financier
        worksheet.set_column(
            int2alpha(1+indexProduitFinancier+num_colonne*8) + ":" + 
            int2alpha(6+indexProduitFinancier+num_colonne*8), 
            12, format_numerique)

    # formattage de la premiere ligne
    format2 = workbook.add_format({"text_wrap": True, "bg_color": "#C4D79B", "border": 1})
    for i in range(0, nb_colonnes_total):
        worksheet.write(f"{int2alpha(1+i)}1", df.columns[i], format2)

fin = datetime.datetime.now()
delta = fin - debut
hours = delta.total_seconds() // 3600
minutes = (delta.total_seconds() % 3600) // 60
secondes = delta.total_seconds() % 60

duree = "{}:{}.{}".format(
    f"0{minutes}"[:2], 
    f"0{secondes}"[:2],
    f"{delta.microseconds}"[:2])

log(f"Fin (durée={duree})")
