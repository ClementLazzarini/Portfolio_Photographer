# Portfolio Jeannot Gougnon - Photographe 📸

Bienvenue sur le dépôt du site portfolio de Jeannot Gougnon, un photographe passionné. Ce projet a été développé pour présenter son travail, ses galeries et permettre aux visiteurs de le contacter.

Le site est développé avec le framework Python **Django** et est actuellement déployé sur **PythonAnywhere**.

---

## ✨ Fonctionnalités

* **Galerie d'images :** Présentation des différentes collections de photographies.
* **Page "À propos" :** Introduction à l'artiste, sa démarche et son parcours.
* **Formulaire de contact :** Un moyen simple pour les clients potentiels de prendre contact.
* **Design responsive :** Une expérience utilisateur optimale sur mobile, tablette et ordinateur.

---

## 🛠️ Technologies utilisées

* **Backend :** Python, Django
* **Frontend :** HTML5, CSS3, JavaScript
* **Base de données :** SQLite3 (en développement)
* **Déploiement :** PythonAnywhere

---

## 🚀 Démarrage rapide (Installation locale)

Suivez ces étapes pour lancer une version du projet sur votre machine locale.

### **1. Prérequis**

Assurez-vous d'avoir **Python 3.x** et **Git** installés sur votre système.

### **2. Installation**

1.  **Clonez ce dépôt :**
    ```bash
    git clone [https://github.com/ClementLazzarini/Portfolio_Photographer.git](https://github.com/ClementLazzarini/Portfolio_Photographer.git)
    ```

2.  **Naviguez dans le dossier du projet :**
    ```bash
    cd Portfolio_Photographer
    ```

3.  **Créez et activez un environnement virtuel :**
    ```bash
    # Sur macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Installez les dépendances :**
    Toutes les librairies nécessaires sont listées dans le fichier `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Appliquez les migrations de la base de données :**
    ```bash
    python src/manage.py migrate
    ```

6.  **Lancez le serveur de développement :**
    ```bash
    python src/manage.py runserver
    ```

Le site est maintenant accessible à l'adresse 👉 **http://127.0.0.1:8000/**

---

## ✍️ Auteur

* **Clément Lazzarini** - [GitHub @ClementLazzarini](https://github.com/ClementLazzarini)
