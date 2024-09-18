'''
The standard ACL numbers are between 1 and 99 (inclusive)
The extended ACL numbers are between 100 199 (inclusive)
Other ACL numbers are nor standard nor extended.
Input an ACL number and categorize it!
'''
def kategoria(szam):
    if 1 <= szam <= 99:
        print("Ez az ACL szám szabványos.")
    elif 100 <= szam <= 199:
        print("Ez az ACL szám kiterjesztett.")
    else:
        print("Ez az ACL szám nem is szabványos, de mégcsak kiterjesztett sem.")

try:
    szam = int(input("Írj be egy ACL számot: "))
    kategoria(szam)
except ValueError:
    print("Hiba! Írj be egy valós ACL számot.")
