from pyscript import window, document
import os

from datetime import date
import json
import logging

logging.basicConfig(level=logging.WARNING)

CUR_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(CUR_DIR, "data")
FOLDERS_DATABASE = os.path.join(DATA_DIR, "arborescence_dossier.json")
DATABASE = os.path.join(DATA_DIR, "arborescence_source.json")
DATABASE_BASE = os.path.join(DATA_DIR, "arborescence_base.json")



my_element = document.querySelector("#test")
my_element.innerText = window.location.hostname