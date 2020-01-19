# chapter4. 파이크러스트 : 코드구조

- 파이썬은 프로그램 구조를 정의하기 위해 '공백' 을 사용하는 흔치 않은 언어이다.

### 4-1. 코멘트 달기 : #

- 프로그램에서 코멘트는 인터프리터에 의해 무시되는 텍스트의 한 부분
- 코드를 설명 혹은 나중에 어떤 문제를 고치기 위해 표시하는 등 다양한 목적으로 코멘트를 사용할 수 있음
- #문자를 이용하여 #문자가 시작된곳부터 그 라인의 마지막까지 코멘트를 표시
- 여러 줄의 주석처리를 한꺼번에 하는 것은 파이썬에서 불가 → 따라서 행마다 # 표시 필수
- 문자열 안에 # 있으면 그냥 평범한 문자열로 받아들임

### 4-2. 라인 유지하기 : \

- 한 라인에서 권장하는 최대 문자수는 80자
- 이 길이 안에 코드를 다 표현할 수 없다면 백슬래시 \ 를 입력 후 다음 라인에 코드 계속 작성
- 라인 끝에 \ 입력 시, 다음 라인으로 넘어가더라도 파이썬은 같은 라인으로 인식

### 4-3. 비교하기 : if,elif(else if), else

- if 와 else 는 조건이 참인지 거짓인지 확인하는 파이썬의 선언문
- print() 는 일반적으로 화면에 객체를 출력하는 파이썬의 내장함수
- if 조건 테스트에는 괄호가 필요 없음 , 대신 콜론 : 을 사용, 콜론 사용 안하면 에러남
- 두개 이상의 조건 테스트가 있다면 if, elif , else 를 사용한다.
- 조건을 쓸때는 비교 연산자를 사용하는데, 비교연산자는 아래와 같다
    - ==, ≠ , < , ≤, >,≥,in
- 비교연산자는 부울값 True or False를 반환
- 만약 한번에 여러개의 조건으로 비교해야 한다면, 부울 연산자를 이용 → and, or, not
- 부울 연산자는  비교 연산자보다 우선순위가 낮음 (비교 연산자를 먼저 실행 후 그 다음 부울 연산자 비교)
- 우선 순위에 대한 혼란을 피하기 위해서는 괄호를 추가하면 됨
    - (5>x) and (x<10)
- 또한 파이썬에서는 하나의 변수를 여러번 비교하는 것도 가능 → 5<x<10
- if, elif, else 예시

        furry=True
        small=True
        if furry:
            if small:
                print("It's a cat!") 
            else:
                print("It's a bear!")
        else:
            if small:
                print("It's a skink!")
            else:
                print("It's a Human, Or hairless bear.")
        
        --------------------------------------------------------------------
        color="puce"
        if color=="red":
            print("It's a tomato")
        elif color=="green":
            print("It's a green pepper")
        else:
            print("I've never heard of the color",color) 

- **4.3.1 True 와 False**
    - False 값은 명시적으로 False 할 필요가 없음, 아래 기재한 항목은 모두 false
        - None, 0, 0.0, '', [], (), {}, set()
    - 이외의 다른 것들은 모두 True 로 간주
    - 파이썬 프로그램은 데이터 자료구조가 false 조건인지 확인하기 위해 진실 혹은 거짓의 정의를 사용
        - if small : ← small에 할당된 값이 참이냐 거짓이냐를 확인하는 조건문
    - 변수가 아닌 표현식을 테스트한다면, 파이썬은 표현식을 계산하고 부울 결과를 반환

### 4-4. 반복하기 : While

- 코드를 한번 이상 실행하려면 '루프' 가 필요 → 가장 간단한 루핑 메커니즘은 while 문

- **4.4.1 중단하기 : break**
    - 무한 루프 속에 break 문 사용 시, 일정 조건 하에 반복문을 종료시킬 수 있음
- **4.4.2 건너뛰기 : continue**
    - 반복문을 종료하고 싶지는 않으나, 일부 조건에서 다음 루프로 건너뛰고 싶다면 continue 사용
- **4.4.3 break 확인하기 : else**
    - break 는 어떤 것을 체크하여 그것을 발견했을 경우 종료하는 while 문을 작성할 때 사용한다면,
    - else 는 while 문이 모두 실행되었지만 발견하지 못하였을 때 사용한다.
    - 그냥 break 체커
