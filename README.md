# Cinderella Toolkit (2011 Edition)

*Ein minimalistischer Static Site Generator in Python – geschrieben von mir im Jahr 2011, lange bevor ich wusste, dass es sowas wie „SSGs“ überhaupt gibt.*

Cinderella Toolkit erzeugt statische Webseiten aus HTML-Templates, indem Platzhalter wie `<!--MENU-->`, `<!--TITLE-->` oder `<!--DESCRIPTION-->` durch vorbereitete Inhalte ersetzt werden.

Es wurde für einen Webspace geschrieben, der **kein PHP**, **keine Serverlogik** und **keine dynamischen Features** unterstützte. Auch moderne JavaScript-Funktionen wie `fetch()` gab es damals schlicht noch nicht. Alles basiert auf lokalem HTML, CSS und JavaScript – und einem einfachen Python-Script

---

## Funktionen

- Einfache Templating-Logik mit Platzhaltern
- Kompatibel mit Python 2 **und** 3
- XHTML 1.0 Strict  
- Unterstützt Superfish-Menüs über jQuery
- Generiert reine HTML-Dateien – keine Server-Abhängigkeit

---

## Verwendung

```bash
python cinderella.py
``
- Deine Templates kommen in den Ordner templates/
- Die z.B. Menü-Datei liegt in input/menu.txt
- Das Script erzeugt die fertigen Dateien in output/

Das hier war mein allererstes echtes Python-Projekt – geschrieben 2011, weil ich keinen Bock mehr hatte, bei jeder kleinen Änderung im Menü 20 HTML-Dateien per Hand zu aktualisieren. Damals wusste ich noch nicht, dass es dafür später mal den Begriff "Static Site Generator" geben würde.

Ich habe es Cinderella Toolkit genannt, weil es Dinge schöner macht – bevor die Uhr Mitternacht schlägt

## Lizenz

MIT – du darfst alles damit machen. Wenn du schmunzeln musstest, dann hat sich der Upload schon gelohnt
