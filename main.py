#CONVERTITORE DA PSEUDOCODIFICA A CODICE PYTHON
import re, sys
sep = lambda: print('='*30)
def convert(code):
    result = """def autotype(value):
        try:
            return int(value)
        except:
            return(value)
#↑ CODICE ARBITRARIO PER CONVERTIRE GLI INPUT IN NUMERI INTERI O VALORI ALFANUMERICI
#NON È RISULTATO DELLA CONVERSIONE.

"""
    if re.search("^PROGRAMMA .*",code[0]):
        result += re.sub("^PROGRAMMA (.*)", r"#\1",code[0])# + ("#PROGRAMMA " + re.sub('^PROGRAMMA (.*)', r'\1',code[0])).rjust(int(2*max(map(len, code))) - (len(code[0]) - 9) + len(code[0])) + "\n"
    for i, x in zip(code, range(len(code))):
        if re.search("^#", i):
            result += i
        elif re.search("(^PROGRAMMA .*|^INIZIO|^FINE.)", i):
            result += ' '
        elif re.search("LEGGI\(",i):
            result += re.sub("LEGGI\((.*)\)", rf"\1 = autotype(input('\1: '))", i)
        elif re.search("SCRIVI\(",i):
            result += re.sub("SCRIVI\((.*)\)", rf"print(\1)", i)
        elif re.search(".*<-",i):
            result += re.sub("(.*)<-(.*)", rf"\1=\2", i) 
        else:
            print(f"ERRORE: PAROLA CHIAVE {i} NON VALIDA. Linea {x+1}")
        result += f"#{i}".rjust(int(2*max(map(len, code))) - len(result.splitlines()[-1]) + len(i))
        result += "\n"
    
    return result
while True:
    code = []
    print(f"Inserisci codice in pseudocodifica")
    sep()
    code.append(f"PROGRAMMA {input('PROGRAMMA ')}")
    print("INIZIO")
    code.append("INIZIO")
    while True:
        a = input(" ")
        code.append(a)
        if a == "FINE.":
            break
    if '-show' in sys.argv:
        sep()
        print(convert(code))
    sep()
    print("ESECUZIONE CODICE...\n")
    exec(convert(code))
    sep()
