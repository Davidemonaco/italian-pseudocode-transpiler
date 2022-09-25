legend = {
        "Opzioni da console": '-show ti permette di visualizzare il codice python risultato della conversione\n-file ti permette di aprire un file ed eseguirlo\n-output ti permette di salvare il codice python in un file esterno\n-replace ti permette di sostituire il file se già esistente, senza chiedere conferma',
        "PROGRAMMA": "Sintassi: PROGRAMMA nomeprogramma\nÈ il primo comando in un programma scritto in pseudocodice, dà il nome al programma.",
        "INIZIO": "Necessario in ogni programma scritto in pseudocodice, è il punto di partenza del programma.",
        "LEGGI": "Sintassi: LEGGI(nomevariabile)\nChiede l'input dell'utente e lo salva in una variabile.",
        "SCRIVI": "Sintassi: SCRIVI(valore)\nScrive sulla console il valore che gli viene dato.",
        "SE": "Sintassi: SE(condizione)\nEsegue il codice all'interno se e solo se la condizione è VERA.",
        "FINE": "Indica la fine di un blocco condizionale o altri comandi che raggruppano varie linee di codice",
        "FINE.": "Esce da un blocco MENTRE; esce dal programma quando usato per uscire da un blocco INIZIO"
        }
def autotype(value):
    try:
        return int(value)
    except:
        return(value)
def sep():
    print('-_'*15)
def open():
    while True:
        for i, x in zip(legend.keys(), range(1, len(legend)+1)):
            print(f"{x}. {i}")
        print('X. Esci')
        choice = autotype(input('-> '))
        if type(choice) == int:
            try:
                sep()
                print(list(legend.keys())[choice-1])
                print(legend[list(legend.keys())[choice-1]])
                sep()
            except IndexError: 
                print(f"{choice} non è un'opzione valida. riprova")
        else:
            if choice.lower() == 'x':
                break
            try:
                sep()
                print(choice)
                print(legend[choice])
                sep()
            except KeyError:
                print(f"{choice} non è un'opzione valida. riprova")

