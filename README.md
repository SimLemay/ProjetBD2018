# ProjetBD2018

## Installation pour le développement:
- Effectuer ces commandes :
```
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g npx
```

-Aller dans ProjetBD2018/static/ et effectuer ces commande pour générer le fichier bundle.js:
```
npm install
npx webpack
```
