import random

지원=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
   11,12,13,14,15,16,17,18,19,20,
   21,22,23,24,25,26,27,28,29,30,
   31,32,33,34,35,36,37,38,39,40,
   41,42,43,44,45,46,47,48,49,50,
   51,52,53,54]
print("지원자수 : ", len(지원))

cnt = 0
당첨=[]

for i in range(0,40):
    number = random.choice(지원)
    당첨.insert(i,number)
    지원.remove(number)
    cnt = cnt+1

print("추첨자수 : ", cnt)
당첨.sort()
print(당첨)