- 예시 (while)

        count=1
        while True: #무한루프 도는 시작구문 (while 1 : or while "helloworld": 도 됨) 
            count=count+1 #반복할 코드 
            if count==100: #무한루프를 멈출 조건식 
                break #루프 중단 
            if count%2==0: #루프를 건너뛸 조건식 
                continue #루프 건너뜀 
            print(count) # 결과적으로 출력할 내용 
        ------------------------
        numbers=[1,3,5]
        position = 0 
        while position<len(numbers)
            number=numbers[position]
            if number % 2==0:
                print('found even number',number)
                break
            position +=1 
        else:
            print('no even number found') #break 없이 조건에 해당하는 루프를 다 돌았을 때 출력되는 결과 
        ------------------------------
        while True:
            반복할 코드 
            무한 루프를 멈출 조건식 
                break
            루프를 건너뛸 조건식 
                continue
            결과적으로 출력할 내용 

### 4.5 순회하기 : for

- 파이썬에서 이터레이터는 자주 유용하게 쓰임 → 크기, 구현여부와 관계없이 자료구조를 순회할 수 있게 해줌
- 데이터가 메모리에 맞지 않더라도 데이터 스트림을 처리할 수 있도록 허용해줌
- 반복가능한 객체 → 객체 내 요소마다 동일한 행위를 반복하여 적용시킬 수 있음 → 반복가능한 타입으로는 리스트, 문자열, 튜플, range,딕셔너리, 셋이 있음
- 리스트, 튜플의 경우 한번에 한 요소, 문자열의 경우 한번에 한 글자, 딕셔너리의 경우 한번에 하나의 키값에 대해 순회 (딕셔너리의 경우 키대신 value 에 대해 순회하려면 valuse() 사용 / 키와 값을 모두 사용하려면 items() 사용)
- break 와 continue 의 경우 while 과 동일하게 동작함
- **4.5.3 break 확인하기 : else**
    - for 문에서도 마찬가지로 모든 항목을 순회했는지 확인하는 부가적인 옵션의 else 문 존재
    - for 문에서 break 문이 호출되지 않으면 else 문이 실행됨 → 즉 break 문에 의해 반복문이 중단되었는지 확인하는 것
- 예시(for)

        rabbits=['Flopsy','Mopsy','Cottontail','Peter']
        current=0
        while current<len(rabbits):
            print(rabbits[current])
            current+=1
        과 동일한 결과물을 반환하는 for 문을 작성해보면, 아래와 같음 
        
        for rabbit in rabbits:
            print(rabbit)
        좀 더 간결하고 파이써닉함
        
        #else 구문 이용하기
        cheeses=[]
        for cheese in cheeses:
            print('this cheese shop has a lovely',cheese) 
        else:
            print('''there's no cheese''')   
        -> 이 경우 빈 리스트를 할당하였기 때문에 else 하위의 문장이 출력됨 

- **4.5.4 여러 시퀀스 순회하기 :zip()**
    - zip()함수 이용 시, 여러 시퀀스를 병렬로 순회할 수 있음
    - 여러 시퀀스 중 가장 짧은 시퀀스가 순회를 완료하면 그 순간 zip() 은 멈춤
    - zip() 함수로 여러 시퀀스를 순회하며 동일한 오프셋에 있는 항목으로부터 튜플을 만들 수 있다.
    - zip()에 의해 반환되는 값은 튜플이나 리스트 자신이 아니라 하나로 반환될 수 있는 순회 가능한 값이다
    - 예시

            english='monday','tuesday','wednesday'
            french='lundi','mardi','mercredi'
            
            list(zip(english,french)) 
            -> [('monday','lundi'),('tuesday','mardi'),('wednesday','mercredi')] 
            
            dict(zip(english,french))
            -> {'monday':'lundi','tuesday':'mardi','wednesday':'mercredi'} 
            

