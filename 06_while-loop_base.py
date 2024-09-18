'''
Write Python program :
    get an input for a number to count to
    if input is "q" or "quit", the program exitsk
    else write numbers from 1 to the number in one line, separated by space and goes back to the input
'''
def elszamolas():
    while True:
        bekeres = input("Adj meg egy számot, ameddig elszámoljak. A kilépéshez írj 'k' betűt vagy azt hogy 'kilép' ")
        
        if bekeres.lower() in ['k', 'kilép']:
            print("Kilépés a programból.")
            break
        szamol = int(bekeres)
        szam = ' '.join(str(i) for i in range(1, szamol + 1))
        print(szam)
       
elszamolas()
