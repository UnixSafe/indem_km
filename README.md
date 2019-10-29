# Dillinger

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)]()

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

AutoFill pourra vous faire gagner du temps.
Il permet de remplir automatiquement vos indemnités kilométriques

# New Features!

  - Gestion Automatique des Week-ends
  - config externalisée dans un fichier conf.json

### Tech

* [Pythons](https://www.python.org/) - Le meilleur langage 
* [ChromeDriver](https://chromedriver.chromium.org/) - Permets l’exécution de programme automatique sous chrome  
* [PIP](https://www.liquidweb.com/kb/install-pip-windows/) - pip est un gestionnaire de paquets utilisé pour installer et gérer des paquets
* [seleniumhq](https://www.seleniumhq.org/projects/webdriver/) - to automate web browsers across many platforms


### Installation

AutoFill requires [Pythons](https://www.python.org/) v3 to run.
Just download  and run ;) 

AutoFill requires [PIP](https://www.liquidweb.com/kb/install-pip-windows/)
- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
- Open a command prompt and navigate to the folder containing get-pip.py.
```sh
$ python get-pip.py
```
- Pip is now installed!

### Install Selenium 3

```sh
 pip install -U selenium
```


## ChromeDriver
Dowload Chrome Driver
Copy the.exe into the same folder as the.exe of google Chrome

## conf.json
````json
{
    "login" : "YoutLogin",
    "password" : "YourPassWdinBase64",
    "indemKmMenu" : "/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div/div",
    "ProfileGoogle" : "C:\\Users\\[YOUR USER NAME ]\\AppData\\Local\\Google\\Chrome\\User Data",
    "DefaultPath" : "THE PATH TO \\ indem_km",
    "VilleD": "WATTIGNIES (59139)",
    "VilleA": "VILLENEUVE-D'ASCQ (59491)",
    "Client": "Auchan Retail",
    "OBJ":"trajet journalier",
    "KM":"6"
}
`````

- password : mot de passe en base64
- indemKmMenu : config externalisé si le menu de l'intranet change (NE PAS TOUCHER)
- ProfileGoogle : le path de votre profil google en local ATTENTION TOUJOURS METTRE DEUX  '\\\\' 
- DefaultPath : le path d'éxécution du programme 
- VilleD  : Ville de départ
- VilleA : Ville d'arrivée
- OBJ : Objet du trajet
- KM : Nombre de kilomètre 

# Run

```sh
python main.py
````