- **4.5.5 숫자 시퀀스 생성하기 : range()**
    - range() 함수는 리스트나 튜플같은 자료구조를 생성하여 저장하지 않더라도 특정 범위내에서 숫자 스트림을 반환함 (스트림이란, → 방향으로 흐르는 것을 말하는 듯)
    - 이는, 컴퓨터의 메모리를 전부 사용하지 않고 프로그램의 충돌없이 아주 큰 범위를 생성할 수 있게 해줌
    - range(start,stop,step) 형태로 사용하며 start의 기본값은 0, step의 기본값은 1이다
        - stop은 꼭 입력해야하는 값이며 숫자 스트림의 범위는 start부터 stop-1까지이다.
        - step에 -1 지정시 끝에서부터 역방향으로 호출
    - zip() 과 range() 같은 함수는 순회가능한 객체를 반환 (리스트, 튜플, 문자열등)
    - 그러므로 for ~ in 형태로 값을 순회시킬 수 있으며 객체를 리스트와 같은 시퀀스로 변환시킬 수 있다.
    - 예시

            for number in range(0,6):
                print(number) 
            
            0
            1
            2
            3
            4
            5

### 4.6  컴프리헨션

- 컴프리헨션(함축) 은 하나이상의 이터레이터로부터 파이썬의 자료구조를 만드는 콤팩트한 방법
- 비교적 간편한 구문으로 반복문과 조건테스트를 결합할 수 있도록 해줌
- 컴프리헨션 사용 시, 리스트나 딕셔너리, 셋트와 같은 데이터 형 표기 내에 코드를 압축, 기술하여 새로운 데이터형을 만들 수 있음

- **4-6-1 리스트 컴프리헨션**
    - [표현식 for 항목 in 순회가능한 객체]
    - 다시 말하면 ⇒ [출력할 값 for 목록에 대한 값(객체를 이룰 하나하나의 항목) in 순회가능한 객체]
    - 리스트 컴프리헨션은 조건표현식도 포함 가능
        - [표현식 for 항목 in 순회가능한 객체 if 조건]
    - 또한, 루프도 중첩될 수 있듯, 리스트 컴프리헨션 내 조건절도 중첩하여 사용 가능함
    - 예시

            # 리스트 컴프리헨션으로 정수 리스트 만들기 
            number_list = [number for number in range(1,6)] 
            
            #리스트 컴프리헨션으로 정수 리스트를 만들되 짝수만 나오도록 
            number_list = [number for number in range(1,6) if number % 2 == 0] 
            
            #컴프리헨션 사용 시, while 문이나 for 문을 이용해 출력한 것보다 간결함 
            
            #리스트 컴프리헨션에 중첩된 조건문 사용 
            rows=range(1,4) 
            cols=range(1,3) 
            cells=[(row,col) for row in rows for col in cols] 
            for cell in cells:
                print(cell) 
            
            (1,1)
            (1,2)
            (2,1)
            (2,2)
            (3,1)
            (3,2)  
            
            #언패킹한 값을 얻으려면, 
            for row,col in cells:
                print(row,col) 
            1 1
            1 2
            2 1
            2 2 
            3 1
            3 2 

- **4-6-2 딕셔너리 컴프리헨션**
    - {키_표현식 : 값 표현식 for 표현식 in 순회가능한 객체}
    - 예시

            word='letters'
            letter_counts={letter:word.count(letter) for letter in word}
            letter_counts
            
            {'l':1, 'e':2, 't':2, 'r':1, 's':1} 

- **4.6.3 셋 컴프리헨션**
    - {표현식 for 표현식 in 순회가능한 객체}
    - a_set = {number for number in range(1,6) if number%3==0}
- **4.6.4 제너레이터 컴프리헨션**
    - 튜플은 컴프리헨션이 없다, 대신 소괄호로 컴프리헨션 하면 제너레이터임
    - 제너레이터 컴프리헨션은 제너레이터 객체를 반환하며,
    - 제너레이터는 이터레이터에 데이터를 제공하는 하나의 방법이다
    - 제너레이터는 한번만 실행 가능하며, 별도의 메모리에 저장되지 않는다. 즉석에서 그 값을 생성하며 이터레이터를 통해 값을 한번에 하나씩 처리한다.

### 4.7 함수

- 함수는 코드의 재사용을 위한 것, 함수는 입력 매개변수로 모든 타입을 여러개 취할 수 있으며 반환 값으로 모든 타입을 여러개 반환할 수 있다
- 함수의 2가지 역할은 → 정의하기 / 호출하기
- 파이썬 함수를 정의하기 위해서는 def 와 함수이름, 괄호를 입력함
- 괄호 안에는 옵션으로 매개변수를 입력할 수 있으며, 마지막에는 콜론 : 을 붙인다. → 매개변수는 없어도 되는데 콜론은 필수임 !!
- 함수명은 변수명과 동일한 규칙으로 작성한다.

    #함수 만들기
    def joinee(anything(매개변수)): #함수 정의 
        return anything+'@@'+anything #반환될 값 
    print(joinee("hohoho")) #매개변수에 'hohoho'(인자)  대입, joinee() 실행 
    
    hohoho@@hohoho
    
    def 함수명(매개변수):
        return 결과로 출력될 값 
    
    함수명(인자) -> 인자를 함수에 대입하여 결과 출력 

