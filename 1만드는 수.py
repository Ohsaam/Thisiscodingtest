n,k = map(int,input().split())
#n,k의 값을 받는다. n = 25 k = 5
result = 0

while True:
    Target = (n//k) * k #25
    result += (n-Target)
    n = Target
    
    if n < k:
        break
    
    n //= k # 실질적으로 나누는 부분 
    

result -= (n-1)
print(result)

#O(logN) 걸림 