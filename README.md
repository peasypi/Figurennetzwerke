# Figurennetzwerke 

Hallo und willkommen im Git vom Drama Mining Projekt

## HOW TO USE SENTINET (MAC)
Um SentiNet zu nutzen, müssen zu aller erst ein paar Dinge eingerichtet werden, damit alles funktioniert.
###### 1. Repo clonen
```sh
$ git clone https://git.informatik.uni-leipzig.de/vp38kaqy/figurennetzwerk.git
```
###### 2. Requierements installieren.

```sh
$ pip install -r requierements.txt
```

###### 3. In den richtigen Ordner gehen
```sh
$ cd ~/figurennetzwerk/App
```

###### 4.
```sh
$ export FLASK_APP=App
```

###### 5.
```sh
$ export FLASK_ENV=development
```
###### 6. 
```sh
$ flask run 
```

###### 7.
App im Browser aufrufen unter: *localhost:5000* 

###### 8.
Nun kann SentiNet genutzt werden!

###### 9.
Wähle ein Drama aus der Dropdown-Liste 
_ODER_
Gib den Namen, Autoren und Akt eines zu analysierenden Dramas ein.
Falls du das gesamte Drama analysieren willst -- wähle bei Akt 0.

###### 10. 
Nach dem die Analyse abgeschlossen ist, kannst du in der Dropdownliste unter *Dein Drama* den Graphen anzeigen lassen.

## HOW TO USE SENTINET (WINDOWS)
###### 1. Microsoft Visual C++ Build Tool installieren
Unter dem Link [https://visualstudio.microsoft.com/de/downloads/] muss das Visual Studio 2019 installiert werden (unter Community -> kostenloser Download)
Ist der Installer installiert, muss jetzt ausgewählt werden, was gebraucht wird: 
a) Unter "Windows" "Desktop Developer with C++" auswählen
b) Unter "Web & Cloud" "Python development" auswählen, dann beides installieren 
###### 2. Repo clonen
```sh
$ git clone https://git.informatik.uni-leipzig.de/vp38kaqy/figurennetzwerk.git
```
###### 2. Requierements installieren.

```sh
$ pip install -r requierements.txt
```
###### 3. Spacy installieren 
```sh
$ py -m spacy download --user de_core_news_sm
```

Im Python-Interpreter: 
```py
import spacy
nlp = spacy.load('de_core_news_sm')
```
###### 4. In den richtigen Ordner gehen
```sh
$ cd ~/figurennetzwerk/App
```

###### 4.
```sh
$ setx FLASK_APP "App"
```

###### 5.
```sh
$ setx FLASK_ENV "development"
```

###### 7. 
```sh
$ py -m flask run 
```
sollte es hier einen Fehler geben, muss bloß cmd.exe neu gestartet werden. Dann nocheinmal py -m flask run im richtigen Ordner ausführen


###### 8.
App im Browser aufrufen unter: *localhost:5000* 

###### 9.
Nun kann SentiNet genutzt werden!

###### 10.
Wähle ein Drama aus der Dropdown-Liste 
_ODER_
Gib den Namen, Autoren und Akt eines zu analysierenden Dramas ein.
Falls du das gesamte Drama analysieren willst -- wähle bei Akt 0.

###### 11. 
Nach dem die Analyse abgeschlossen ist, kannst du in der Dropdownliste unter *Dein Drama* den Graphen anzeigen lassen.