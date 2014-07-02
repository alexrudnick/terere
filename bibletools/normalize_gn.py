"""
Routines for normalizing Guarani text, mostly by Michael Gasser.
"""

import unicodedata

def clean_file(inf, outf):
    with open(inf, encoding='utf8') as i:
        with open(outf, 'w', encoding='utf8') as o:
            for line in i:
                line = clean(line)
                print(line, end='', file=o)

def clean(string):
    """Clean up Guarani string, replacing commonly used alternative characters"""

    # Normalize first.
    string = unicodedata.normalize("NFKC", string)

    # Nasal vowels: replace umlaut and circumflex with tilde
    string = string.replace('î', 'ĩ').replace('â', 'ã').replace('ê', 'ẽ')
    string = string.replace('ô', 'õ').replace('û', 'ũ').replace('ŷ', 'ỹ')
    string = string.replace('Î', 'Ĩ').replace('Â', 'Ã').replace('Ê', 'Ẽ')
    string = string.replace('Ô', 'Õ').replace('Û', 'Ũ').replace('Ŷ', 'Ỹ')
    string = string.replace('ï', 'ĩ').replace('ä', 'ã').replace('ë', 'ẽ')
    string = string.replace('ö', 'õ').replace('ü', 'ũ').replace('ÿ', 'ỹ')
    string = string.replace('Ï', 'Ĩ').replace('Ä', 'Ã').replace('Ë', 'Ẽ')
    string = string.replace('Ö', 'Õ').replace('Ü', 'Ũ').replace('Ÿ', 'Ỹ')
    # Galeano sometimes uses this Vietnamese vowel for some reason
    string = string.replace("ữ", "ũ")
    # Puso: use ordinary single quote
    for c in "’`´°‘":
        string = string.replace(c, "'")
    # Accented vowels; some people use grave instead of acute
    string = string.replace("à", "á").replace("è", "é").replace("ì", "í")
    string = string.replace("ò", "ó").replace("ù", "ú").replace("ỳ", "ý")
    string = string.replace("À", "Á").replace("È", "É").replace("Ì", "Í")
    string = string.replace("Ò", "Ó").replace("Ù", "Ú").replace("Ỳ", "Ý")
    # Nasal g: replace double character with circumflex g
    string = string.replace("g̃", "ĝ").replace("G̃", "Ĝ")
    # Galeano uses this
    string = string.replace("ğ", "ĝ").replace("Ğ", "Ĝ")
    return string

def basic_clean(string):
    """Clean Vikipetã contents."""
    # Simplify nasal g by replacing double character with circumflex g
    string = string.replace("g̃", "ĝ").replace("G̃", "Ĝ")
    # Puso: use ordinary single quote
    for c in "’‘":
        string = string.replace(c, "'")
    return string