- 함수의 인자는 갯수에 상관없이 모든타입의 인자를 취할 수 있다.
- 반환값도 마찬가지로 개수에 상관없이 모든 타입을 반환할 수 있다.
- 함수가 명시적으로 return 을 호출하지 않으면 호출자는 반환값으로 None 을 얻는다.

- **None 이란?**
    - None은 아무것도 없다는 것을 뜻하는 파이썬의 특별한 값
    - None 은 false 와는 다름
    - 값이 None 이냐는 것에 대해서는 참과 거짓을 판단할 수 있지만 None 자체에 대해 참과 거짓을 판단할 수 없음
    - 즉, 빈 딕셔너리, 빈 리스트, 빈 문자열, 빈 튜플, 0, 0.0 과는 다르다.

- **4.7.1 위치 인자**
    - 파이썬은 다른 언어에 비해 함수의 인자를 유연하고 독특하게 처리
    - 인자의 가장 익숙한 타입은 **값을 순서대로 상응하는 매개변수에 복사**하는 위치인자
    - 예시

            def menu(wine, entree, dessert):
                return{'wine':wine, 'entree':entree, 'dessert':dessert}
            
            menu('chardonay','chicken','cake')
            -> {'wine' : 'chardonay','dessert':'cake','entree':'chicken'} 
            #결과값으로 출력될 때 위치 순서 지정 없음 
            #인자가 입력된 순서대로 각 값에 순서대로 대입 

    - 위치 인자의 단점은 각 위치의 의미를 알아야 값이 제대로 위치에 대입된다는 것

- **4.7.2 키워드 인자**
    - 위치인자는 각 위치별로 의미를 알아야했다면, 키워드 인자의 경우 매개변수에 상응하는 이름을 인자에 지정할 수 있다.
    - 매개변수에 직접 인자를 할당하는 개념인 것 같다.
    - 심지어 인자를 함수의 정의와 다른 순서로 지정할 수 있다.
    - 위치 인자와 키워드 인자를 함께 쓸 수도 있다. 위치 인자와 키워드 인자로 함수를 호출한다면, 위치 인자가 먼저 와야한다.
    - 예시

            menu(entree='beef',wine='chardonay',dessert='cake') 
            #함수 내 각 매개변수별로 직접 인자 할당
            -> {'wine' : 'chardonay','dessert':'cake','entree':'beff'}
            
            menu('chardonay',dessert='cake',entree='beef') 
            #함수 내 위치인자와 키워드 인자 둘다 사용, 단 위치인자를 키워드인자보다 먼저 호출  
             -> {'wine' : 'chardonay','dessert':'cake','entree':'beff'}

- **4.7.3 기본 매개변수값 지정하기**
    - 매개변수에 기본값 지정 가능, 호출자가 대응하는 인자를 제공하지 않으면 기본값을 사용
    - 함수 정의 시, 매개변수에 기본값을 지정하여 만들면 인자가 없어도 걍 그 기본값을 반환한다
    - 예시

            def menu(wine,entree,dessert='icecream')
                return {'wine':wine,'entree':entree,'dessert':dessert}
            
            #디저트에 아이스크림이라는 기본값 지정 
            #함수 호출 시 디저트에 대한 인자값이 없다면 아이스크림이 반환 
            #기본값 지정은 함수를 정의할 때만 가능하다 

- **4.7.4 위치인자 모으기 : ***
    - '*' : 애스터리스크
    - 애스터리스크 사용 시, 함수 내 매개변수에서 위치인자 변수들을 튜플로 한데 묶는다.
    - 즉, 인자를 모두 언패킹하여 한꺼번에 함수에 던지는 개념인 듯
    - 가변인자를 사용하는 print() 와 같은 함수에서는 아주 유용
    - 또한 함수에 위치인자 몇개 지정 나머지는 애스터리스크를 통해 한꺼번에 모두 취하게 할 수도 있음
    - 예시

            def print_more(require1,requere2,*args)
                print('need this one':require1)
                print('need this one too':require2)
                print('all the rest':*args) 
            
            print_more('cap','gloves','scarf','monocle','mustache wax') 
            
            need this one : cap 
            need this one too : gloves
            all the rest : ('scarf','monocle','mustache wax') 
            # *args 인자에 대해서는 변수들을 한데 튜플로 묶어 반환 

