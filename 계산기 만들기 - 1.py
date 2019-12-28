# 계산기 내에서 사용할 사칙연산 함수 만들기
def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def multiple(a,b):
    return a*b
def divide(a,b):
    return a/b

#계산기 함수 만들기
def caculator():
    try:
        result=int(input('숫자를 입력하세요:')) #첫번째 초기 값
        while True:
            c=str(input('연산자를 입력하세요:'))
            if c == '=':
                print(result)
                break
            else:
                if c=='+':
                    b = int(input('숫자를 입력하세요:'))
                    result=sum(result,b)
                elif c=='-':
                    b = int(input('숫자를 입력하세요:'))
                    result=diff(result,b)
                elif c=='*':
                    b = int(input('숫자를 입력하세요:'))
                    result=multiple(result,b)
                elif c=='/':
                    b = int(input('숫자를 입력하세요:'))
                    result=divide(result,b)
                else: #연산자 이상한거 넣었을 때
                    print("올바른 연산자를 입력해야지요!")
                    break
                print(result)
    except ValueError: #이상한값 넣었을 때, 숫자에 문자 넣었을 때
        print("올바른 값을 넣어야지요!")
    except ZeroDivisionError: #영으로 나누었을 때
        print("0으로 나누면 안되지요 !")
    except: #그 외의 모든 에러
        print("뭔진모르지만 뭔가 잘못한게 분명하다!")

caculator()




