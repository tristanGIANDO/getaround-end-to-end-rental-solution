# Utiliser une image de base officielle pour Python
FROM continuumio/miniconda3

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY model.pkl model.pkl

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour l'API
EXPOSE 8000

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
