def numberOfVowels(word):
    vowels = ["a","e","i","o","u","á","à","ã","é","è","í","ì","ú","ó","õ"]
    nber = 0
    for letter in word:
        if letter in vowels:
            nber += 1
    return nber

print(numberOfVowels("olá"))
