input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의

step = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인한다.

result = 0

for i in step:
    #이동하고자 하는 위치 확인한다.
    next_row = row + i[0]
    next_column = column + i[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
        
print(result)