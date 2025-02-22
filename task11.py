def pos_change(num,curr_pos,target_pos):

    number = 0

    
    for i in range(len(num) - 1, -1,-1):
        number += int(num[i]) * curr_pos ** i
    number = int(str(number)[::-1])
    if target_pos == 10:
        return number
    
        
    
    nashti = 0
    digits = "0123456789ABCDEF"
    res = ""
    while number > 0:
        nashti = number % target_pos
        res += digits[nashti]
        number = number//target_pos
        
    return res
    

num = input("Enter the num: ")
curr_pos = int(input("Enter the current position: "))
target_pos = int(input("Enter the target position: "))

print(pos_change(num,curr_pos,target_pos))