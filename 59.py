"""
Project Euler
Problem 59

the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.

A modern encryption method is to take a text file,
convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

author:  Adam Shechter
"""
import string

WORDBANK = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as',
            'you', 'do', 'at', 'this', 'but', 'his', 'by']


def main():
    cipher_arr = loadFileToArray()
    cipher_text = decryptCypher(cipher_arr)
    ascii_value = sumAsciiVal(cipher_text)
    print('text\n{}'.format(cipher_text))
    print('Sum ascii value: {}'.format(ascii_value))


def sumAsciiVal(text):
    sumNum = 0
    for chri in text:
        print('{}  {}'.format(chri, ord(chri)))
        sumNum += ord(chri)
    return sumNum


def decryptCypher(cipherArr):
    keyGen = _keyGenerator()
    decryptText = ''
    maxWords = 0
    while 1:
        try:
            key = next(keyGen)
            wordCount = 0
            text = _decryptArr(cipherArr, key)
            for word in WORDBANK:
                result = text.lower().find(word)
                if result > -1:
                    wordCount += 1
            if wordCount > maxWords:
                maxWords = wordCount
                decryptText = text
        except StopIteration:
            break
    return decryptText


def _keyGenerator():
    for chr1 in string.ascii_lowercase:
        for chr2 in string.ascii_lowercase:
            for chr3 in string.ascii_lowercase:
                key = chr1 + chr2 + chr3
                yield key


def _decryptArr(cipher, key):
    text = ''
    keyArr = [ord(x) for x in key]
    keyInd = 0
    for chrVal in cipher:
        text += chr(int(chrVal) ^ keyArr[keyInd])
        keyInd = keyInd + 1 if keyInd < 2 else 0
    return text


def loadFileToArray():
    with open('59_cypher.txt', 'r') as f:
        cipherArr = f.read().strip().split(',')
    return cipherArr

if __name__ == '__main__':
    main()
