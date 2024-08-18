import json
from pprint import pprint


class Colonnes:
    codeMiMax: int = 10
    numPaiementMax: int = 10
    numIFMax: int = 10

    def __init__(self):
        self.json_schema: dict = dict()
        self.liste: list = list()

        self.get_liste()
        self.create_json_schema()

    def get_liste(self) -> None:
        """
        la liste contient des tuples :
        - code de la clé CSV (non decodee)
        - code de la clé CSV (decodee)
        - libelle correspondant du titre de la colonne CSV
        - type de la colonne (str, int...)
        - emplacement de la cle JSON (après la clé "demandeAide")
          * lorsqu'il y a un tableau mettre des crochets []
          * indiquer [concat] pour concatener le contenu des 
            differentes valeurs dans le meme champ
        """

        self.liste.append((
            "idDemandeAide", 
            "idDemandeAide", 
            "Identifiant unique de la demande d'aide",
            "string",
            "idDemandeAide"))
        self.liste.append((
            "listeIdDossier", 
            "listeIdDossier", 
            "Liste des Dossiers",
            "string",
            "listeIdDossier.idDossiersPartenaire[concat]"))

        self.liste.append((
            "codeRegion", 
            "codeRegion", 
            "Code de la région de la demande d'aide",
            "string",
            "codeRegion"))
        self.liste.append((
            "codeAutoriteGestion", 
            "codeAutoriteGestion", 
            "Code autorité de gestion",
            "string",
            "codeAutoriteGestion"))
        self.liste.append((
            "dateDepotDA", 
            "dateDepotDA", 
            "Date de dépôt de la demande d'aide",
            "string",
            "dateDepotDA"))
        self.liste.append((
            "codeStatutDA", 
            "codeStatutDA", 
            "Code statut de la demande",
            "string",
            "codeStatutDA"))

        self.liste.append((
            "horodatageGenerationFlux", 
            "horodatageGenerationFlux", 
            "Horodatage de génération du flux",
            "string",
            "horodatageGenerationFlux"))
        self.liste.append((
            "idGoPei", 
            "idGoPei", 
            "Identifiant unique du GO PEI",
            "string",
            "idGoPei"))
        self.liste.append((
            "idGal", 
            "idGal", 
            "Identifiant unique du GAL",
            "string",
            "idGal"))
        self.liste.append((
            "idProjetCooperation", 
            "idProjetCooperation", 
            "Identifiant unique du Projet Coopération",
            "string",
            "idProjetCooperation"))

        self.liste.append((
            "nouvelleInstallationIrrigationOn", 
            "nouvelleInstallationIrrigationOn", 
            "Nouvelles installations d'irrigation",
            "object",
            "nouvelleInstallationIrrigationOn"))
        self.liste.append((
            "modernisationInstallationIrrigationOn", 
            "modernisationInstallationIrrigationOn", 
            "Modernisation installations d'irrigation existantes",
            "object",
            "modernisationInstallationIrrigationOn"))
        self.liste.append((
            "recyclageEauOn", 
            "recyclageEauOn", 
            "Recyclage de l'eau",
            "object",
            "recyclageEauOn"))
        self.liste.append((
            "hautDebitOn", 
            "hautDebitOn", 
            "Haut débit",
            "object",
            "hautDebitOn"))
        self.liste.append((
            "methanisationOn", 
            "methanisationOn", 
            "Méthanisation",
            "object",
            "methanisationOn"))

        self.liste.append((
            "montantPayeBrutUEIrrigationBiomethane", 
            "montantPayeBrutUEIrrigationBiomethane", 
            "Montant payé brut part UE irrigation biométhane",
            "float64",
            "montantPayeBrutUEIrrigationBiomethane"))
        self.liste.append((
            "montantPayeBrutCofinanceIrrigationBiomethane", 
            "montantPayeBrutCofinanceIrrigationBiomethane", 
            "Montant payé brut cofinancé, part nationale et UE, irrigation biométhane",
            "float64",
            "montantPayeBrutCofinanceIrrigationBiomethane"))
        self.liste.append((
            "montantPayeBrutTopupIrrigationBiomethane", 
            "montantPayeBrutTopupIrrigationBiomethane", 
            "Montant payé brut top-up irrigation biométhane",
            "float64",
            "montantPayeBrutTopupIrrigationBiomethane"))

        self.liste.append((
            "codeMUP", 
            "codeMUP", 
            "code MUP",
            "string",
            "calculAide.donMtCalcules[].codeMUP"))
        self.liste.append((
            "montantCalculeDATopup", 
            "montantCalculeDATopup", 
            "Montant calculé top-up pour la demande d'aide",
            "float64",
            "calculAide.donMtCalcules[].montantCalculeDATopup"))
        self.liste.append((
            "montantCalculeDACofi", 
            "montantCalculeDACofi", 
            "Montant calculé cofinancé, part nationale et UE, pour la demande d'aide",
            "float64",
            "calculAide.donMtCalcules[].montantCalculeDACofi"))

        self.liste.append((
            "guidBenAide", 
            "guidBenAide", 
            "Identifiant unique du bénéficiaire de l'aide (GUID)",
            "string",
            "beneficiaireAide.guidBenAide"))
        self.liste.append((
            "exploitantAgricoleOn", 
            "exploitantAgricoleOn", 
            "Exploitant agricole",
            "object",
            "beneficiaireAide.exploitantAgricoleOn"))
        self.liste.append((
            "codeGenreBenAide", 
            "codeGenreBenAide", 
            "Code du genre du bénéficiaire de l'aide",
            "string",
            "beneficiaireAide.codeGenreBenAide"))

        # Données de paiement
        for index in range(self.numPaiementMax):
            self.liste.append((
                "codeTypePaiement{index}", 
                f"codeTypePaiement{index}", 
                f"Code type de paiement {index}",
                "string",
                "paiements[index].codeTypePaiement"))
            self.liste.append((
                "datePaiement{index}", 
                f"datePaiement{index}", 
                f"Date de paiement {index}",
                "string",
                "paiements[index].datePaiement"))
            self.liste.append((
                "montantPayeBrutTopupAssocie{index}", 
                f"montantPayeBrutTopupAssocie{index}", 
                f"Montant payé brut Top-up associé {index}",
                "float64",
                "paiements[index].donMtPayes[].montantPayeBrutTopupAssocie"))
            self.liste.append((
                "montantPayeBrutTopupDissocie{index}", 
                f"montantPayeBrutTopupDissocie{index}", 
                f"Montant payé brut Top-up dissocié {index}",
                "float64",
                "paiements[index].donMtPayes[].montantPayeBrutTopupDissocie"))
            self.liste.append((
                "montantPayeBrutCofiAssocie{index}", 
                f"montantPayeBrutCofiAssocie{index}", 
                f"Montant payé brut part nationale cofinancée associée {index}",
                "float64",
                "paiements[index].donMtPayes[].montantPayeBrutCofiAssocie"))
            self.liste.append((
                "montantPayeBrutCofiDissocie{index}", 
                f"montantPayeBrutCofiDissocie{index}", 
                f"Montant payé brut part nationale cofinancée dissociée {index}",
                "float64",
                "paiements[index].donMtPayes[].montantPayeBrutCofiDissocie"))
            self.liste.append((
                "montantPayeBrutUE{index}", 
                f"montantPayeBrutUE{index}", 
                f"Montant payé brut part UE {index}",
                "float64",
                "paiements[index].donMtPayes[].montantPayeBrutUE"))

        # Données des codes Mi
        for index in range(self.codeMiMax):
            self.liste.append((
                "codeMi{index}", 
                f"codeMi{index}", 
                f"Code de l’indicateur Mi {index}",
                "string",
                "donIndicResultats[index].codeMi"))
            self.liste.append((
                "quantiteCollecteeMi{index}", 
                f"quantiteCollecteeMi{index}", 
                f"Quantité collectée de l’indicateur Mi {index}",
                "float64",
                "donIndicResultats[index].quantiteCollecteeMi"))
            self.liste.append((
                "guidBenFinal{index}", 
                f"guidBenFinal{index}", 
                f"Identifiant unique du bénéficiaire final (GUID) {index}",
                "string",
                "donIndicResultats[index].guidBenFinal[concat]"))
            self.liste.append((
                "codeGenreBenFinal{index}", 
                f"codeGenreBenFinal{index}", 
                f"Code du genre du bénéficiaire final {index}",
                "string",
                "donIndicResultats[index].codeGenreBenFinal[concat]"))

        self.liste.append((
            "codeMUP.1", 
            "codeMUP.1", 
            "code MUP.1",
            "string",
            "donIndicRealisation.donMtUnitaires[].codeMUP"))
        self.liste.append((
            "quantiteCollecteeMU", 
            "quantiteCollecteeMU", 
            "Quantité collectée MU",
            "float64",
            "donIndicRealisation.donMtUnitaires[].quantiteCollecteeMU"))

        self.liste.append((
            "montantInteretsGainsGeneres", 
            "montantInteretsGainsGeneres", 
            "Montant des intérêts et gains générés",
            "float64",
            ""))
        self.liste.append((
            "montantRessourcesRestitueesFeader", 
            "montantRessourcesRestitueesFeader", 
            "Montant des ressources restituées FEADER",
            "float64",
            ""))
        self.liste.append((
            "montantRessourcesRestituees", 
            "montantRessourcesRestituees", 
            "Montant des ressources restituées",
            "float64",
            ""))

        # Données des Produits Financiers
        for index in range(self.numIFMax):
            self.liste.append((
                "codeProduitFinancier{index}", 
                f"codeProduitFinancier{index}", 
                f"Code du produit financier {index}",
                "string",
                ""))
            self.liste.append((
                "montantCoutsFraisGestionAttributionDirecteParticipation{index}", 
                f"montantCoutsFraisGestionAttributionDirecteParticipation{index}", 
                f"Montant des coûts et frais de gestion attribution directe fonds à participation {index}",
                "float64",
                ""))
            self.liste.append((
                "montantCoutsFraisGestionAttributionDirecteSpecifique{index}", 
                f"montantCoutsFraisGestionAttributionDirecteSpecifique{index}", 
                f"Montant des coûts et frais de gestion attribution directe fonds spécifiques {index}",
                "float64",
                ""))
            self.liste.append((
                "montantCoutsFraisGestionAppelOffreParticipation{index}", 
                f"montantCoutsFraisGestionAppelOffreParticipation{index}", 
                f"Montant des coûts et frais de gestion appel d'offre fonds à participation {index}",
                "float64",
                ""))
            self.liste.append((
                "montantCoutsFraisGestionAppelOffreSpecifique{index}", 
                f"montantCoutsFraisGestionAppelOffreSpecifique{index}", 
                f"Montant des coûts et frais de gestion appel d'offre fonds spécifiques {index}",
                "float64",
                ""))
            self.liste.append((
                "montantDepensesEligibles{index}", 
                f"montantDepensesEligibles{index}", 
                f"Montant des dépenses éligibles {index}",
                "float64",
                ""))
            self.liste.append((
                "montantRessourcesMobilisees{index}", 
                f"montantRessourcesMobilisees{index}", 
                f"Montant des ressources mobilisées {index}",
                "float64",
                ""))
            self.liste.append((
                "guidBenFinal{index}.1", 
                f"guidBenFinal{index}.1", 
                f"Identifiant unique du bénéficiaire final (GUID) {index}.1",
                "string",
                ""))

        self.liste.append((
            "montantNonPayeSanction", 
            "montantNonPayeSanction", 
            "Montant non payé suite à des sanctions",
            "float64",
            "montantsReconciliationBrutsNets[].montantNonPayeSanction"))
        self.liste.append((
            "montantRecouvre", 
            "montantRecouvre", 
            "Montant recouvré",
            "float64",
            "montantsReconciliationBrutsNets[].montantRecouvre"))

    def create_json_schema(self) -> None:
        """
        Creation d'un JSON schema sous forme de dictionnaire
        a partir de la liste
        """
        # print("\nJSON schéma:")

        for i, c1 in enumerate(self.liste):
            clesJSON = c1[4]
            if not clesJSON:
                continue

            courant = self.json_schema
            for cleJSON in clesJSON.split("."):
                if not courant.get(cleJSON):
                    courant[cleJSON] = dict()
                courant = courant[cleJSON]
            
            courant["#cleCSV#"] = c1[0]
            # print(courant)

        # pprint(self.json_schema)

    def controle_validite(self):

        print("\nNb colonnes:", len(cj.liste))
            
        # recherche de doublons
        print("\nListe des doublons de clés:")
        for i, c1 in enumerate(cj.liste):
            for j, c2 in enumerate(cj.liste):
                if j <= i:
                    continue
                if c1[1] == c2[1]:
                    print("-", c1[2], "<->", c2[2])

        print("Liste des doublons de libellés:")
        for i, c1 in enumerate(cj.liste):
            for j, c2 in enumerate(cj.liste):
                if j <= i:
                    continue
                if c1[2] == c2[2]:
                    print(c1)

        print("Types contenus dans la Liste:")
        type_liste: list = []
        for i, c1 in enumerate(cj.liste):
            if c1[3] not in type_liste:
                type_liste.append(c1[3])

        print(type_liste)


