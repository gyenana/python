# chapter5. 파이포장하기 : 모듈, 패키지, 

### 5-1.  스탠드얼론 프로그램

- stand-alone[스탠드 얼론]이란 다른 어떤 장치의 도움도 필요 없이 그것만으로 완비된 장치를 의미함
- 따라서 파이썬에서의 스탠드얼론 프로그램이란, .py 파일을 생성하고 호출해서 결과물을 반환하는 것인가

### 5-2.  커맨드 라인 인자

    import sys
    print('program arguments:'sys.argv)
    
    >> sys 를 인자로 받아 리턴 

### 5-3.  모듈과 import 문

- 모듈은 단지 파이썬 코드의 파일
- 코드는 계층구조로 이루어져 있는데 대략 아래와 같음 (책으로 비유하자면)
    - 단어는 데이터 타입
    - 문장은 선언문
    - 단락은 함수
    - 장은 모듈
- import 문 사용 시 다른 모듈의 코드를 참조할 수 있음, 이는 임포트한 모듈의 코드와 변수를 프로그램에서 사용할 수 있게 함
- **5.3.1 모듈 임포트하기**
    - import 문을 이용하면 간단하게 모듈을 임포트 할 수 있음
    - 모듈은 .py 확장자가 없는 파이썬 파일의 이름 ⇒ 예를들어 [report.py](http://report.py) 라면 → report  인 셈
    - 여러개의 모듈을 같은 디렉토리에 저장하고 메인 프로그램에서 호출하면 메인프로그램이 호출한 각 모듈에 접근해서 모듈 내 정의된 함수를 실행한다.
    - 모듈 내 정의된 함수를 호출할  수 있는 방법은 두가지임
        - from 모듈 import 함수
        - import 모듈 return 모듈.함수()
        - 후자를 이용하면 더 분명하게 어떤 것을 호출하는지 알수 있기 때문에 좀 더 안전하지만, 약간의 입력을 더 필요로 함
    - 모듈은 함수 밖에서도 호출할 수 있다. 만일 해당 모듈을 여러 코드에서 사용해야하는 경우, import 문을  함수 밖으로 빼내는 것을 고려해야 한다.
    - 임포트된 코드가 함수 내부에서만 제한되는 경우 내부에 놓는다.

- **5.3.2 다른 이름으로 모듈 임포트 하기**
    - import 모듈 as 별칭
    - 별칭.함수()

- **5.3.3 필요한 모듈만 임포트하기**
    - 모듈의 필요한 부분만 임포트
    - from 모듈 import 필요한 함수

- **5.3.4 모듈 검색 경로**
    - 파이썬은 임포트할 파일을 어디에서 찾을까?
        - 디렉터리 이름의 리스트와 표준 sys 모듈에 저장되어있는 ZIP 아카이브 파일을 변수 path로 사용한다.
    - 이부분의 이해가 좀 더 필요하다 ...

### 5-4. 패키지

- 파이썬 애플리케이션을 좀 더 확장 가능하게 만들기 위해 모듈을 '패키지' 라는 파일 계층 구조에 구성할 수 있음
- 파이썬은 '__init__.py' 파일을 포함하는 디렉터리를 패키지로 간주함 , 이 파일의 내용은 비워도 상관 없음

### 5-5. 파이썬 표준 라이브러리

- 파이썬의 두드러진 점 중 하나는 **배터리 포함** 이라는 철학으로 유용한 작업을 처리하는 많은 표준 라이브러리 모듈이 있는 것
- 이 모듈은 핵심코드가 늘어나는 것을 피하기 위해 분리되어 있음
- 파이썬 코드 작성 시 원하는 기능이 표준 모듈에 있는지 먼저 확인하는 것이 좋으며, 튜토리얼과 함게 모듈에 대한 공식 문서 등을 제공함

- **5.5.1 누락된 키 처리하기 : setdefault() , defaultdict()**
    - 존재하니 않는 키로 딕셔너리에 접근 시 예외가 발생하는데 기본값을 반환하는 딕셔너리의 get() 함수를 사용하면 해당 예외를 피할 수 있다.
    - setdefault() 함수는 get() 함수와 유사하지만, 키가 누락된 경우 누락된 키를 추가, 추가된 키에 값을 할당할 수 있다.

            periodic_table = {'H':1,'H2':2}
            C=periodic_table.setdefault('C',3)
            periodic_table 
            >> {'H':1,'H2':2,'C':3} <- 존재하지 않는 'C' 키에 대해 키를 추가하고 값 할당 

    - 존재하는 키에 다른 기본값을 할당하려 시도 시, 키에 대한 원래 값이 반환되고 적용되지 않는다.
    - defalutdict() 함수도 유사함 , 단 딕셔너리를 생성할 때 모든 새 키에 대한 기본값을 먼저 지정하고, 인자를 함수로 받는다.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edb35f41-4816-49fd-85a8-913f8df732a2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edb35f41-4816-49fd-85a8-913f8df732a2/Untitled.png)

    - defaultdict() 의 인자는 값을 누락된 키에 할당하여 반환하는 함수임 , 즉 존재하지 않는 '키' 에 대해 '기본값'을 할당하여 반환하는 함수
    - 빈 기본값을 반환하기 위해 int() 함수는 정수 0 , list() 는 빈 리스트 ([]) , dict() 는 빈 딕셔너리 ({}) 를 반환함 , 인자를 입력하지 않으면 새로운 키의 초깃값이 None 으로 설정된다.
    - defaultdict() 의 인자에 함수를 받을 수도 있고 lambda 로 함수를 정의할 수도 있음

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdc71392-3d08-4820-b3a0-cb27631c1c56/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdc71392-3d08-4820-b3a0-cb27631c1c56/Untitled.png)

