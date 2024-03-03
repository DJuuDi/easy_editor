import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_noets()
        self.ui.noet_list.addItems(self.notes)
        self.ui.noet_list.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_note)
        self.ui.create_btn.clicked.connect(self.create_note)
        self.ui.delete_btn.clicked.connect(self.delete_note)
        self.ui.add_teg_btn.clicked.connect(self.add_tag)
        self.ui.unpin_teg_btn.clicked.connect(self.del_tag)

    def show_note(self):
        self.name = self.ui.noet_list.selectedItems()[0].text()
        self.ui.title_edit.setText(self.name)
        self.ui.text_edit.setText(self.notes[self.name]["текст"])
        self.ui.noet_lnst.clear()
        self.ui.noet_lnst.addItems(self.notes[self.name]["теги"])

        
    def save_note(self):
        tags = []
        for i in range(self.ui.tag_list.count()):
            tags.append(self.ui.tag_list.item(i).text())
        self.notes[self.ui.title_edit.text()] = {
            "текст": self.ui.text_edit.toPlainText(),
            "теги":[]
        }
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file)
        self.ui.noet_list.clear()
        self.ui.noet_list.addItems(self.notes)

    def clear(self):
        self.ui.title_edit.clear()
        self.ui.text_edit.clear()

    def create_note(self):
        self.clear()

    def read_noets(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "Гугл замітка":{
                    "текст": "акк: juliagergun@gmail.com, пароль: 5345julia5345",
                    "теги": []
            }
        }

    def delete_note(self):
        try:
            del self.notes[self.name]
            self.clear()
            self.ui.noet_list.clear()
            self.ui.noet_list.addItems(self.notes)
            self.save_note()
        except:
            print("")

    def add_tag(self):
        tag_name = self.ui.search_l.text()
        if tag_name!="":
            if tag_name not in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].append(tag_name)
                self.ui.noet_lnst.clear()
                self.ui.noet_lnst.addItems(self.notes[self.name]["теги"])

    def del_tag(self):
        if self.ui.noet_lnst.selectedItems():
            tag_name = self.ui.noet_lnst.selectedItems()[0].text()
            if tag_name in self.notes[self.name]["теги"]:
                    self.notes[self.name]["теги"].remove(tag_name)
                    self.ui.noet_lnst.clear()
                    self.ui.noet_lnst.addItems(self.notes[self.name]["теги"])
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