- **4.7.5 키워드 인자 모으기 : ****
    - 키워드 인자를 딕셔너리로 묶기 위해서는 ** 사용 → 두개의 애스터리스크를 사용하는 이유는, 키워드 인자의 경우 딕셔너리 형태로 묶이는데 애스터 리스크를 1개만 사용하면 '키'만 묶임, 따라서 키와 값을 모두 묶기 위해서 두개의 애스터리스크가 필요함
    - 예시

            def print_kwargs(**kwargs):
                print('keyword arguments':kwargs)
            
            print_kwargs(wine='merlot',entree='mutton',dessert='macaron')
            
            -> keyword arguments: {'dessert':'macaron','entree':'mutton','wine'='merlot'}
             

    - 위치 매개변수와 *args, **kwargs 를 섞어 사용하려면, 이들을 순서대로 배치해야한다
        - 위치매개변수 → *args → **kwargs

- **4.7.6 docstring**
    - 파이썬의 철학 중 '가독성은 중요하다' 라는 구절이 있음
    - docstring 은 함수 정의 중 그 함수에 대한 설명을 문자열로 포함시키는 것을 말함
    - docstring 은 길게 작성할 수 있으며 서식을 추가할 수도 있음
    - 함수의 docstring을 보려면 help(함수) 하면 됨

