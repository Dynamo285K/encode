def encode(code,key):
    new_key = ''
    x=0

    for r in range(0, len(key)):
        for i in code:
            if x> len(key)-1:
                x = x - len(key)
                q = ord(key[x])
                v = ord(i)
                new_key += chr(((((v + q) - 97) % 26) + 97))
            else:
                q = ord(key[x])
                x += 1
                v = ord(i)
                new_key += chr(((((v+q) - 97) % 26) + 97))
        return new_key


print(encode("starec a more","ropucha"))
print(encode("knedla","asdsadasdsa"))



