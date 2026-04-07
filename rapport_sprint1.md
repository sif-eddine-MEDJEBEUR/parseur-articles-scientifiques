# Rapport Sprint 1 - Comparaison des outils de conversion PDF vers texte

## Équipe
- Maître SCRUM : Sif-Eddine Medjebeur

## Objectif
Comparer deux outils de conversion PDF en texte : `pdftotext` et `pdf2txt` (pdfminer),
afin de choisir le plus adapté pour le parseur d'articles scientifiques.

## Outils testés

### 1. pdftotext (poppler-utils)

**Installation :**
```bash
sudo apt install poppler-utils
```

**Options testées :**

| Option | Description |
|--------|-------------|
| (aucune) | Conversion simple |
| `-layout` | Respecte la mise en page originale |
| `-raw` | Garde l'ordre du flux de contenu |

**Avantages :**
- Texte lisible avec mots correctement séparés
- Option `-raw` donne les meilleurs résultats pour les articles scientifiques
- Sections bien délimitées et faciles à parser
- Rapide et fiable

**Inconvénients :**
- L'option `-layout` produit trop d'espaces pour les articles en double colonne
- Certains caractères spéciaux peuvent être mal encodés

### 2. pdf2txt / pdfminer.six (Python)

**Installation :**
```bash
pip3 install pdfminer.six
```

**Options testées :**
```bash
python3 -m pdfminer.high_level article.pdf
python3 -c "from pdfminer.high_level import extract_text; ..."
```

**Avantages :**
- Intégrable directement en Python
- Paramétrable via LAParams

**Inconvénients :**
- Les mots sont collés sans espaces (ex: "AScalableMMRApproach...")
- Résultats souvent vides ou illisibles
- Moins fiable sur les PDFs scientifiques

## Conclusion et choix

Nous avons choisi **pdftotext avec l'option `-raw`** car il produit
un texte propre et lisible sur l'ensemble du corpus d'apprentissage (11/12 PDFs).
Le 12ème fichier (jing-cutepaste.pdf) est un PDF corrompu, indépendant de l'outil utilisé.

**Commande retenue :**
```bash
pdftotext -raw article.pdf article.txt
```
