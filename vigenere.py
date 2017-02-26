#!/bin/env python


def main():
    userChoice = int(input("1) encrypt\n2) decrypt\n> "))
    if userChoice == 1:
        plaintext = input("Plaintext: ")
        key = input("Key: ")
        key = key.replace(" ", "")
        print("encrypted: " + encipher(plaintext, key))
    else:
        ciphertext = input("Ciphertext: ")
        key = input("Key: ")
        key = key.replace(" ", "")
        print("decrypted: " + decipher(ciphertext, key))


def encipher(plaintext, key):
    numOfSpace = 0
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char == ' ':
            numOfSpace += 1
            ciphertext += " "
        else:
            originalLetter = ord(char) - 97
            keyLetter = ord(key[(i - numOfSpace) % len(key)]) - 97
            ciphertext += chr((originalLetter + keyLetter) % 26 + 97)
    return ciphertext


def decipher(ciphertext, key):
    numOfSpace = 0
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char == ' ':
            numOfSpace += 1
            plaintext += " "
        else:
            encipheredLetter = ord(char) - 97
            keyLetter = ord(key[(i - numOfSpace) % len(key)]) - 97
            plaintext += chr((encipheredLetter - keyLetter) % 26 + 97)
    return plaintext


main()