- **4.7.7 일등시민 : 함수**
    - **모든 것이 객체다 라는 파이썬의 철학은 파이썬의 만트라이기도 함**
    - 객체는 숫자, 문자열, 튜플, 리스트, 딕셔너리 그리고 함수를 포함한다.
    - 파이썬에서 함수는 일등시민이다. 이는
        - 함수를 변수나 데이터에 할당할 수 있으며
        - 함수를 객체의 인자로 넘길 수 있으며
        - 함수를 객체의 리턴값으로 리턴할 수 있다는 것이다.
    - 이와 같이 파이썬은 몇몇 다른 언어에서는 불가능한 기능을 제공한다.

    [일등시민: 함수 ](https://www.notion.so/bc7e9ec1e7d44e488f41f78ceaa82e40)

    [first-class citizen(일등 시민)](https://www.notion.so/first-class-citizen-34a1c4f961dd4d8d8b68743748928b7f)

- **4.7.8 내부함수**
    - 내부함수로 함수 내 또다른 함수 정의 가능
    - 내부 함수는 루프나 코드 중복을 피하기 위해 또다른 함수 내에 어떤 복잡한 작업을 한번 이상 수행할 때 유용하게 사용됨

        def outer(a,b):
        	def inner(c,d):
        			return c+d 
        	return inner(a,b) <- 함수를 리턴값으로 호출 (함수 = 일등시민) 

- **4.7.9 클로져(closure)**
    - 내부함수는 클로져처럼 행동할 수 있음
    - 클로져는 다른 함수에 의해 동적으로 생성되며 바깥함수로부터 생성된 변수값을 변경, 저장할 수 있음
    - 클로져는 중첩함수 구조에서 내부 함수의 지연 실행을 위해 저장된 정보를 의미

        def outer:
        	msg="Hello,Python!"
        	def inner: #내부 함수 선언 
        		print(msg) #내부함수의 리턴값 
        	return inner #outer 함수에 대해 inner 함수의 함수명을 호출 
        
        res=outer() #outer함수 호출 -> 'inner'라는 함수명이 결과 (함수 일등시민, 변수에 할당) 
        res() 
        #res에 inner 라는 함수명이 할당되었고, 그에 따라 res()=inner()
        #따라서 위에서 선언한 inner()가 실행됨 
        #원래 함수는 함수를 벗어나면 함수 내 선언된 값에 대해 저장되지 않았으므로 결과값이 호출  ㄴㄴ 
        #그러나 이 경우 상단에서 선언한 msg 값이 출력되는데, 이는 중첩함수 구조에서 실행되지 않은 내부함수에 대해 
        #이 내부함수가 나중에 실행될 수 있도록 실행에 필요한 내용에 대해 저장하고 있기 때문 
        #이때 내부함수를 위해 저장되어있는 정보를 클로져라고 함 
        #따라서 res에 inner 함수를 할당한 후 inner 함수가 실제적으로 outer함수를 벗어났음에도 불구하고
        #결과값이 출력될 수 있었던 이유는, inner함수를 위한 클로져가 생성되었기 때문 
        res()
        
        --결과--
        Hello,Python!
        Hello,Python!

- **4.7.10 익명함수 : lambda()**
    - 람다함수는 단일문으로 표현되는 익명함수
    - 별도의 함수 이름을 할당하여 함수를 정의하는 것이 아니라 실행될 내용 그자체를 바로 기록
    - 람다함수는 복잡한 식을 반복적으로 사용하거나, 함수에 식을 인수로 전달할 때 사용 (코드가 간결해짐)
    - 람다는 많은 작은 함수를 정의하고, 이들을 호출해서 얻은 모든 결과값을 저장해야하는 경우에 유용함, 특히 콜백함수를 정의하는 그래픽 유저 인터페이스에서 람다를 사용할 수 있음

        def edit_story(words,func):
        	for word in words:
        		print(func(word))
        
        stairs=['thud','meow','thud','hiss']
        
        def enliven(word):
        	return word.capitalize()+'!' 
        
        edit_story(stairs,enliven)
        
        >>>>결과 
        
        Thud!
        Meow!
        Thud!
        Hiss! 
        
        위 함수를 람다 이용한다면? 
        
        edit_stroy(stairs,lambda word:word.capitalize()+'!') 
        #별도의 enliven 함수의 정의 없이 하고자 하는 바를 직접 edit_story 함수 내에 정의 
        #람다의 콜론과 닫는 괄호 사이에 있는 것이 함수의 정의 부분 
        > 상단과 동일한 결과 출력 

### **4.8 제너레이터**

- 제너레이터는 파이썬의 시퀀스를 생성하는 객체로, 전체 시퀀스를 한번에 메모리에 생성하고 정렬할 필요없이 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
- 제너레이터는 이터레이터에 대한 데이터 소스로 자주 사용된다.
- 제너레이터의 대표적인 예시는 range() 함수가 있다. (일련의 정수 생성)
    - 파이썬2의 range()는 메모리에 제한적인 리스트를 반환했다면, 파이썬2의 xrange()가 현재 파이썬 3의 range() 이다.
- 제너레이터는 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음값을 반환
    - 일반함수의 경우 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫번째 라인부터 수행한다.
- **제너레이터 함수의 경우 return 이 아니라 yield 문으로 값을 반환한다.**
- 정리하면, 제너레이터는 이터레이터와 유사하게 함수를 회차별로 실행시키는 개념
    - 이터레이터는 항목별로 하나씩 실행시킴 , next() 사용
    - 제너레이터는 즉 함수계의 이터레이터 , 함수 호출 시 전체 실행 ㄴㄴ next() 로 회차별 실행
- **제너레이터는 제너레이터 함수로 생성하며, yield 문으로 실행 결과 반환 후, 함수의 실행을 일시중지 시킴, 이후 함수 바깥에서 next() 함수 실행 시, 멈춘 지점 이후 부터 함수 실행**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab5d26fe-bc13-47a1-abd4-303a70c11505/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab5d26fe-bc13-47a1-abd4-303a70c11505/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/743c469e-8546-4e34-8549-24ad22912760/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/743c469e-8546-4e34-8549-24ad22912760/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d1e3349-1e82-4770-ab76-e6f34eea6a4e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d1e3349-1e82-4770-ab76-e6f34eea6a4e/Untitled.png)

<참고 : 이터레이터> 

- 이터러블객체 : 리스트, 튜플, 딕셔너리, 세트, 문자열, range() (한번에 한개씩 값을 반환할 수 있는 객체)
- 이터러블인지 확인하기 위해서는 dir() 함수를 이용, "__iter__" 메소드 존재 여부 확인
- 이터러블 객체에 대해 iter() 함수 적용 시, 이터레이터로 변환이 가능하며, 변환된 이터레이터에 대해 next() 함수로 이터레이터 내 값에 대해 순서대로 한개씩 반환 가능함

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f453dcf9-e83a-4105-b9bc-0bfff397b9b0/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f453dcf9-e83a-4105-b9bc-0bfff397b9b0/Untitled.png)

