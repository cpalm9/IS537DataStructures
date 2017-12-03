from hash import HashTable,StringHashTable,GuidHashTable,ImageHashTable
import os

strHT = StringHashTable()
with open('strings.txt') as f:
    for line in f:
        strHT.set(line, line)
print("String hash table:")
strHT.debug_print()
print("\nString lookups:")
print(strHT.get('indian meal moth'))
print(strHT.get('orb-weaving spiders (banded garden spider)'))
 
GuidHT = GuidHashTable()
with open('guids.txt') as f:
    for x in f:
        GuidHT.set(x, x)
print("\nGUID hash table:")
GuidHT.debug_print()
print("\nGUID lookups:")
print(GuidHT.get('00000158691797bd77464883000a001800388ccf'))
print(GuidHT.get('00000158691797bd7746488c000a001991ef0003'))

ImageHT = ImageHashTable()
with open('images.txt') as f:
    for x in f:
        ImageHT.set(x, x)
print("\nImage hash table:")
ImageHT.debug_print()
print("\nImage lookups:")
print(ImageHT.get('document.png'))
print(ImageHT.get('security_keyandlock.png'))
