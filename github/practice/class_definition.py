# 액슬러 클래스 생성
class axler :
    # init 은 생성자, 별다른 호출이 없어도 액슬러 클래스를 가진 인스턴스 생성
    def __init__(self,charname="unknown"):
        self.level = 0
        self.height = 150
        self.charname = charname
    def create_char(self):
        print(self.charname, " 캐릭터가 생성되었습니다. 레벨은", self.level, " , 신장은 ", self.height, "cm 입니다.")
# 액슬러 클래스 내 선언된 메소드
    def levelup(self) :
        self.level += 1
        print(self.charname," 캐릭터가 ",self.level,"레벨이 되었습니다.")
    def presentlevel(self):
        print("현재",self.charname," 캐릭터의 레벨은 ",self.level,"입니다.")

# 액슬러 클래스를 상속받는 자식 클래스인 액슬러 버전2 생성
class axler_ver2(axler):
    def __init__(self,charname,level):
        #부모 클래스에 정의된 메서드 호출
        super().__init__(charname)
        self.level = level
        print(self.charname, " 캐릭터가 ",self.level,"레벨에서 1차전직 하였습니다 ! ")
    #부모 클래스에 정의된 메서드 오버라이딩
    def presentlevel(self):
        print("1차 전직 후 현재",self.charname,"캐릭터의 레벨은",self.level,"입니다!!")

#char1라는 변수에 레벨 = 0 , 키는 150인 액슬러 인스턴스 할당 (기본값)
char1 = axler("gyenana")
#charname 인자를 넣지 않았을 떄에는 unknown 이라는 기본값이 출력됨
char2 = axler()
# 액슬러 인스턴스가 할당된 char1에 메소드 levelup 적용
char1.levelup()
#자식 클래스 생성 후 변수 넣고 실행
char3=axler_ver2("gyenana",20)
#오버라이딩 실험
char3.presentlevel()

print('----------구분선--------------')
#반복문 사용해서 레벨 업 시키고, 20레벨 도달 시 자식 클래스로 변경
input_charname="nanagye"
mainchar = axler(input_charname)
mainchar.create_char()
while True:
    for newlevel in range(20):
        mainchar.levelup()
    if mainchar.level == 20:
        mainchar = axler_ver2(input_charname, mainchar.level)
        mainchar.presentlevel()
    break



