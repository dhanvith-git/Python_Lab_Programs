numbers = list(map(int, input("Enter numbers: ").split()))
freq = {}
for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
