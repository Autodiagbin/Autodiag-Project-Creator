import json
from pathlib import Path
from pprint import pprint

CUR_DIR = Path().cwd().resolve()
DATABASE = CUR_DIR / "arborescence_source.json"
DATABASE_BASE = CUR_DIR / "arborescence_base.json"
DATABASE_TARGET = CUR_DIR.parent / "data" / "arborescence_dossier.json"


def construct_folders(user_settings):
    collect = user_settings["specifite"] + user_settings["options"]
    if DATABASE.is_file():
        with open(DATABASE, "r", encoding='utf-8') as db:
            all_results = json.load(db)
            folders = []
            todo = {}
            for match in collect:
                if match in all_results.keys():
                    folders = folders + [i for i in all_results[match].keys() if i]
                    todo[match] = all_results[match].values()
            folders = folders + list(all_results["Commun"].keys())
            for com in all_results["Commun"].keys():
                todo[com] = all_results["Commun"][com]
    return folders, todo


def construct_tree(user_settings):
    with open(DATABASE_BASE, "r", encoding='utf-8') as db:
        base = json.load(db)
    base["SCREENSHOT"] = base["SCREENSHOT"] + list(construct_folders(user_settings)[0])
    with open(DATABASE_TARGET, "w", encoding='utf-8') as db:
        json.dump(obj=base, fp=db)
    return True


if __name__ =="__main__":
    settings = {'marque': 'ASUS', 'modele': 'mon mode', 'autodiag': 'Aide au diag', 'specifite': ['eSim', '5G'], 'options': ['Bixsby', 'Mode Silencieux ON / OFF'], 'path': 'E:\\Projects\\Autodiag Project Creator\\Export\\mon mode', 'printcpt': 'Sur le côté (Gauche)', 'creator': 'RMansouri', 'date_created': '05/17/22', 'version': 'sdf', 'type_objet': ['Spécifique', 'Générique']}
    m = construct_tree(settings)
    pprint(m)