- for 문의 경우 내부적으로 "__iter__" 메소드와 "__next__" 메소드로 변환되어 실행되며 사실상 내부적으로 이터레이터를 생성하고 사용하는 프로세스를 가짐, 반복 횟수를 별도 지정하지 않으면, 자동으로 이터러블을 구성하고 있는 항목의 갯수 만큼 반복 실행함

### 4.9 데커레이터

- 데커레이터는 하나의 함수를 취해서 또 다른 함수를 반환하는 함수
- 기존의 함수에 기능을 추가해주는 함수를 의미한다. → 기존 함수를 수정하지 않고 새 기능을 추가
    - 일반적인 예시로는 함수에 전달된 인자를 보기위해 디버깅문을 추가하는 것
- 데커레이터 함수는 일급함수와 클로져를 기반으로 구성됨
- 데커레이터를 사용하기 위해서는 아래와 같은 내용을 사용
    - *arg(위치인자), **kwargs(키워드인자)
    - 내부함수
    - 함수 인자

    < 수동으로 데커레이터 할당 > 
    def decorator_function(original_function): #함수 선언 1
        def wrapper_function(): #내부 함수 선언 5
            return original_function() #인자로 받은 함수를 리턴값으로 7 
        return wrapper_function #내부 함수를 리턴값으로 6
     
    def display(): #별도의 함수 선언 2
        print("display 함수가 실행됐습니다") #8
     
    decorated_display = decorator_function(display) #display 함수를 인자로 전달 3
    # -> decorator_function(display) => display 
    decorated_display() #함수 실행 / display 함수를 인자로 받음 /클로져 개념 4
    #-> display() 와 동일 
    
    >>결과 
    
    display 함수가 실행됐습니다
    
    위의 코드는 다음과 같은 내용입니다.  
    데코레이터 함수인 decorator_function과 일반 함수인 display를 
    #1과 #2에서 각각 정의를 하였습니다. 
    그 다음에 #3에서 decorated_display라는 변수에 display 함수를 인자로 갖은 
    decorator_function을 실행한 리턴값을 할당하였습니다. 
    물론 이 리턴값은 wrapper_function이 되겠죠. 여기서 wrapper_function 함수는 아직 실행된게 아닙니다.
     decorated_display 변수 안에서 호출되기를 기다리는 겁니다. 
    그리고 #4의 decorated_display()를 통해 wrapper_function을 호출하면 
    #5번에서 정의된  wrapper_function이 호출이 됩니다. 
    그러면 #7에서 original_function인 display 함수가 호출되어 
    #8의 print 함수가 호출되고 문자열이 출력되는 겁니다.
    
    < 다른 방법으로 데커레이터 할당 > 
    def decorator_function(original_function): #함수 선언 1
        def wrapper_function(): #내부 함수 선언 5
            return original_function() #인자로 받은 함수를 리턴값으로 7 
        return wrapper_function #내부 함수를 리턴값으로 6
    
    @decorator_function 
    def display(): #별도의 함수 선언 2
        print("display 함수가 실행됐습니다") #8
     
    display() 

