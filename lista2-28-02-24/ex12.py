# Implemente um algoritmo para encontrar
# a menor string em uma lista de strings

def minor_string(strings):
    minor = strings[0]
    for string in strings:
        if len(string) < len(minor):
            minor = string
    return minor


strings = ['ab', 'abc', 'abcd', 'a', 'abcde']
print(minor_string(strings))
