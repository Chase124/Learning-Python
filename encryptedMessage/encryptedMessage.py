encryptedSentence = "this if is you not are a reading very this good then way you to have hide done a it message wrong"

decryptedSentence = []

splitList = encryptedSentence.split()


for position in range(0, len(splitList)-1):
    if position % 2 == 0:
        decryptedSentence.append(splitList[position])

decryptedString = " ".join(decryptedSentence)

print decryptedString
