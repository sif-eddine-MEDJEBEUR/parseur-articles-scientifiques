import sys
import re

def parse_article(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sections = {
        "Titre": [],
        "Auteurs": [],
        "Abstract": [],
        "Introduction": [],
        "Corps": [],
        "Conclusion": [],
        "Bibliographie": []
    }

    keywords = {
        "Abstract": r"^abstract[\s\-—:\.]*$|^abstract[\s\-—:\.]",
        "Introduction": r"^([ivxlcdm]+\.?\s+|\d+\.?\s+)?introduction$",
        "Conclusion": r"^([ivxlcdm]+\.?\s+|\d+\.?\s+)?(conclusion|discussion|future work)",
        "Bibliographie": r"^(references|bibliography|bibliographie)$"
    }

    noise = r"licens|copyright|all rights|©|^\d+$|^c\s+\d{4}"

    abstract_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^abstract", line.strip(), re.IGNORECASE):
            abstract_idx = i
            break

    # Si pas d'abstract trouvé, on prend le texte après les auteurs
    if abstract_idx is None:
        intro_idx = None
        for i, line in enumerate(lines):
            if re.match(r"^([ivxlcdm]+\.?\s+|\d+\.?\s+)?introduction$", line.strip(), re.IGNORECASE):
                intro_idx = i
                break
        if intro_idx:
            abstract_idx = intro_idx

    if abstract_idx:
        header = [l.strip() for l in lines[:abstract_idx] if l.strip()]
        header = [l for l in header if not re.search(r'pages \d+|conference|workshop|\d{4}$', l, re.IGNORECASE)]
        if header:
            sections["Titre"] = header[:2]
            sections["Auteurs"] = header[2:5]

    current_section = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if re.search(noise, stripped, re.IGNORECASE):
            continue

        matched = False
        for section, pattern in keywords.items():
            if re.match(pattern, stripped, re.IGNORECASE):
                current_section = section
                inline = re.sub(r"^abstract[\s\-—:\.]+", "", stripped, flags=re.IGNORECASE).strip()
                if section == "Abstract" and inline and inline.lower() != "abstract":
                    sections["Abstract"].append(inline)
                matched = True
                break

        if not matched and current_section:
            if current_section == "Introduction":
                if re.match(r"^([ivxlcdm]+\.?\s+|\d+\.?\s+)\w+", stripped, re.IGNORECASE) and not re.match(r"^([ivxlcdm]+\.?\s+|\d+\.?\s+)?introduction", stripped, re.IGNORECASE):
                    current_section = "Corps"
            sections[current_section].append(stripped)

    for section, content in sections.items():
        print(f"\n{'='*40}")
        print(f"{section} :")
        print('\n'.join(content[:5]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 parser.py <fichier.txt>")
    else:
        parse_article(sys.argv[1])
