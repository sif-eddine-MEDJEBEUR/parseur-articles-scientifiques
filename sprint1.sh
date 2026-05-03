#!/bin/bash

# Conversion de tous les PDFs avec pdftotext -raw
echo "=== Conversion avec pdftotext -raw ==="
for pdf in ~/corpus/*.pdf; do
    name=$(basename "$pdf" .pdf)
    pdftotext -raw "$pdf" ~/corpus/pdftotext_${name}.txt 2>/dev/null
    echo "Converti : $name"
done

# Conversion avec pdfminer
echo ""
echo "=== Conversion avec pdfminer ==="
for pdf in ~/corpus/*.pdf; do
    name=$(basename "$pdf" .pdf)
    python3 -m pdfminer.high_level "$pdf" > ~/corpus/pdfminer_${name}.txt 2>/dev/null
    echo "Converti : $name"
done

echo ""
echo "Conversion terminee !"