- 참고 링크
    - [https://blog.naver.com/pisibook/221702736595](https://blog.naver.com/pisibook/221702736595)
    - [http://schoolofweb.net/blog/posts/파이썬-데코레이터-decorator/](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/)
- 여러개의 데커레이터 존재 시, 함수에서 가장 가까운 데커레이터를 먼저 실행한 후 그 위에 데커레이터가 실행된다.

### 4.10 네임스페이스와 스코프

- 이름은 사용되는 위치에 따라 다른 것을 참조할 수 있음, 파이썬은 다양한 네임스페이스가 있음
- 네임스페이스는 특정 이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계가 없는 것을 말함
- 네임스페이스란, **프로그래밍 언어에서 특정한 객체(Object)를 이름(Name)에 따라 구분할 수 있는 범위를 의미한다. 파이썬 내부의 모든것은 객체로 구성되며 이들 각각은 특정 이름과의 매핑 관계를 갖게 되는데 이 매핑을 포함하고 있는 공간을 네임스페이스라고 한다.**

네임스페이스가 필요한 이유는 다음과 같다. 프로그래밍을 수행하다보면 모든 변수 이름과 함수 이름을 정하는 것이 중요한데 이들 모두를 겹치지 않게 정하는 것은 사실상 불가능하다.

> 따라서 프로그래밍언어에서는 네임스페이스라는 개념을 도입하여, 특정한 하나의 이름이 통용될 수 있는 범위를 제한한다. 즉, 소속된 네임스페이스가 다르다면 같은 이름이 다른 개체를 가리키도록 하는 것이 가능해진다.

- 네임스페이스는 아래와 같이 분류 가능
    - 전역 네임스페이스 : 전역 변수
    - 지역 네임스페이스 : 함수나 메소드 내 존재, 함수 내 지역변수
    - 빌트인 네임스페이스 : 기본 내장 함수 및 예외 함수 존재
- 전역변수의 경우 함수 내에서 값을 변경 시도 시, 에러가 나타남, 함수 내에서 전역 변수에 접근하기 위해서는 global 키워드를 사용해서 전역 변수의 접근을 명시해야 함 (파이썬의 철학 : **명확한 것이 함축적인 것보다 낫다.)**
    - global 키워드를 사용하지 않으면 함수 내에서 전역 변수 접근이 불가하며, 동일한 이름의 지역변수에 접근함
- 파이썬은 네임스페이스의 내용을 접근하기 위해 두가지 함수를 제공
    - local() : 지역 네임스페이스의 내용이 담긴 딕셔너리를 반환 (네임스페이스는 딕셔너리 형태로 구현)
    - global(): 전역 네임스페이스의 내용이 담긴 딕셔너리를 반환
- 참고 링크 : [https://hcnoh.github.io/2019-01-30-python-namespace](https://hcnoh.github.io/2019-01-30-python-namespace)

- **4.10.1 이름에 _와 __사용**
    - 두 언더스코어(__) 로 시작하고 끝나는 이름은 파이썬 내의 사용을 위해 예약되어 있음
    - 그러므로 변수 선언 시 두 언더스코어 사용 안됨

### 4.11 에러 처리하기 : try, except

- 일부 언어에서 에러는 특수 함수의 반환값으로 표시, 파이썬에서는 관련 에러가 발생할 때 실행되는 코드인 '예외' 사용
- 모든 잠재적인 에러를 방지하기 위해 적절한 예외처리가 필요함
- 예외 처리에 대한 핸들러를 제공하지 않으면, 파이썬은 에러 메시지와 오류가 발생한 위치에 대한 정보 출력 후 프로그램 종료시킴
- 따라서, 에러가 예상되는 코드에 try 문을 사용하고 그 에러를 처리하기 위해 except을 사용

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4712fab9-31ef-473d-a8f2-f5aaae79bbf8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4712fab9-31ef-473d-a8f2-f5aaae79bbf8/Untitled.png)

- except 만 기술하고 예외 이름에 대해 별도 지정하지 않으면 모든 에러에 대해 예외 처리한다는 의미 (포괄적인 예외 처리)
- 예외 타입을 넘어 예외 사항에 대한 세부 정보를 얻고싶다면 아래와 같이 변수에 에러 내용 저장
    - except 예외타입 as 이름

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/409b233b-bb82-4996-903b-703e264edc54/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/409b233b-bb82-4996-903b-703e264edc54/Untitled.png)

    - as 뒤 이름(변수명) 은 파이썬이 보내는 에러 메시지를 저장함, 따라서 해당 변수에 대해 print() 함수 실행 시 파이썬이 보내는 에러 사항에 대해 확인할 수 있음
- 각종 예외 타입
    - IndexError : 시퀀스에서 잘못된 위치를 입력할 때 발생하는 예외 타입
    - ZeroDivisionError : 0으로 나눴을 때 생기는 예외타입
    - ValueError : 값을 잘못 넣었을 때 생기는 예외타입 (int 인데 string 입력)

### 4.12 예외 만들기

- 파이썬에서 이미 정의되어 있는 예외와 별도로 본인이 필요한 예외에 대해 직접 해당 예외에 대한 예외 타입을 정의할 수 있음
- 새로운 예외타입을 정의하려면 '클래스' 객체 타입을 정의해야 함
- [https://python.bakyeono.net/chapter-9-4.html#944-예외-유형-정의하기](https://python.bakyeono.net/chapter-9-4.html#944-%EC%98%88%EC%99%B8-%EC%9C%A0%ED%98%95-%EC%A0%95%EC%9D%98%ED%95%98%EA%B8%B0)

[별도 . 포인터란? ](https://www.notion.so/cbfc5bfb642a4bb9afa770235b46f1bc)
