import input_str
import print_input
import reverse_input

while True :
        result=''
        arg = input_str.input_str()
        b = str(input('입력한 문자열을 출력시킬 방향을 선택하세요./ F(정방향) or R(역방향) : '))
        if b=='F':
            result = print_input.forward_print(arg)
        elif b=='R':
            result = reverse_input.reverse_print(arg)
        break
        print(result)

