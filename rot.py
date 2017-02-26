#!/bin/env python
def main():
    userChoice = int(input("1) encrypt/decrypt\n2) print all\n3) crack rot\n> "
                           ))
    if userChoice == 1:
        ciphertext = input("Ciphertext: ")
        key = int(input("Key: "))
        print("encrypted: " + rot(ciphertext, key))
    elif userChoice == 2:
        ciphertext = input("Ciphertext: ")
        printAllRot(ciphertext)
    elif userChoice == 3:
        ciphertext = input("Ciphertext: ")
        length = int(input("Minimum length: "))
        crackRot(ciphertext, length)
    else:
        print("Invalid choice")


def rot(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char == " ":
            ciphertext += " "
        else:
            ciphertext += chr((ord(char) - 97 + key) % 26 + 97)
    return ciphertext


def printAllRot(ciphertext):
    for i in range(1, 27):
        print(rot(ciphertext, i))


def crackRot(ciphertext, length):
    dictionary = open("./words_en_google", "r")
    lines = set(line.strip() for line in dictionary
                if len(line.strip()) >= length)
    possibleOutputs = {x: 0 for x in range(0, 27)}
    for i in range(1, 27):
        currentIteration = rot(ciphertext, i)
        for line in lines:
            if line.rstrip() in currentIteration:
                possibleOutputs[i] += 1
    sortedOutputs = sorted(((possibleOutputs[ip], ip)
                            for ip in possibleOutputs), reverse=True)
    for (i, k) in sortedOutputs:
        print("ROT" + str(k) + ": " + rot(ciphertext, k))


main()
