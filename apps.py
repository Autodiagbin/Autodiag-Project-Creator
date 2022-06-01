import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import os

import project
from tinydb import TinyDB, where

CUR_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(CUR_DIR, "data")
FOLDERS_DATABASE = os.path.join(DATA_DIR, "arborescence_dossier.json")
EXPORT_DIR = os.path.join(CUR_DIR, "Export")
DB = TinyDB('historique.json')


class Ui_main_window(object):
    def __init__(self) -> None:
        self.version = "0.1"

    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(555, 630)
        main_window.setMinimumSize(QtCore.QSize(555, 630))
        main_window.setMaximumSize(QtCore.QSize(555, 630))
        main_window.setStyleSheet("")
        self.tabs = QtWidgets.QTabWidget(main_window)
        self.tabs.setGeometry(QtCore.QRect(10, 30, 531, 590))
        self.tabs.setObjectName("tabs")
        self.tab_run = QtWidgets.QWidget()
        self.tab_run.setObjectName("tab_run")

        self.btn_proceed = QtWidgets.QPushButton(self.tab_run)
        self.btn_proceed.setGeometry(QtCore.QRect(10, 500, 151, 41))
        self.btn_proceed.setObjectName("btn_proceed")
        self.btn_proceed.clicked.connect(self.proceed)
        self.btn_folder = QtWidgets.QPushButton(self.tab_run)
        self.btn_folder.setGeometry(QtCore.QRect(350, 510, 171, 41))
        self.btn_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  
        self.btn_folder.setObjectName("btn_folder")
        self.btn_folder.hide()
        self.grp_basics = QtWidgets.QGroupBox(self.tab_run)
        self.grp_basics.setGeometry(QtCore.QRect(10, 10, 281, 171))
        self.grp_basics.setObjectName("grp_basics")
        self.lab_marque = QtWidgets.QLabel(self.grp_basics)
        self.lab_marque.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.lab_marque.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                      "font-weight: bold;")
        self.lab_marque.setTextFormat(QtCore.Qt.RichText)  
        self.lab_marque.setObjectName("lab_marque")
        self.cbb_marque = QtWidgets.QComboBox(self.grp_basics)
        self.cbb_marque.setGeometry(QtCore.QRect(10, 90, 131, 22))
        self.cbb_marque.setObjectName("cbb_marque")
        self.lab_model = QtWidgets.QLabel(self.grp_basics)
        self.lab_model.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.lab_model.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                     "font-weight: bold;")
        self.lab_model.setTextFormat(QtCore.Qt.RichText)  
        self.lab_model.setObjectName("lab_model")
        self.input_model = QtWidgets.QLineEdit(self.grp_basics)
        self.input_model.setGeometry(QtCore.QRect(10, 140, 241, 20))
        self.input_model.setObjectName("input_model")
        self.lab_autodiag = QtWidgets.QLabel(self.grp_basics)
        self.lab_autodiag.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.lab_autodiag.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                        "font-weight: bold;")
        self.lab_autodiag.setTextFormat(QtCore.Qt.RichText)  
        self.lab_autodiag.setObjectName("lab_autodiag")
        self.cbb_autodiag = QtWidgets.QComboBox(self.grp_basics)
        self.cbb_autodiag.setGeometry(QtCore.QRect(10, 40, 241, 22))
        self.cbb_autodiag.setObjectName("cbb_autodiag")
        self.grp_options = QtWidgets.QGroupBox(self.tab_run)
        self.grp_options.setGeometry(QtCore.QRect(300, 110, 221, 301))
        self.grp_options.setObjectName("grp_options")
        self.lab_locate = QtWidgets.QLabel(self.grp_options)
        self.lab_locate.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.lab_locate.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                      "font-weight: bold;")
        self.lab_locate.setTextFormat(QtCore.Qt.RichText)  
        self.lab_locate.setObjectName("lab_locate")
        self.cbb_locate = QtWidgets.QComboBox(self.grp_options)
        self.cbb_locate.setGeometry(QtCore.QRect(20, 50, 171, 22))
        self.cbb_locate.setObjectName("cbb_locate")

        self.grp_buttons = QtWidgets.QGroupBox(self.grp_options)
        self.grp_buttons.setGeometry(QtCore.QRect(10, 90, 201, 201))
        self.grp_buttons.setObjectName("grp_buttons")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.grp_buttons)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.cb_option1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option1.setChecked(False)
        self.cb_option1.setObjectName("cb_option1")
        self.verticalLayout.addWidget(self.cb_option1)

        self.cb_option2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option2.setChecked(False)
        self.cb_option2.setObjectName("cb_option2")
        self.verticalLayout.addWidget(self.cb_option2)

        self.cb_option3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option3.setChecked(False)
        self.cb_option3.setObjectName("cb_option3")
        self.verticalLayout.addWidget(self.cb_option3)

        self.cb_option4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option4.setChecked(False)
        self.cb_option4.setObjectName("cb_option4")
        self.verticalLayout.addWidget(self.cb_option4)

        self.cb_option5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option5.setChecked(False)
        self.cb_option5.setObjectName("cb_option5")
        self.verticalLayout.addWidget(self.cb_option5)

        self.cb_option6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_option6.setChecked(False)
        self.cb_option6.setObjectName("cb_option6")
        self.verticalLayout.addWidget(self.cb_option6)

        self.grp_specificite = QtWidgets.QGroupBox(self.tab_run)
        self.grp_specificite.setGeometry(QtCore.QRect(10, 190, 281, 291))
        self.grp_specificite.setObjectName("grp_specificite")
        # ------------------------------------------------------------
        # Specificité  
        self.lay_list = QtWidgets.QWidget(self.grp_specificite)
        self.lay_list.setGeometry(QtCore.QRect(10, 30, 261, 249))
        self.lay_list.setObjectName("lay_list")

        self.lay_list_spec = QtWidgets.QVBoxLayout(self.lay_list)
        self.lay_list_spec.setContentsMargins(0, 0, 0, 0)
        self.lay_list_spec.setObjectName("lay_list_spec")

        self.cb_spec1 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec1.setChecked(False)
        self.cb_spec1.setObjectName("cb_spec1")
        self.lay_list_spec.addWidget(self.cb_spec1)

        self.cb_spec2 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec2.setChecked(False)
        self.cb_spec2.setObjectName("cb_spec2")
        self.lay_list_spec.addWidget(self.cb_spec2)

        self.cb_spec3 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec3.setChecked(False)
        self.cb_spec3.setObjectName("cb_spec3")
        self.lay_list_spec.addWidget(self.cb_spec3)

        self.cb_spec4 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec4.setChecked(False)
        self.cb_spec4.setObjectName("cb_spec4")
        self.lay_list_spec.addWidget(self.cb_spec4)

        self.cb_spec5 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec5.setChecked(False)
        self.cb_spec5.setObjectName("cb_spec5")
        self.lay_list_spec.addWidget(self.cb_spec5)

        self.cb_spec6 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec6.setChecked(False)
        self.cb_spec6.setObjectName("cb_spec6")
        self.lay_list_spec.addWidget(self.cb_spec6)

        self.cb_spec7 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec7.setChecked(False)
        self.cb_spec7.setObjectName("cb_spec7")
        self.lay_list_spec.addWidget(self.cb_spec7)

        self.cb_spec8 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec8.setChecked(False)
        self.cb_spec8.setObjectName("cb_spec8")
        self.lay_list_spec.addWidget(self.cb_spec8)

        self.cb_spec9 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec9.setChecked(False)
        self.cb_spec9.setObjectName("cb_spec9")
        self.lay_list_spec.addWidget(self.cb_spec9)

        self.cb_spec10 = QtWidgets.QCheckBox(self.lay_list)
        self.cb_spec10.setChecked(False)
        self.cb_spec10.setObjectName("cb_spec10")
        self.lay_list_spec.addWidget(self.cb_spec10)

        self.cb_spec1.hide()
        self.cb_spec2.hide()
        self.cb_spec3.hide()
        self.cb_spec4.hide()
        self.cb_spec5.hide()
        self.cb_spec6.hide()
        self.cb_spec7.hide()
        self.cb_spec8.hide()
        self.cb_spec9.hide()
        self.cb_spec10.hide()

        self.all_specs = [self.cb_spec1, self.cb_spec2, self.cb_spec3, self.cb_spec4, self.cb_spec5, self.cb_spec6,
                          self.cb_spec7, self.cb_spec8, self.cb_spec9, self.cb_spec10]

        self.cb_option1.hide()
        self.cb_option2.hide()
        self.cb_option3.hide()
        self.cb_option4.hide()
        self.cb_option5.hide()
        self.cb_option6.hide()

        self.all_options = [self.cb_option1, self.cb_option2, self.cb_option3, self.cb_option4, self.cb_option5,
                            self.cb_option6]

        self.grp_type_objet = QtWidgets.QGroupBox(self.tab_run)
        self.grp_type_objet.setGeometry(QtCore.QRect(300, 490, 221, 61))
        self.grp_type_objet.setObjectName("grp_type_objet")

        self.cb_generique = QtWidgets.QCheckBox(self.grp_type_objet)
        self.cb_generique.setChecked(False)
        self.cb_generique.setObjectName("cb_generique")
        self.cb_generique.setGeometry(QtCore.QRect(10, 30, 70, 17))

        self.cb_specifique = QtWidgets.QCheckBox(self.grp_type_objet)
        self.cb_specifique.setChecked(False)
        self.cb_specifique.setObjectName("cb_specifique")
        self.cb_specifique.setGeometry(QtCore.QRect(120, 30, 70, 17))
        # ------------------------------------------------------------

        self.grp_info = QtWidgets.QGroupBox(self.tab_run)
        self.grp_info.setGeometry(QtCore.QRect(300, 419, 221, 71))
        self.grp_info.setObjectName("grp_info")
        self.lb_information = QtWidgets.QLabel(self.grp_info)
        self.lb_information.setGeometry(QtCore.QRect(20, 20, 181, 16))
        self.lb_information.setObjectName("lb_information")
        self.tabs.addTab(self.tab_run, "")
        self.tab_opt_sup = QtWidgets.QWidget()
        self.tab_opt_sup.setObjectName("tab_opt_sup")
        self.input_prefix = QtWidgets.QLineEdit(self.tab_opt_sup)
        self.input_prefix.setGeometry(QtCore.QRect(140, 20, 121, 20))
        self.input_prefix.setObjectName("input_prefix")
        self.lb_prefix = QtWidgets.QLabel(self.tab_opt_sup)
        self.lb_prefix.setGeometry(QtCore.QRect(10, 20, 126, 16))
        self.lb_prefix.setObjectName("lb_prefix")
        self.cb_suivi = QtWidgets.QCheckBox(self.tab_opt_sup)
        self.cb_suivi.setGeometry(QtCore.QRect(0, 60, 141, 17))
        self.cb_suivi.setLayoutDirection(QtCore.Qt.RightToLeft)  
        self.cb_suivi.setTristate(False)
        self.cb_suivi.setObjectName("cb_suivi")

        self.btn_dir = QtWidgets.QToolButton(self.tab_opt_sup)
        self.btn_dir.setGeometry(QtCore.QRect(490, 120, 31, 21))
        self.btn_dir.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_dir.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)  
        self.btn_dir.setObjectName("btn_dir")
        self.btn_dir.clicked.connect(self.get_directory)

        self.btn_delete_histo = QtWidgets.QToolButton(self.tab_opt_sup)
        self.btn_delete_histo.setGeometry(QtCore.QRect(470, 180, 41, 23))
        self.btn_delete_histo.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_delete_histo.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)  
        self.btn_delete_histo.setObjectName("btn_delete_histo")
        self.btn_delete_histo.clicked.connect(self.delete_from_history)

        self.btn_search_histo = QtWidgets.QToolButton(self.tab_opt_sup)
        self.btn_search_histo.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.btn_search_histo.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_search_histo.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)  
        self.btn_search_histo.setObjectName("btn_search_histo")
        self.btn_search_histo.clicked.connect(self.search)

        self.btn_search_all = QtWidgets.QToolButton(self.tab_opt_sup)
        self.btn_search_all.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.btn_search_all.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_search_all.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)  
        self.btn_search_all.setObjectName("btn_search_all")
        self.btn_search_all.clicked.connect(self.get_history)

        self.btn_open_directory = QtWidgets.QToolButton(self.tab_opt_sup)
        self.btn_open_directory.setGeometry(QtCore.QRect(420, 180, 41, 23))
        self.btn_open_directory.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_open_directory.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)  
        self.btn_open_directory.setObjectName("btn_open_directory")
        self.btn_open_directory.clicked.connect(self.open_dir)

        self.lb_dir = QtWidgets.QLabel(self.tab_opt_sup)
        self.lb_dir.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.lb_dir.setObjectName("lb_dir")
        self.input_dir = QtWidgets.QLineEdit(self.tab_opt_sup)
        self.input_dir.setGeometry(QtCore.QRect(10, 120, 471, 20))
        self.input_dir.setObjectName("input_dir")
        self.table_histo = QtWidgets.QTableWidget(self.tab_opt_sup)
        self.table_histo.setGeometry(QtCore.QRect(10, 210, 511, 330))
        self.table_histo.setObjectName("table_histo")

        self.get_history()

        self.lb_histo = QtWidgets.QLabel(self.tab_opt_sup)
        self.lb_histo.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.lb_histo.setObjectName("lb_histo")
        self.input_search_histo = QtWidgets.QLineEdit(self.tab_opt_sup)
        self.input_search_histo.setGeometry(QtCore.QRect(10, 180, 171, 20))
        self.input_search_histo.setObjectName("input_search_histo")
        self.tabs.addTab(self.tab_opt_sup, "")
        self.logo = QtWidgets.QLabel(main_window)
        self.logo.setGeometry(QtCore.QRect(310, 58, 231, 101))
        self.logo.setPixmap(QtGui.QPixmap("data/logo.png"))
        self.logo.setObjectName("logo")

        self.lab_version = QtWidgets.QLabel(self.grp_basics)
        self.lab_version.setGeometry(QtCore.QRect(150, 70, 61, 16))
        self.lab_version.setStyleSheet("font: 10pt \"Trebuchet MS\";\n"
                                       "font-weight: bold;")
        self.lab_version.setTextFormat(QtCore.Qt.RichText)  
        self.lab_version.setObjectName("lab_version")

        self.input_version = QtWidgets.QLineEdit(self.grp_basics)
        self.input_version.setGeometry(QtCore.QRect(150, 90, 100, 20))
        self.input_version.setObjectName("input_version")

        self.retranslateUi(main_window)
        self.populate()
        self.tabs.setCurrentIndex(0)
        self.stylize()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Autodiag - Création de projet"))
        self.btn_proceed.setText(_translate("main_window", "📦 Créer le fichier projet"))
        self.btn_folder.setText(_translate("main_window", "Atteindre le dossier"))
        self.grp_basics.setTitle(_translate("main_window", "Information de base"))
        self.lab_marque.setText(_translate("main_window", "Marque"))
        self.lab_model.setText(_translate("main_window", "Modèle"))
        self.lab_autodiag.setText(_translate("main_window", "Autodiag"))
        self.grp_options.setTitle(_translate("main_window", "Options"))
        self.lab_locate.setText(_translate("main_window", "Capteur empreinte"))
        self.grp_buttons.setTitle(_translate("main_window", "Bouton d\'option"))

        self.cb_option1.setText(_translate("main_window", "Option_1"))
        self.cb_option2.setText(_translate("main_window", "Option_2"))
        self.cb_option3.setText(_translate("main_window", "Option_3"))
        self.cb_option4.setText(_translate("main_window", "Option_4"))
        self.cb_option5.setText(_translate("main_window", "Option_5"))
        self.cb_option6.setText(_translate("main_window", "Option_6"))

        self.grp_specificite.setTitle(_translate("main_window", "Spécificité de l\'appareil"))

        self.cb_spec1.setText(_translate("main_window", "Spec_1"))
        self.cb_spec2.setText(_translate("main_window", "Spec_2"))
        self.cb_spec3.setText(_translate("main_window", "Spec_3"))
        self.cb_spec4.setText(_translate("main_window", "Spec_4"))
        self.cb_spec5.setText(_translate("main_window", "Spec_5"))
        self.cb_spec6.setText(_translate("main_window", "Spec_6"))
        self.cb_spec7.setText(_translate("main_window", "Spec_7"))
        self.cb_spec8.setText(_translate("main_window", "Spec_8"))
        self.cb_spec9.setText(_translate("main_window", "Spec_9"))
        self.cb_spec10.setText(_translate("main_window", "Spec_10"))

        self.grp_info.setTitle(_translate("main_window", "Information"))
        self.lb_information.setText(_translate("main_window", "Veuillez rentrer les informations"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_run), _translate("main_window", "Execution"))
        self.lb_prefix.setText(_translate("main_window", "Prefix - [Nom de dossier]"))
        self.cb_suivi.setText(_translate("main_window", "Créer un fichier de suivi "))
        self.btn_dir.setText(_translate("main_window", "..."))
        self.lb_dir.setText(_translate("main_window", "Destination de mon dossier projet"))
        self.lb_histo.setText(_translate("main_window", "Historique"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_opt_sup), _translate("main_window", "Options sup."))
        self.btn_delete_histo.setText(_translate("main_window", "❌"))
        self.btn_search_histo.setText(_translate("main_window", "🔎"))
        self.btn_search_all.setText(_translate("main_window", "Tous"))
        self.cb_generique.setText(_translate("main_window", "Générique"))
        self.cb_specifique.setText(_translate("main_window", "Spécifique"))
        self.lab_version.setText(_translate("main_window", "Version"))
        self.grp_type_objet.setTitle(_translate("main_window", "Type objet"))
        self.btn_open_directory.setText(_translate("main_window", "📁"))

    def stylize(self):
        color_btn = "#e03567"
        color_btn2 = "#2c7ef8"
        color_bg = "#2a2a2a"
        color_bg2 = "#454545"
        color_secondary = "#faf9f9"

        main_window.setStyleSheet(f"background-color: {color_bg}; color: {color_secondary}")
        self.tabs.setStyleSheet(
            "QLineEdit {background-color: #7b7477 }" + "\n" + "QCheckBox::indicator::disabled { background: none}")
        self.table_histo.setStyleSheet(f"background-color: {color_bg2}; color: {color_secondary}")
        self.btn_proceed.setStyleSheet(f"background-color: {color_btn2}; color: {color_bg};font-weight: bold")
        self.logo.setStyleSheet(f"background-color: None;")

    def populate(self):
        checked_word = "✔"
        # On récupére toutes les entrées dans les fichier CSV dans data
        self.cbb_autodiag.addItems(project.get_autodiags())
        self.cbb_marque.addItems(project.get_marques())
        self.cbb_locate.addItems(project.get_capteurs())

        specs = project.get_specificite()
        for index in range(len(specs)):
            self.all_specs[index].show()
            self.all_specs[index].setChecked(specs[index].startswith(checked_word))
            self.all_specs[index].setObjectName(specs[index].lstrip(checked_word))
            self.all_specs[index].setText(specs[index].lstrip(checked_word))

        options = project.get_options()
        for index in range(len(options)):
            self.all_options[index].show()
            self.all_options[index].setChecked(options[index].startswith(checked_word))
            self.all_options[index].setObjectName(options[index].lstrip(checked_word))
            self.all_options[index].setText(options[index].lstrip(checked_word))

    def proceed(self):
        # Si la destination n'est pas communiqué on défini le répertoire dans "export"
        if os.path.isdir(self.input_dir.text()):
            dir = os.path.join(self.input_dir.text(), self.input_prefix.text() + self.input_model.text())
        else:
            os.makedirs(EXPORT_DIR, exist_ok=True)
            dir = os.path.join(EXPORT_DIR, self.input_prefix.text() + self.input_model.text())

        # On vérifie que le dossier n'existe pas déja
        if os.path.exists(dir):
            self.update_info("Le dossier existe déja - Vérifiez que le projet n'est pas déja crée", "error")
            return False

        # On vérifie que tout les champs sont bien renseignés
        if (
                self.cbb_autodiag.currentText() and self.cbb_marque.currentText() and self.cbb_locate.currentText() and self.input_model.text()) != "" and (
                self.cbb_autodiag.currentText() and self.cbb_marque.currentText() and self.cbb_locate.currentText() and self.input_model.text()) != None:

            # On rempli les spécificités rentré par l'utilisateur - en vérifiant qu'il sont cochés
            spec_validated = [spec.text() for spec in self.all_specs if spec.isChecked()]
            options_validated = [opt.text() for opt in self.all_options if opt.isChecked()]
            writing = []
            if self.cb_specifique.isChecked():
                writing.append("Spécifique")
            if self.cb_generique.isChecked():
                writing.append("Générique")

            # On crée le projet
            modele_suffixed = self.input_prefix.text() + self.input_model.text()
            new_project = project.Project(marque=self.cbb_marque.currentText(), modele=modele_suffixed,
                                          autodiag=self.cbb_autodiag.currentText(), path=dir, specifite=spec_validated,
                                          options=options_validated, printcpt=self.cbb_locate.currentText(),
                                          version=self.input_version.text(), writing=writing)
            new_project.create_project()

            # On pousse dans l'historique l'objet
            self.push_history(new_project)
            self.get_history()

            # On ouvre le répertoire une fois crée
            self.open_dir(path=new_project.path)
        else:
            self.update_info("Veuillez saisir toutes les informations nécessaire à la création du dossier", "warning")
            return False

    def push_history(self, project):
        DB.insert(project.__dict__)
        self.update_info("Mise à jour de l'historique", "info")

    def delete_from_history(self):

        selected = self.table_histo.selectedIndexes()
        selected_index = [index.siblingAtColumn(0).data() for index in selected]
        selected_index = list(dict.fromkeys(selected_index))

        table = DB.table("_default")
        for item in selected_index:
            table.remove(where('modele') == item)

        self.get_history()

    def search(self):
        if self.input_search_histo.text().strip() == "":
            self.update_info("La zone de recherche est vide", "warning")
            return False
        my_search = self.input_search_histo.text()
        self.get_history(search=my_search)

    def get_history(self, search=None):
        if search is None or search == "" or search == False:
            historique = DB.all()
        else:
            historique = DB.search(where('modele') == search)

        historique_count = len(historique)
        self.table_histo.setRowCount(historique_count)
        self.table_histo.setColumnCount(4)
        self.table_histo.setColumnWidth(3, 450)
        self.table_histo.setHorizontalHeaderLabels(["Modéle", "Date", "Crée par", "Chemin", "Présent"])
        self.table_histo.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        i = 0
        for mod in historique:
            histo_modele = QtWidgets.QTableWidgetItem(mod["modele"])
            histo_date = QtWidgets.QTableWidgetItem(mod["date_created"])
            histo_creator = QtWidgets.QTableWidgetItem(mod["creator"])
            histo_path = QtWidgets.QTableWidgetItem(mod["path"])
            histo_path.setBackground(self.check_dir(mod["path"]))
            histo_path.setForeground(QtGui.QColor("white"))
            histo_path.setToolTip(mod["path"])

            self.table_histo.setItem(i, 0, histo_modele)
            self.table_histo.setItem(i, 1, histo_date)
            self.table_histo.setItem(i, 2, histo_creator)
            self.table_histo.setItem(i, 3, histo_path)
            i += 1

    def open_dir(self, path):
        if path == "" or path == None or path == False:
            row = self.table_histo.currentItem().row()
            path = self.table_histo.item(row, 3).text()

        if os.path.exists(path):
            os.startfile(path)
            return True
        self.update_info("Le répertoire n'a pas été créer correctement et ne s'ouvre pas", "error")
        return False

    def get_directory(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self.input_dir, 'Hey! Select a File')
        self.input_dir.setText(filepath)

    def check_dir(self, dir):
        if os.path.exists(dir):
            return QtGui.QColor("darkGreen")
        return QtGui.QColor("red")

    def update_info(self, info, type="info"):
        if type == "warning":
            logging.warning(info)
            self.lb_information.setText(info)
            self.lb_information.setStyleSheet("color: yellow")
        elif type == "error":
            logging.error(info)
            self.lb_information.setText(info)
            self.lb_information.setStyleSheet("color: red")
        else:
            logging.info(info)
            self.lb_information.setText(info)
            self.lb_information.setStyleSheet("color: blue")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = QtWidgets.QWidget()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
