# Create a simple IF function that compares nativeVLAN and dataVLAN values and prints result.
def hasonlitas(nativeVLAN, dataVLAN):
    if nativeVLAN == dataVLAN:
        print("A nativeVLAN és a dataVLAN egyforma.")
    else:
        print("A nativeVLAN és a dataVLAN eltérnek egymástól.")
nativeVLAN = 500
dataVLAN = 1000

hasonlitas(nativeVLAN, dataVLAN)