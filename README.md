# Parseur d'articles scientifiques

## Description
Ce projet est un parseur d'articles scientifiques en format texte.
Il convertit des fichiers PDF en texte puis identifie et extrait les sections suivantes :
- Titre
- Auteurs
- Abstract
- Introduction
- Corps
- Conclusion
- Bibliographie

## Prérequis
- GNU/Linux
- Python 3
- pdftotext (poppler-utils)

## Installation
```bash
sudo apt install poppler-utils
```

## Utilisation

### 1. Convertir un PDF en texte
```bash
pdftotext -raw article.pdf article.txt
```

### 2. Lancer le parseur
```bash
python3 parser.py article.txt
```

## Outil de conversion choisi
Après comparaison de `pdftotext` et `pdf2txt` (pdfminer), nous avons choisi **pdftotext** avec l'option `-raw` car :
- Meilleure lisibilité du texte
- Les mots sont correctement séparés
- Les sections sont bien délimitées