- **5.5.2 항목 세기 : Counter()**
    - 표준 라이브러리에는 항목을 셀 수 있는 함수가 여러 개 존재
    - most_common() : 모든 요소를 내림차순으로 반환, 숫자를 입력하는 경우 그 숫자만큼 상위 요소를 반환
    - 카운터끼리는 +,-,|,& 모두 가능 (합집합,차집합, 교집합, 유니온)
        - & 사용 시, 겹치는 공통항목 중 낮은 수의 공통 항목이 선택되며
        - | 사용 시, 겹치는 공통항목 중 높은 수의 공통항목이 선택된다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5fff599-1663-421b-b279-cc0a0d096422/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5fff599-1663-421b-b279-cc0a0d096422/Untitled.png)

- **5.5.3 키 정렬하기 : OrderedDict()**
    - 딕셔너리는 키 순서와 상관없이 출력됨
    - 그러나 OrderedDict() 함수는 키의 추가 순서를 기억하고, 이터레이터로부터 순서대로 키값을 반환한다.
    - 즉 키의 순서를 인지하고 추가된 키 순서대로 값이 출력됨

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f6a9ec04-0282-440c-949e-f477309ae34b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f6a9ec04-0282-440c-949e-f477309ae34b/Untitled.png)

- **5.5.4 스택 + 큐 == 데크**
    - 데크는 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐
    - 데크는 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때 유용하게 쓰임
    - popleft() 함수는 , 데크로부터 왼쪽 끝의 항목을 제거한 후 그 항목을 반환
    - pop() 함수는 오른쪽 끝의 항목을 제거한 후 그 항목을 반환
    - 인자로 받은 문자열이 양쪽 문자가 서로 일치한다면 단어 중간에 도달할때까지 데크를 pop 한다.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fad59eb9-bcfc-435a-942f-56c7a8b26fb3/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fad59eb9-bcfc-435a-942f-56c7a8b26fb3/Untitled.png)

    - 회문 코드를 좀 더 간단하게 작성하고 싶다면 문자열을 반전해서 비교하면 됨

            def another_palindrome(word):
            	return word == word[::-1] 

- **5.5.5 코드 구조 순회하기 : itertools**
    - itertools 는 특수 목적의 이터레이터 함수를 포함하고 있음
    - for...in 루프에서 이터레이터 함수를 호출할 때 함수는 한번에 한 항목씩 반환하고, 호출 상태를 기억함
    - chain() 함수는 순회 가능한 인자들을 하나씩 반환함
    - cycle() 함수는 인자를 순환하는 무한 이터레이터 → 순서대로 항목 하나씩 반환하되, 한번만 순환하는게 아닌 무한대 순환 (1,2,1,2,1,2,1,2,...)
    - accumulate() 함수는 축적된 값을 계산 , 기본적으로 합계 계산
        - 첫번째 , 첫번쨰+두번쨰 , 첫뻔째+두번째+세번쨰 ...
        - accumulate() 함수의 경우 두번째 인자로 함수를 전달, 축적의 연산을 합계 대신 이 함수로 사용할 수 있음 → 예를 들어 accumulate(값,곱셈)이면 : 1,1*2,1*2*3 ... 이 됨
    - itertools 모듈은 시간을 단축할 수 있는 조합과 순열에 대한 더 많은 함수를 제공함

- 5.5.6 깔끔하게 출력하기 :pprint()
    - print() 함수는 출력 시 정렬 ㄴㄴ
    - pprint() 함수는 가독성을 위해 요소들을 정렬하여 출력

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afd9d894-481c-4456-a7dd-44e41457d002/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afd9d894-481c-4456-a7dd-44e41457d002/Untitled.png)

### 5-6. 배터리 장착 : 다른 파이썬 코드 가져오기

- 표준 라이브러리에 원하는 모듈이 없거나 그 모듈이 예상대로 동작하지 않을때가 있는데
- 파이썬은 전 세계적으로 써드파티 오픈 소스가 있음
    - PyPI
    - github
    - readthedocs
