t = int(input())
for _ in range(t):
    w = list(input())
    word_dict = list(input())
    for i in range(len(w)):
        if w[i].isalnum():
            w[i] = word_dict[int(ord(w[i])) - 65]
    print(''.join(w))
