# Bytes to text ----------------------------------------------------------------
byte_characters = b'\x63\x6c\x69\x63\x68\xe9'
print(byte_characters)  # b'clich\xe9'
print(byte_characters.decode("latin-1"))  # cliché


# Text to bytes ----------------------------------------------------------------
text_characters = "cliché"
print(text_characters.encode("UTF-8"))  # b'clich\xc3\xa9'
print(text_characters.encode("latin-1"))  # b'clich\xe9'
print(text_characters.encode("CP437"))  # b'clich\x82'
print(text_characters.encode("ascii"))  # Traceback ...UnicodeEncodeError: 'ascii' can't encode \xe9 ...

# encode accept *strict; *replace; *ignore; *xmlcharrefreplace
print(text_characters.encode("ascii", "replace"))  # b'clich?'
print(text_characters.encode("ascii", "ignore"))   # b'clich'
print(text_characters.encode("ascii", "xmlcharrefreplace"))  # b'cliché'

# Mutable byte strings ---------------------------------------------------------
b = bytearray(b"avcdefgh")
b[4:6] = b"\x15\xa3"
print(b)  # bytearray(b'abcd\x15\xa3')

b = bytearray(b"avcdef")
b[3] = ord(b"g")  # ordinal
b[4] = 68
print(b)  # bytearray(b'abcgDfgh')
