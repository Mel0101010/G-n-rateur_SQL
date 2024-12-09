# Generateur de Base de Données

À utiliser pour générer : 
-  des tables SQL  à la main
- un MCD à la main
- des tables SQL à partir d'un mcd 
- un mcd à partir d'un code SQL 
- une table SQL à partir d'un fichier .csv
## Utilisation 

`$ git clone https://github.com/Mel0101010/Generateur_SQL.git`

`$ cd Generateur_SQL`

`$ python main.py`

choisissez alors ce que vous voulez faire en utilisant le menu devant vous

## Contraintes

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
- Binary 
- VarBinary


