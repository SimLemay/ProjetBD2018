# ProjetBD2018

## Installation pour l'execution
- Aller dans ProjetBD2018/ et effectuer cette commande pour creer la BD et le user pour l'application:
```
mysql -u root -p < scripts/creation_bd.sql
```
- Lancer l'application avec l'option --reset pour creer les tables et inserer les premieres donnees:
```
<lien vers l'executable python> ProjetBD2108.py --reset
```
- Effectuer cette commande dans ProjetBD2018/ pour creer le trigger servant au respect des quantités:
```
mysql -u root -p < scripts/creation_trigger.sql
```
- Lancer l'application:
```
<lien vers l'executable python> ProjetBD2108.py
```

## Installation pour le développement:
- Effectuer ces commandes :
```
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g npx
```

- Aller dans ProjetBD2018/static/ et effectuer ces commande pour générer le fichier bundle.js:
```
npm install
npx webpack
```
