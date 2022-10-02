#CONVERTITORE DA PSEUDOCODIFICA A CODICE PYTHON
import re, sys
sep = lambda: print('='*30)
def reset():
    sys.argv = [sys.argv[0]]

def convert(code): # Funzione usata per la traslazione in codice python
    result = """import sys
def autotype(value):
    try:
        return int(value)
    except:
        return(value)
#↑ CODICE ARBITRARIO PER CONVERTIRE GLI INPUT IN NUMERI INTERI O VALORI ALFANUMERICI
#NON È RISULTATO DELLA CONVERSIONE.

"""
    indent = []
    if re.search("^PROGRAMMA .*",code[0]): # La prima stringa del programma deve contenere l'istruzione PROGRAMMA seguita dal nome del programma.
        result += re.sub("^PROGRAMMA (.*)", r"#\1",code[0]) # Aggiunge un commento alla prima riga del codice convertito che indica il nome del programma.
    else:
        print("ERRORE: La prima linea di codice deve essere un comando PROGRAMMA")
        return 1

    if code[1] != 'INIZIO':
        print("ERRORE: Il codice deve contenere un'istruzione INIZIO nella seconda riga.")
        return 1

    for i, x in zip(code, range(len(code))): # Controllo degli altri comandi. 
        i = i.strip()
        if len(i) == 0:
            continue
        result += (' '*4)*len(indent)
        if re.search("^#", i):
            result += i # Aggiunta dei commenti senza effettuare modifiche.
        elif re.search("ALTRIMENTI SE\(", i):
            result = result[:-4]
            result += re.sub("ALTRIMENTI SE\((.*)\)", r"elif(\1):", i) 
        elif re.search("MENTRE\(", i):
            indent.append('break')
            result += re.sub("MENTRE\((.*)\)", r"while(\1):",i) 
        elif re.search("SE\(", i):
            indent.append('')
            result += re.sub("SE\((.*)\)", r"if(\1):",i) 
        elif re.search("ALTRIMENTI", i):
            if indent[-1] == 'break':
                indent[-1] = 'pass'
            result = result[:-4]
            result += re.sub("ALTRIMENTI", r"else:", i)
        elif re.search(".*<-",i):
            result += re.sub("(.*)<-(.*)", rf"\1=\2", i) # Assegnazione variabili.
        elif re.search("^PROGRAMMA .*", i):
            result += ' ' # Codice necessario per aggiungere i commenti per il comando PROGRAMMA.
        elif re.search("^INIZIO", i):
            indent.append('')
            result += 'while __name__ == "__main__":' # Codice che dà l'entrata al main.  
        elif re.search("FINE.", i):
            result += "sys.exit()"
        elif re.search("FINE", i):
            if len(indent[-1]) != 0:
                result += indent[-1]
            indent.pop()
            result += ' '
        elif re.search("LEGGI\(",i):
            result += re.sub("LEGGI\((.*)\)", rf"\1 = autotype(input('\1: '))", i) # Prende un input dall'utente e lo salva in una variabile.
        elif re.search("SCRIVI\(",i): 
            result += re.sub("SCRIVI\((.*)\)", rf"print(\1)", i) # Scrive la variabile sulla console.
        else:
            print(f"ERRORE: PAROLA CHIAVE {i} NON VALIDA. Linea {x+1}") # ERRORE se si inserisce un comando non valido.
            print("ASSICURARSI DI AVER INSERITO PARENTESI AI COMANDI CHE LE RICHIEDONO.")
            return 1
        result += f"#{i}".rjust(int(2*max(map(len, code))) - len(result.splitlines()[-1]) + len(i)+(4*(str(code).count('FINE')+2))) # Commenti equivalenti al codice in pseudocodifica originale, con aggiunto allineamento
        result += "\n"
    
    return result

if __name__ ==  '__main__':
    choice = None
    file = None
    while True:
        #ARGOMENTO -file DA CONSOLE
        if '-file' in sys.argv:
            try:
                file = sys.argv[sys.argv.index('-file') + 1]
                choice = '2'
            except IndexError:
                print("ERRORE: L'opzione -file richiede un parametro.")
                break
        ########################
        if not choice:
            choice = input("1. Scrivi codice\n2. Apri file\n3. Manuale\nX. Esci\n-> ")
        code = []
        if choice == '1':
            print(f"Inserisci codice in pseudocodifica")
            print("Scrivere 'X' per terminare l'inserimento.")
            sep()
            code.append(f"PROGRAMMA {input('PROGRAMMA ')}")
            print("INIZIO")
            code.append("INIZIO")
            while True:
                a = input("").replace('\t', ' '*4)
                if a == "X":
                    break
                code.append(a)
        elif choice == '2':
            if not file:
                sep()
                print("USARE DIRECTORY COMPLETA O TRASCINARE FILE NELLA CONSOLE")
                file = input("Inserisci file da aprire: ")
                sep()
            try:
                with open(file, 'r') as file:
                    code = file.read().replace('\t', ' '*4).splitlines()
            except FileNotFoundError:
                print("ERRORE: Impossibile trovare il file specificato.")
                continue
        elif choice == '3':
            import Manual
            sep()
            Manual.open()
            choice = None
            sep()
            continue
        elif choice.lower() == 'x':
            break
        else:
            print("ERRORE: Opzione non valida.")
            continue
        
        if convert(code) == 1:
            reset()
            continue

        #ARGOMENTO -show DA CONSOLE
        if '-show' in sys.argv:
            sep()
            print(convert(code))
        ########################

        if not (('-file' in sys.argv) or ('-output' in sys.argv)):
            sep()
            print("ESECUZIONE CODICE...\n")
        
        #ARGOMENTO -output DA CONSOLE
        if '-output' in sys.argv:
            try:
                filename = sys.argv[sys.argv.index('-output') + 1]
                 
                if '-replace' in sys.argv:
                    mode = 'w'
                else:
                    mode = 'x'
                with open(filename, mode, encoding="utf-8") as output:
                    output.write(convert(code))
                print(f"File salvato con successo come {filename}")
            except IndexError:
                print("ERRORE: L'opzione -output richiede un parametro.")
                break
            except FileExistsError:
                print("ERRORE: Il file esiste già.")
                if 'N' not in input("Sostituirlo? (Sì)/No: "):
                    sys.argv.append('-replace')
                    continue
                else:
                    break
        ########################
        else:
            try:
                exec(convert(code))
            except SystemExit:
                sep()
                print("---ESECUZIONE TERMINATA---")
            except SyntaxError:
                sep()
                print("ERRORE DI SINTASSI.")
        #ARGOMENTO -file e -output DA CONSOLE
        if ('-file' in sys.argv) or ('-output' in sys.argv):
            break
        ########################
        sep()
        choice = None
        file = None
