def texto_para_morse(text):
    morse = {" ": "|",'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..','E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.'
             '','S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..',
             '0': '-----', '1': '.----','2': '..---', '3': '...--','4': '....-', '5': '.....','6': '-....', '7': '--...'
            ,'8': '---..', '9': '----.'}
    codigo_morse = ""
    for x in text:
        codigo_morse += morse[x]

    return codigo_morse
text = input("Escreva para converter para Código Morse: ")
print(texto_para_morse(text))
