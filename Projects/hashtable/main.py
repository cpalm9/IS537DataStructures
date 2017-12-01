from hash import HashTable,StringHashTable,GuidHashTable,ImageHashTable

strHT = StringHashTable()
with open('strings.txt', 'r') as f:
    for x in f:
        strHT.set(x.lower(), x)
        strHT.get(x.lower())