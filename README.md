# spendFlask
Spend Management web app with flask

# Pour cloner le projet 

 git clone https://github.com/rigeladkn/spendFlask.git

# Ouvrir le projet 
 cd spendFlask

# Installer les modules de l'environnnement virtuel 
 virtualenv env

# Pour démarrer l'environnenent virtuel  
 source env/bin/activate

#installer les dépendances du projet
 pip3 install -r requirements.txt
 
# Configurer le projet 
 export FLASK_APP="app/routes.py" 
 export FLASK_DEBUG=1

# Lancer le projet 
flask run