#!/usr/bin/env python3

def main(ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for i in range(len(alphabet)):
        for c in ciphertext.lower():
            if c in alphabet:
                plaintext += alphabet[(alphabet.index(c) - i) % len(alphabet)]
            else:
                plaintext += c
        print(f"Key {i}: {plaintext}")
        plaintext = ""

if __name__ == "__main__":
    main(input("Enter the ciphertext: "))
    # main("Gb or, be abg g%b or: gung vf gur d@hrfgvba")
