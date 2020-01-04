import inputstring
import forward_reverse_print

a=inputstring.input()
direction = input("방향을 선택하세요 / F = 정방향 / R = 역방향 : ")

while True :
    if direction == 'F' or direction =='f':
        forward_reverse_print.forwardprint(a)
        break
    if direction =='R' or direction =='r':
        forward_reverse_print.reverseprint(a)
        break