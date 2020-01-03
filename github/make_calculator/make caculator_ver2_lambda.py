# 계산기 함수 만들기
def caculator():
    try:
        result = int(input('숫자를 입력하세요:'))  # 첫번째 초기 값
        while True:
            c = str(input('연산자를 입력하세요:'))
            if c == '=':
                print(result)
                break
            else:
                if c == '+':
                    b = int(input('숫자를 입력하세요:'))
                    result = (lambda inputA, inputB: inputA + inputB)(result, b)
                    # 앞에서는 def 로 했던 부분을 람다로 대체
                    # 람다 함수의 값을 result 변수에 새롭게 할당
                elif c == '-':
                    b = int(input('숫자를 입력하세요:'))
                    result = (lambda inputA, inputB: inputA - inputB)(result, b)
                elif c == '*':
                    b = int(input('숫자를 입력하세요:'))
                    result = (lambda inputA, inputB: inputA * inputB)(result, b)
                elif c == '/':
                    b = int(input('숫자를 입력하세요:'))
                    result = (lambda inputA, inputB: inputA / inputB)(result, b)
                else:
                    print("올바른 연산자를 입력해야지요!")
                    break
                print(result)
    except ValueError:
        print("올바른 값을 넣어야지요!")
    except ZeroDivisionError:
        print("0으로 나누면 안되지요 !")
    except:
        print("뭔진모르지만 뭔가 잘못한게 분명하다!")


caculator()
