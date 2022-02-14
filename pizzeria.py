
T = int(input())

like_list = []
dislike_list = []

for i in range(0,T):

    l = input().split(" ")[1:]
    d = input().split(" ")[1:]

    for i in l:
        if not i in like_list:
            like_list.append(i)
    
    for i in d:
        if not i in dislike_list:
            dislike_list.append(i)

for x in like_list:
    if x in dislike_list:
        like_list.remove(x)

print(str(len(like_list)), end=" ")
for i in like_list:
    print(i, end=" ")
print()