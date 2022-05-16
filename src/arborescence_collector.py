import json
from pathlib import Path

CUR_DIR = Path().cwd().resolve()
DATABASE = CUR_DIR / "arborescence_source.json"
DATABASE_BASE = CUR_DIR / "arborescence_base.json"
DATABASE_TARGET = CUR_DIR.parent / "data" / "arborescence_dossier.json"


def construct_folders(settings):
    collect = settings["specifite"] + settings["options"]
    if DATABASE.is_file():
        with open(DATABASE, "r", encoding='utf-8') as db:
            all_results = json.load(db)
            folders = []
            todo = {}
            for match in collect:
                if match in all_results.keys():
                    folders.append(match)
                    todo[match] = all_results[match].values()
            folders = folders + list(all_results["Commun"].keys())

            for com in all_results["Commun"].keys():
                todo[com] = all_results["Commun"][com]
    return folders, todo


def construct_tree(settings):
    with open(DATABASE_BASE, "r", encoding='utf-8') as db:
        base = json.load(db)
    base["SCREENSHOT"] = base["SCREENSHOT"] + list(construct_folders(settings)[0])
    with open(DATABASE_TARGET, "w", encoding='utf-8') as db:
        json.dump(obj=base, fp=db)
    return True


construct_tree()
