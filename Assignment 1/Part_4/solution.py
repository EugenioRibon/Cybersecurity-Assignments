#!/usr/bin/env python3
import sys
import string
import itertools

# Standard English Letter Frequencies
ENGLISH_FREQS = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

def score_text(text):
    """
    Calculates score based on Letter Frequencies + Common Word Bonus.
    Lower score is better.
    """
    counts = {char: 0 for char in string.ascii_lowercase}
    letter_count = 0
    
    text_lower = text.lower()
    for char in text_lower:
        if char in counts:
            counts[char] += 1
            letter_count += 1
            
    if letter_count == 0: return float('inf')
    
    score = 0
    for char, count in counts.items():
        observed = count
        expected = letter_count * ENGLISH_FREQS[char]
        if expected > 0:
            score += ((observed - expected) ** 2) / expected
        else:
            score += observed * 10

    COMMON_WORDS = ["THE", "IS", "AND", "TO", "OF", "IN", "IT", 
                    "YOU", "THAT", "AN", "TIME", "HE", "RE"]
    
    text_upper = text.upper()
    
    for word in COMMON_WORDS:
        if word in text_upper:
            score -= 20

    return score

def decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_indices = [alphabet.index(k) for k in key.lower()]
    key_len = len(key)
    plaintext = ""
    k_idx = 0
    
    for char in ciphertext:
        if char.lower() in alphabet:
            c_val = alphabet.index(char.lower())
            k_val = key_indices[k_idx % key_len]
            p_val = (c_val - k_val) % 26
            
            if char.isupper():
                plaintext += alphabet[p_val].upper()
            else:
                plaintext += alphabet[p_val]
            k_idx += 1
        else:
            plaintext += char
    return plaintext

def main():
    if len(sys.argv) > 1:
        ciphertext = sys.argv[1]
    else:
        ciphertext = input("Enter ciphertext: ")

    candidates = []

    print("Cracking... (Checking key lengths 1-4)")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for length in range(1, 5): 
        for key_tuple in itertools.product(alphabet, repeat=length):
            key = "".join(key_tuple)
            decrypted_text = decrypt(ciphertext, key)
            score = score_text(decrypted_text)
            
            candidates.append((score, key, decrypted_text))

    candidates.sort(key=lambda x: x[0])

    print(f"\n--- TOP 10 CANDIDATES ---")
    for i in range(10):
        score, key, text = candidates[i]
        print(f"{i+1}. Key: {key} (Score: {score:.2f})")
        print(f"   Text: {text}")

if __name__ == "__main__":
    main()