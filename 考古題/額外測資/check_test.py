# test 2-1
bingo_game([[1, 2, 3], [4, 5, 6], [7, 8, 9]], n=3, pick_list=[2, 4, 6, 8])

# test 2-2
bingo_game([[5, 22, 12, 20, 23], [11, 9, 16, 19, 8], [2, 15, 21, 10, 4], [7, 18, 1, 24, 17], [25, 3, 14, 6, 13]], [[14, 15, 2, 5, 25], [19, 1, 13, 7, 4], [11, 9, 16, 21, 8], [12, 22, 23, 20, 17], [18, 6, 24, 10, 3]], [[5, 10, 21, 25, 18], [24, 22, 14, 15, 8], [11, 13, 1, 3, 2], [19, 23, 12, 9, 20], [16, 4, 6, 7, 17]], [[17, 14, 23, 9, 2], [5, 11, 25, 15, 7], [6, 10, 19, 20, 3], [13, 8, 22, 1, 4], [16, 18, 12, 21, 24]], n=5, pick_list=[24, 15, 22, 1, 7, 21, 10, 20, 25, 12, 5, 17, 3, 14, 16, 11, 23, 19])

# test 2-3
rand_cards = []
rand_pick = []
file_content = []
with open('test2-3.txt', 'r') as f:
    file_content = f.readlines()
count = 0
for i in range(7):
    li = []
    for j in range(11):
        lii = []
        for k in range(11):
            lii.append(int(file_content[count]))
            count += 1
        li.append(lii)
    rand_cards.append(li)

for i in range(11*11-11*3):
    rand_pick.append(int(file_content[count]))
    count += 1

bingo_game(*rand_cards, n=11, pick_list=rand_pick)

# test 2-4
rand_cards = []
rand_pick = []
file_content = []
with open('test2-4.txt', 'r') as f:
    file_content = f.readlines()
count = 0
for i in range(10):
    li = []
    for j in range(19):
        lii = []
        for k in range(19):
            lii.append(int(file_content[count]))
            count += 1
        li.append(lii)
    rand_cards.append(li)

for i in range(19*19-19*3):
    rand_pick.append(int(file_content[count]))
    count += 1

bingo_game(*rand_cards, n=19, pick_list=rand_pick)

# test 2-5
bingo_game([[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15], [20, 19, 18, 17, 16], [21, 22, 23, 24, 25]], n=5, pick_list=[1, 5, 25, 21, 17, 19, 9, 13, 7])

# test 2-6
rand_cards = []
file_content = []
with open('test2-6.txt', 'r') as f:
    file_content = f.readlines()
count = 0
for i in range(8):
    li = []
    for j in range(7):
        lii = []
        for k in range(7):
            lii.append(int(file_content[count]))
            count += 1
        li.append(lii)
    rand_cards.append(li)
rand_pick = [i for i in range(1, 7*7+1)]
rand_pick.reverse()
bingo_game(*rand_cards, n=7, pick_list=rand_pick)

# test 3-1
find_substrings("ababa")

# test 3-2
find_substrings("nevergonnagiveyouupnevergonnaletyoudownnevergonnarunaroundanddesertyounevergonnamakeyoucrynevergonnasaygoodbyeevergonnatellalieandhurtyou")

# test 3-3
find_substrings("ccccccc")

# test 3-4
find_substrings("ghgghhgghhgghg")

# test 3-5
find_substrings("o")

# test 3-6
find_substrings("wqehpnfkalsfhapsnvpasjofbisbdblnzmxbcoiquwghksjhdloaishdqwehhalsalwsahlsfwiqwqwlakskhlqfllakqowihflkshf")