class ConvertJSON(Colonnes):

    json_filename: str
    csv_filename: str
    SEPARATEUR: str = ";"

    def __init__(self):
        super().__init__()
        self.csv: dict

    def load_data_file(self, json_filename: str) -> None:
        self.json_filename = json_filename
        with open(json_filename, encoding="utf-8") as file_handler:
            self.demandes_aide = json.load(file_handler)

    def decode(self, datas, json_schema, **options) -> None:
        """
        Decodage recursive des valeurs du JSON par rapport au schema
        """
        if datas is None or json_schema is None:
            print("Aucune donnée")
            return

        cle: str
        valeur: object

        for cle_json in json_schema:
            if "[concat]" in cle_json:
                # on concatene toutes les valeurs du tableau
                cle = cle_json.split("[")[0]
                cle_csv = json_schema.get(cle_json).get("#cleCSV#")

                valeur = ""
                for elt in datas.get(cle, []):
                    valeur = f"{valeur} {elt}".strip()
                self.csv[cle_csv] = valeur
                continue

            elif "[]" in cle_json:
                # on ne prend que la premiere valeur du tableau
                cle = cle_json.split("[")[0]
                valeur = ""
                for elt in datas.get(cle, [])[:1]:
                    self.decode(
                        elt, 
                        json_schema.get(cle_json), 
                        **options)
                continue

            elif "[index]" in cle_json:
                # Traitement du tableau à faire
                for index, elt in enumerate(datas.get(cle_json.split("[")[0], [])):
                    self.decode(
                        elt, 
                        json_schema.get(cle_json), 
                        index=index)
                continue

            elif json_schema.get(cle_json).get("#cleCSV#") is None:
                # il y a des sous cles a traiter
                self.decode(
                    datas.get(cle_json),
                    json_schema.get(cle_json))
                continue

            else:
                # cle unique à valoriser
                if options.get("index") is not None:
                    # print("index:", options.get("index"), cle_json)
                    cle_csv = f'{cle_json}.{options.get("index")}'
                    cle_csv = json_schema.get(
                        cle_json).get("#cleCSV#").format(index=options.get("index"))
                else:
                    cle_csv = cle_json
                    cle_csv = json_schema.get(cle_json).get("#cleCSV#")

                valeur = datas.get(cle_json)
                if valeur is not None:
                    self.csv[cle_csv] = valeur

    def write_file(self):
        ligne: str = ""
        # pprint(self.csv)

        # Enregistre Titres
        for col1, colonne, titre, *_ in self.liste:
            valeur = self.csv.get(colonne)
            if valeur is not None:
                ligne += f"{valeur}"

            ligne += self.SEPARATEUR

        self.file_handler.write(f"{ligne}\n")

    def process_json(self):
        ligne: str = ""

        # Enregistre Titres
        for col1, colonne, titre, *_ in self.liste:
            if titre:
                ligne += f"{titre}"
            else:
                ligne += f"{colonne}"
            ligne += self.SEPARATEUR

        self.file_handler.write(f"{ligne}\n")

        nb_docs: int = 0
        for conteneur in self.demandes_aide:
            demandeAide = conteneur.get("demandeAide")
            self.csv = dict()
            self.decode(demandeAide, self.json_schema)
            self.write_file()
            if nb_docs % 1000 == 0:
                print(".", end="", flush=True)
            nb_docs += 1

        print(f"\n{nb_docs} documents traités.")

    def convert_json_to_csv(self):

        try:
            self.csv_filename = ".".join(self.json_filename.split(".")[:-1]) + ".csv"
            with open(self.csv_filename, "w", encoding="utf-8") as self.file_handler:
                self.process_json()

        except Exception as erreur:
            print("Erreur:", erreur)
            raise erreur


if __name__ == "__main__":

    cj = ConvertJSON()
    # cj.load_data_file("UneDA.json")
    # cj.load_data_file("DeuxDA.json")
    cj.load_data_file("Ddrp_Synapse_V2.2.json")
    cj.convert_json_to_csv()
