# Generateur de Base de Données

À utiliser pour générer : 
-  des tables SQL  à la main
- un MCD à la main
- des tables SQL à partir d'un mcd 
- une table SQL à partir d'un fichier .csv
- ainsi que pour afficher les tables créées
## Installation 

```bash
$ git clone https://github.com/Mel0101010/Generateur_SQL.git
```

```bash
$ cd Generateur_SQL
```

```bash
$ python main.py
```

choisissez alors ce que vous voulez faire en utilisant le menu devant vous

## Installation des Dépendances

Debian-based
```bash
sudo apt update
sudo apt install sqlite3 python3-pip
pip install mocodo
```

arch-based
```bash
sudo pacman -Syu
sudo pacman -S sqlite python3-pip
pip install mocodo
```


## Contraintes

### Dépendences

Python -> 3.10
SQLite -> 3.0
Mocodo -> 3.0

###  CSV -> SQL

le fichier CSV doit etre de la forme suivante : 
```csv
Nom_de_la_table
attribut1,attribut2,attribut3...
value1,value2,value3...
...
```
### Types SQL 
Chaque attribut pour une conversion en SQL doit etre typé selon un des types suivants : 

- Bit 
- Char
-  DateTime
-  Decimal
-  Float
-  Integer
-  Money
-  Numeric
-  Real
-  SmallDateTime
-  SmallInt
-  SmallMoney
-  TinyInt
-  VarChar

## Autres

les fichiers MCD ou SQL créés seront dans le dossier /filescreated
