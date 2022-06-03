import os
from datetime import date
import json
import logging

logging.basicConfig(level=logging.WARNING)

CUR_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(CUR_DIR, "data")
FOLDERS_DATABASE = os.path.join(DATA_DIR, "arborescence_dossier.json")
DATABASE = os.path.join(CUR_DIR, "src", "arborescence_source.json")
DATABASE_BASE = os.path.join(CUR_DIR, "src", "arborescence_base.json")


def construct_folders(user_settings):
    collect = user_settings["specifite"] + user_settings["options"]
    if os.path.exists(DATABASE):
        with open(DATABASE, "r", encoding='utf-8') as db:
            all_results = json.load(db)
            folders = []
            todo = {}
            for match in collect:
                if match in all_results.keys():
                    folders = folders + [i for i in all_results[match].keys() if i]
                    for fld in all_results[match].keys():
                        todo[fld] = [i for i in all_results[match][fld] if i]

            folders = folders + list(all_results["Commun"].keys())
            for com in all_results["Commun"].keys():
                todo[com] = all_results["Commun"][com]
    return folders, todo


def construct_tree(user_settings):
    todo = construct_folders(user_settings)[1]
    with open(DATABASE_BASE, "r", encoding='utf-8') as db:
        base = json.load(db)
    base["SCREENSHOT"] = base["SCREENSHOT"] + list(construct_folders(user_settings)[0])
    with open(FOLDERS_DATABASE, "w", encoding='utf-8') as db:
        json.dump(obj=base, fp=db, indent=4)
    return todo


class Project:
    def __init__(self, marque: str, modele: str, autodiag: str, specifite: list, options: list,
                 writing: list, path: str, printcpt: str = "n/a", version: str = "n/a"):
        self.marque = marque
        self.modele = modele
        self.autodiag = autodiag
        self.specifite = specifite
        self.options = options
        self.path = path
        self.printcpt = printcpt
        self.creator = get_user()
        self.date_created = date.today().strftime('%m/%d/%y')
        self.version = version
        self.writing = writing
        self.todo = {}

    def create_project(self):
        # TODO : Vérifier ce que retourne cette fonction et agir en conséquence en créant l'arbre avant traitement
        self.todo = construct_tree(user_settings=self.__dict__)
        print(self.todo)
        if os.path.isfile(FOLDERS_DATABASE):
            with open(FOLDERS_DATABASE, "r") as fd:
                data = json.load(fd)
                for dir_root in data:
                    if self.path != "" or self.path != None:
                        path = os.path.join(self.path, dir_root)
                        os.makedirs(path, exist_ok=True)
                        for dirs in data[dir_root]:
                            os.makedirs(os.path.join(path, dirs), exist_ok=True)
                    else:
                        logging.warning("ERREUR 102 : Probléme de DIRECTORY. Absent ou inexistant")
                with open(os.path.join(self.path, "nfo.json"), "w") as js:
                    json.dump(fp=js, obj=self.__dict__, indent=4)

        else:
            logging.warning("ERREUR 101 : Le fichier d'arborescence de fichier n'existe pas")


def get_user():
    return os.getlogin()


def get_marques():
    directory = os.path.join(DATA_DIR, "marques.csv")
    if os.path.isfile(directory):
        with open(directory, "r", encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les marques")
            return f


def get_specificite():
    directory = os.path.join(DATA_DIR, "specificite.csv")
    if os.path.isfile(directory):
        with open(directory, "r", encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les spécificité")
            return f


def get_options():
    directory = os.path.join(DATA_DIR, "options.csv")
    if os.path.isfile(directory):
        with open(directory, "r", encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les options")
            return f


def get_autodiags():
    directory = os.path.join(DATA_DIR, "autodiags.csv")
    if os.path.isfile(directory):
        with open(directory, "r", encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les autodiags")
            return f


def get_capteurs():
    directory = os.path.join(DATA_DIR, "capteurs.csv")
    if os.path.isfile(directory):
        with open(directory, "r", encoding='utf8') as db:
            f = db.read().splitlines()
            logging.info("COLLECT : Collecter les capteurs")
            return f


if __name__ == "__main__":
    pass
