
def DecodeWord(s, decoding_table):
    decoded_word = ""
    #Your code goes here.
    for char in s:
        if char in decoding_table:
            decoded_word += decoding_table[char]
        else:
            decoded_word += char
    return decoded_word

decoding_table = {
    'L': 'T',
    'T': 'L',
    '8': 'A',
    'A': 'E',
    'E': 'B',
    'B': 'A'
}

#encoded_word = "WBLARF8TTS"
encoded_word = "L8KAOUL"
#encoded_word = "E8N8N8"
#encoded_word = "8TRA8DY T8LA"
#encoded_word = "8TT LHA TILLTA LIMAS"	
#encoded_word = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
#encoded_word = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
#encoded_word = "UUHO"
#encoded_word = "EOUUUUOUU"
decoded_word = DecodeWord(encoded_word, decoding_table)
print("Encoded Word:", encoded_word)
print("Decoded Word:", decoded_word)