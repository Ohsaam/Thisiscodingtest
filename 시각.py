a = int(input())

count = 0

for i in range(a+1):
    for j in range(60): #분을 의미한다.
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
                
print(count)
