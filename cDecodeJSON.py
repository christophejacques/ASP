import os
import sys
import json


class DecodeJSON:

    json_filename: str
    csv_filename: str
    SEPARATEUR: str = ";"

    codeMiMax: int = 10
    numPaiementMax: int = 10
    numIFMax: int = 10
    nbDocs: int = 0

    colonnes: list = list()

    def __init__(self):

        if len(sys.argv) == 2:
            self.json_filename = sys.argv[1]
        else:
            self.json_filename = "Ddrp_Synapse_V2.2.json"

        if not os.path.isfile(self.json_filename):
            raise Exception(f"Le fichier {self.json_filename!r} n'existe pas")

        if self.json_filename.split(".")[-1].lower() != "json":
            raise Exception("Le fichier doit avoir l'extension .json")

        self.csv_filename = ".".join(self.json_filename.split(".")[:-1]) + ".csv"

        print("Current Path:", os.getcwd(), flush=True)
        print(f"Traitement du fichier {self.json_filename!r}", flush=True)

        with open(self.json_filename, encoding="utf-8") as file_handler:
            self.demandes_aide = json.load(file_handler)

    def charger_noms_colonnes(self):
        """
        Charge le detail des noms de colonnes
        pour le fichier .CSV
        """

        self.colonnes.append(("idDemandeAide", "Identifiant unique de la demande d'aide"))
        self.colonnes.append(("listeIdDossier", "Liste des Dossiers"))

        self.colonnes.append(("codeRegion", "Code de la région de la demande d'aide"))
        self.colonnes.append(("codeAutoriteGestion", "Code autorité de gestion"))
        self.colonnes.append(("dateDepotDA", "Date de dépôt de la demande d'aide"))
        self.colonnes.append(("codeStatutDA", "Code statut de la demande"))

        self.colonnes.append(("horodatageGenerationFlux", "Horodatage de génération du flux"))
        self.colonnes.append(("idGoPei", "Identifiant unique du GO PEI"))
        self.colonnes.append(("idGal", "Identifiant unique du GAL"))
        self.colonnes.append(("idProjetCooperation", "Identifiant unique du Projet Coopération"))

        self.colonnes.append(("nouvelleInstallationIrrigationOn", "Nouvelles installations d'irrigation"))
        self.colonnes.append(("modernisationInstallationIrrigationOn", "Modernisation installations d'irrigation existantes"))
        self.colonnes.append(("recyclageEauOn", "Recyclage de l'eau"))
        self.colonnes.append(("hautDebitOn", "Haut débit"))
        self.colonnes.append(("methanisationOn", "Méthanisation"))

        self.colonnes.append(("montantPayeBrutUEIrrigationBiomethane", "Montant payé brut part UE irrigation biométhane"))
        self.colonnes.append(("montantPayeBrutCofinanceIrrigationBiomethane", "Montant payé brut cofinancé, part nationale et UE, irrigation biométhane"))
        self.colonnes.append(("montantPayeBrutTopupIrrigationBiomethane", "Montant payé brut top-up irrigation biométhane"))

        self.colonnes.append(("codeMUP", "code MUP"))
        self.colonnes.append(("montantCalculeDATopup", "Montant calculé top-up pour la demande d'aide"))
        self.colonnes.append(("montantCalculeDACofi", "Montant calculé cofinancé, part nationale et UE, pour la demande d'aide"))

        self.colonnes.append(("guidBenAide", "Identifiant unique du bénéficiaire de l'aide (GUID)"))
        self.colonnes.append(("exploitantAgricoleOn", "Exploitant agricole"))
        self.colonnes.append(("codeGenreBenAide", "Code du genre du bénéficiaire de l'aide"))

        for index in range(1+self.numPaiementMax):
            self.colonnes.append((f"codeTypePaiement{index}", f"Code type de paiement {index}"))
            self.colonnes.append((f"datePaiement{index}", f"Date de paiement {index}"))
            self.colonnes.append((f"montantPayeBrutTopupAssocie{index}", f"Montant payé brut Top-up associé {index}"))
            self.colonnes.append((f"montantPayeBrutTopupDissocie{index}", f"Montant payé brut Top-up dissocié {index}"))
            self.colonnes.append((f"montantPayeBrutCofiAssocie{index}", f"Montant payé brut part nationale cofinancée associée {index}"))
            self.colonnes.append((f"montantPayeBrutCofiDissocie{index}", f"Montant payé brut part nationale cofinancée dissociée {index}"))
            self.colonnes.append((f"montantPayeBrutUE{index}", f"Montant payé brut part UE {index}"))

        for index in range(self.codeMiMax+1):
            self.colonnes.append((f"codeMi{index}", f"Code de l’indicateur Mi {index}"))
            self.colonnes.append((f"quantiteCollecteeMi{index}", f"Quantité collectée de l’indicateur Mi {index}"))
            self.colonnes.append((f"guidBenFinal{index}", f"Identifiant unique du bénéficiaire final (GUID) {index}"))
            self.colonnes.append((f"codeGenreBenFinal{index}", f"Code du genre du bénéficiaire final {index}"))

        self.colonnes.append(("codeMUP", "code MUP"))
        self.colonnes.append(("quantiteCollecteeMU", "Quantité collectée MU"))

        self.colonnes.append(("montantInteretsGainsGeneres", "Montant des intérêts et gains générés"))
        self.colonnes.append(("montantRessourcesRestitueesFeader", "Montant des ressources restituées FEADER"))
        self.colonnes.append(("montantRessourcesRestituees", "Montant des ressources restituées"))

        for index in range(1+self.numIFMax):
            self.colonnes.append((f"codeProduitFinancier{index}", f"Code du produit financier {index}"))
            self.colonnes.append((f"montantCoutsFraisGestionAttributionDirecteParticipation{index}", f"Montant des coûts et frais de gestion attribution directe fonds à participation {index}"))
            self.colonnes.append((f"montantCoutsFraisGestionAttributionDirecteSpecifique{index}", f"Montant des coûts et frais de gestion attribution directe fonds spécifiques {index}"))
            self.colonnes.append((f"montantCoutsFraisGestionAppelOffreParticipation{index}", f"Montant des coûts et frais de gestion appel d'offre fonds à participation {index}"))
            self.colonnes.append((f"montantCoutsFraisGestionAppelOffreSpecifique{index}", f"Montant des coûts et frais de gestion appel d'offre fonds spécifiques {index}"))
            self.colonnes.append((f"montantDepensesEligibles{index}", f"Montant des dépenses éligibles {index}"))
            self.colonnes.append((f"montantRessourcesMobilisees{index}", f"Montant des ressources mobilisées {index}"))
            self.colonnes.append((f"guidBenFinal{index}", f"Identifiant unique du bénéficiaire final (GUID) {index}"))

        self.colonnes.append(("montantNonPayeSanction", "Montant non payé suite à des sanctions"))
        self.colonnes.append(("montantRecouvre", "Montant recouvré"))

    def process_json(self):
        """
        Transformer les données JSON en données CSV
        """

        ligne: str = ""

        self.charger_noms_colonnes()

        # Enregistre Titres
        for colonne, titre in self.colonnes:
            if titre:
                ligne += f"{titre}"
            else:
                ligne += f"{colonne}"
            ligne += self.SEPARATEUR

        self.file_handler.write(f"{ligne}\n")

        csv: dict
        for demande_aide in self.demandes_aide:
            self.nbDocs += 1
            if self.nbDocs % 1000 == 0:
                print(".", flush=True, end="")

            objet = demande_aide["demandeAide"]
            csv = dict()

            csv["guidBenAide"] = objet.get("beneficiaireAide").get("guidBenAide")
            csv["codeGenreBenAide"] = objet.get("beneficiaireAide").get("codeGenreBenAide")
            csv["exploitantAgricoleOn"] = objet.get("beneficiaireAide").get("exploitantAgricoleOn")

            for index, montants in enumerate(objet["calculAide"]["donMtCalcules"]):
                csv["codeMUP"] = montants.get("codeMUP")
                csv["montantCalculeDACofi"] = montants.get("montantCalculeDACofi")
                csv["montantCalculeDATopup"] = montants.get("montantCalculeDATopup")

            csv["idDemandeAide"] = objet.get("idDemandeAide")
            # print(csv["idDemandeAide"])

            csv["listeIdDossier"] = " ".join(objet.get("listeIdDossier").get("idDossiersPartenaire"))
            csv["codeStatutDA"] = objet.get("codeStatutDA")
            csv["codeRegion"] = objet.get("codeRegion")
            csv["codeAutoriteGestion"] = objet.get("codeAutoriteGestion")
            csv["dateDepotDA"] = objet.get("dateDepotDA")

            csv["horodatageGenerationFlux"] = objet.get("horodatageGenerationFlux")
            csv["idGoPei"] = objet.get("idGoPei")
            csv["idGal"] = objet.get("idGal")
            csv["idProjetCooperation"] = objet.get("idProjetCooperation")

            csv["nouvelleInstallationIrrigationOn"] = objet.get("nouvelleInstallationIrrigationOn")
            csv["modernisationInstallationIrrigationOn"] = objet.get("modernisationInstallationIrrigationOn")
            csv["recyclageEauOn"] = objet.get("recyclageEauOn")
            csv["hautDebitOn"] = objet.get("hautDebitOn")
            csv["methanisationOn"] = objet.get("methanisationOn")

            csv["montantPayeBrutUEIrrigationBiomethane"] = objet.get("montantPayeBrutUEIrrigationBiomethane")
            csv["montantPayeBrutCofinanceIrrigationBiomethane"] = objet.get("montantPayeBrutCofinanceIrrigationBiomethane")
            csv["montantPayeBrutTopupIrrigationBiomethane"] = objet.get("montantPayeBrutTopupIrrigationBiomethane")

            for realisation in objet.get("donIndicRealisation").get("donMtUnitaires", []):
                csv["quantiteCollecteeMU"] = realisation.get("quantiteCollecteeMU")

            for index, resultats in enumerate(objet.get("donIndicResultats", [])):
                if index > self.codeMiMax:
                    self.codeMiMax = index
                csv[f"codeMi{index}"] = resultats.get("codeMi")
                csv[f"quantiteCollecteeMi{index}"] = resultats.get("quantiteCollecteeMi")
                csv[f"guidBenFinal{index}"] = None

            for mtReconciliation in objet.get("montantsReconciliationBrutsNets", []):
                csv["montantNonPayeSanction"] = mtReconciliation.get("montantNonPayeSanction")
                csv["montantRecouvre"] = mtReconciliation.get("montantRecouvre")

            for index, paiement in enumerate(objet.get("paiements", [])):
                if index > self.numPaiementMax:
                    self.numPaiementMax = index
                csv[f"codeTypePaiement{index}"] = paiement.get("codeTypePaiement")
                csv[f"datePaiement{index}"] = paiement.get("datePaiement")
                for mtPaye in paiement.get("donMtPayes", []):
                    csv[f"montantPayeBrutCofiAssocie{index}"] = mtPaye.get("montantPayeBrutCofiAssocie")
                    csv[f"montantPayeBrutCofiDissocie{index}"] = mtPaye.get("montantPayeBrutCofiDissocie")
                    csv[f"montantPayeBrutTopupAssocie{index}"] = mtPaye.get("montantPayeBrutTopupAssocie")
                    csv[f"montantPayeBrutTopupDissocie{index}"] = mtPaye.get("montantPayeBrutTopupDissocie")
                    csv[f"montantPayeBrutUE{index}"] = mtPaye.get("montantPayeBrutUE")

            # Transfert du contenu du dictionnaire csv 
            # dans une ligne du fichier .CSV
            ligne = ""
            for colonne, *_ in self.colonnes:
                valeur = csv.get(colonne)
                if valeur is not None:
                    ligne += f"{valeur}"
                ligne += self.SEPARATEUR

            # Ecriture de la ligne dans le fichier
            self.file_handler.write(f"{ligne}\n")

    def run(self):

        try:
            with open(self.csv_filename, "w", encoding="utf-8") as self.file_handler:
                self.process_json()

        except Exception as erreur:
            print("Erreur:", erreur)

        print()
        print(self.nbDocs, "documents traités.")
        print(f"Fichier {self.csv_filename!r} créé avec succès.")


d = DecodeJSON()
d.run()
