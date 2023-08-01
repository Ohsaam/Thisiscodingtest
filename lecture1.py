#거스름돈 문제 작성자 오지환

n = 1260
count = 0
coin = [500, 100, 50, 10]


for c in coin:
    count += n // c # 1260 // 500 --> 몫 갑을 count에 저장하고 n값을 나눈 c값을 
    n %= c
    
print(count)

결과 
6