for k1 in range(ord('a'), ord('z') + 1):
    for k2 in range(ord('a'), ord('z') + 1):
        text = ''
        for i, xor in enumerate(open('0059_cipher.txt', 'r').readline().split(',')):
            text += chr((k1, k2, ord('p'))[i % 3] ^ int(xor))
        if ' the ' in text:
            print(sum(ord(ch) for ch in text))
