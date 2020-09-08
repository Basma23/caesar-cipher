def encrypt(text, shift): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + shift - 65) % 26 + 65) 
        else: 
            result += chr((ord(char) + shift - 97) % 26 + 97) 
    return result 

def decrypt(text, shift): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) - shift - 65) % 26 + 65) 
        else: 
            result += chr((ord(char) - shift - 97) % 26 + 97) 
    return result 

if __name__ == "__main__":
    print(encrypt('abc', 1))
    print(encrypt('abc', 10))
    print(encrypt('abc', 26))
    print(encrypt('BASMA', 30))
    print(encrypt('NiceTry', 7))
    print(decrypt('cde', 1))
    print(decrypt('klm', 10))
    print(decrypt('abc', 26))
    print(decrypt('FEWQE', 30))
    print(decrypt('UpjlAyf', 7))
    print(encrypt('It was the best of times, it was the worst of times', 1))
    print(decrypt('Juoxbtouifocftuopgoujnftaojuoxbtouifoxpstuopgoujnft', 1))
    assert encrypt('abc', 1) == 'bcd'
    assert encrypt('abc', 10) == 'klm'
    assert encrypt('abc', 26) == 'abc'
    assert encrypt('BASMA', 30) == 'FEWQE'
    assert decrypt('bcd', 1) == 'abc'
    assert decrypt('klm', 10) == 'abc'
    assert decrypt('abc', 26) == 'abc'
    assert decrypt('FEWQE', 30) == 'BASMA'
    assert decrypt('UpjlAyf', 7)
    print('All tests are passed!!!')