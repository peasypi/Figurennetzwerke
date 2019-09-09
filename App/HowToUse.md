# HOW TO USE SENTINET
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
App im Browser aufrufen unter: *localhost:5000* 

###### 7.
Nun kann SentiNet genutzt werden!

###### 8.
Wähle ein Drama aus der Dropdown-Liste 
_ODER_
Gib den Namen, Autoren und Akt eines zu analysierenden Dramas ein.
Falls du das gesamte Drama analysieren willst -- wähle bei Akt 0.

###### 9. 
Nach dem die Analyse abgeschlossen ist, kannst du in der Dropdownliste unter *Dein Drama* den Graphen anzeigen lassen.

