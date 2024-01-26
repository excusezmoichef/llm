#!/bin/bash

echo "Projet LLM"
echo "------Membres------"
echo -e "Djelal BOUDJI\nVincent PETT\nTristan DURIEUX\nEdouard RINALDI"
echo "-------------------"

# Clean de l'environnement virtuel python
if [ "$1" == "--clean" ]; then
    echo "Suppression de l'environnement virtuel python"
    exit 0
    rm -rf llm-env
fi

if command -v python3 &> /dev/null; then
    python_executable="python3"
elif command -v python &> /dev/null; then
    python_executable="python"
else
    echo "Python n'est pas installé. Veuillez l'installer pour exécuter ce script."
    exit 1
fi

# Mise en place de l'environnement virtuel python
echo "Mise en place de l'environnement virtuel python"
$python_executable -m venv llm-env
source llm-env/bin/activate

# Installation des dépendences
echo "Installation des dépendences"
pip install -r requirements.txt

echo "Lancement du programme"
$python_executable main.py