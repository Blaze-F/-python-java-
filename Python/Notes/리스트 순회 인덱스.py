lis = [1, 0, 1, 0, 0, 0, 1, 1, 1, 1]

# filter 사용
seq = list(filter(lambda e: lis[e] == 1, range(len(lis))))

print("filtered")
print(seq)


# enumerate 사용
seq = [i for i, ele in enumerate(lis) if ele == 1]
print("enumerate")
print(seq)

"""
output

filtered
[0, 2, 6, 7, 8, 9]
enumerate
[0, 2, 6, 7, 8, 9]

"""
