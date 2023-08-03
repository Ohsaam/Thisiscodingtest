data = input()

#첫 번째 문자를 숫자로 변경해서 대입한다.
result = int(data[0])

for i in range(1, len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기 보단 더하기를 수행한다. 
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)


