
def horspool(text, kelime):
    n = len(text)
    m = len(kelime)
    if m > n:
        return -1  # desen metinde yok
    skip = {}
    for i in range(m-1):
        skip[kelime[i]] = m - i - 1
    i = m - 1  # desenin son karakterinden başla
    while i < n:
        k = 0
        while k < m and kelime[m-1-k] == text[i-k]:
            k += 1
        if k == m:
            return i - m + 1  # desen metinde bulundu
        else:
            if text[i] in skip:
                i += skip[text[i]]
            else:
                i += m  # desen uzunluğu kadar kaydır
    return -1  # desen metinde yok

with open("alice_in_wonderland.txt", "r") as f:
    text = f.read()
    
kelime = input("Aranacak Değeri Girin : ")              #upon için 
sonuc = horspool(text, kelime)
print("Aranan kelimenin bulunduğu sıra : ",sonuc)


