
import os
import json
import logging

from pprint import pprint

CUR_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(CUR_DIR,"data")
FOLDERS_DATABASE = os.path.join(DATA_DIR,"arborescence_dossier.json")

logging.basicConfig(level=logging.INFO)

class Project:
    def __init__(self,marque:str,modele:str,autodiag:str,specifite:list[str],options:list[str],path:str) -> None:
        self.marque = marque
        self.modele = modele
        self.autodiag = autodiag
        self.specifite = specifite
        self.options = options
        self.path = path

    def __str__(self) -> str:
        return f"Dossier projet : {self.marque} {self.modele} - Autodiag : {self.autodiag} OPT : {self.specifite} avec options {self.options} - Destination : {self.path}"

    def getUser(self):
        return os.getlogin()

    def createProject(self):
        if os.path.isfile(FOLDERS_DATABASE):
            with open(FOLDERS_DATABASE,"r") as fd:
                data = json.load(fd)
                for dir_root in data:
                    path = os.path.join(CUR_DIR,dir_root)
                    os.makedirs(path,exist_ok=True)
                    for dirs in data[dir_root]:
                        os.makedirs(os.path.join(path,dirs),exist_ok=True)
                
        else:
            logging.warning("ERREUR 101 : Le fichier d'arborescence de fichier n'existe pas")


def get_marques():   
    directory = os.path.join(DATA_DIR,"marques.csv")       
    if os.path.isfile(directory):
        with open(directory,"r",encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les marques")
            return f

def get_specificite():
    directory = os.path.join(DATA_DIR,"specificite.csv")
    if os.path.isfile(directory):
        with open(directory,"r",encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les spécificité")
            return f

def get_autodiags():
    directory = os.path.join(DATA_DIR,"autodiags.csv")
    if os.path.isfile(directory):
        with open(directory,"r",encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les autodiags")
            return f

def get_capteurs():
    directory = os.path.join(DATA_DIR,"capteurs.csv")
    if os.path.isfile(directory):
        with open(directory,"r",encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les capteurs")
            return f




if __name__ == "__main__":
    p = Project("Samsung","Galaxy S21FE","Bouygues",["5G","eSim"],["Empreinte Façade"],"")

