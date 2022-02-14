
T = int(input())


like_dict = {}
dislike_dict = {}

final_like_list = []

for i in range(0, T):

    l = input().split(" ")[1:]
    d = input().split(" ")[1:]

    for i in l:
        if not i in like_dict.keys():
            like_dict[i] = 1
        else:
            like_dict[i] += 1

    for i in d:
        if not i in dislike_dict.keys():
            dislike_dict[i] = 1
        else:
            dislike_dict[i] += 1

for x in like_dict.keys():
    if (not x in dislike_dict.keys()) or (x in dislike_dict and (like_dict[x] - dislike_dict[x] > 0)):
        final_like_list.append(x)

print(len(final_like_list), end=" ")
for i in final_like_list:
    print(i, end=" ")
