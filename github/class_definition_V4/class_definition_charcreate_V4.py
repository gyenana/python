import random
import string


class Character :
    def __init__(self,charname):
        #인스턴스 변수에 값 할당
        self.level = 1
        self.charname = charname
        self.classchoice = "초보자"
        self.weapon="주먹"
        self.skill ="후려치기"
        self.attackpower = 10
        self.life = 200
        self.ownmoney=0
    def create_char(self):
        print("{} {} 캐릭터가 생성되었습니다. 레벨은 {} , 클래스는 {} 입니다.".format(self.classchoice,self.charname,self.level,self.classchoice))

    def levelup(self) :
        self.level += 1
        self.life +=15
        self.attackpower+=20
        print("{} {} 캐릭터가 {}레벨이 되었습니다.".format(self.classchoice,self.charname,self.level))
        print("{} {} 캐릭터의 생명력이 {}, 공격력이 {} 로 증가하였습니다.".format(self.classchoice,self.charname,self.life,self.attackpower))

    def attackmonster(self,Monster):
        Monster.life  = Monster.life - self.attackpower
        if Monster.life <= 0 :
            print("막타 {} 데미지로 인해 {}가 사망하여 공격대상이 사라졌습니다.".format(self.attackpower,Monster.name))
        elif Monster.life > 0:
            print("{} {} 캐릭터가 {} 으로 {} 를 시전합니다!!!".format(self.classchoice, self.charname, self.weapon, self.skill))
            print("{}의 생명력이 {} 깎입니다 ! ".format(Monster.name, self.attackpower))

    def jump(self):
        print("{} {} 캐릭터가 점프합니당 ~ ".format(self.classchoice,self.charname))

    def showstatus(self):
        print("캐릭터명 : {} \n레벨 : {} \n클래스 : {} \n생명력 : {} \n공격력 : {} \n보유머니량 : {}"\
              .format(self.charname,self.level,self.classchoice,self.life,self.attackpower,self.ownmoney))

class Warrior(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "전사"
        self.skill = "강하게 내려찍기"
        self.weapon = "대검"
        self.level = character.level
        self.attackpower = character.attackpower+15
        self.life = character.life+150
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
        print("생명력 : {}, 공격력 : {}, 주 무기 : {} , 주요 스킬 : {} 입니다.".format(self.life, self.attackpower, self.weapon,self.skill))

class Knight(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "나이트"
        self.skill = "정권찌르기"
        self.weapon = "한손검"
        self.level = character.level
        self.attackpower = character.attackpower+26
        self.life = character.attackpower+260
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
        print("생명력 : {}, 공격력 : {}, 주 무기 : {} , 주요 스킬 : {} 입니다.".format(self.life,self.attackpower,self.weapon,self.skill))

class Magician(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "매지션"
        self.skill = "벼락치기"
        self.weapon = "스태프"
        self.level = character.level
        self.attackpower = character.attackpower+30
        self.life = character.attackpower+300
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
        print("생명력 : {}, 공격력 : {}, 주 무기 : {} , 주요 스킬 : {} 입니다.".format(self.life,self.attackpower,self.weapon,self.skill))

class Axler(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "액슬러"
        self.skill = "도끼날리기"
        self.weapon = "도까"
        self.level = character.level
        self.attackpower = character.attackpower+21
        self.life = character.attackpower+210
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
        print("생명력 : {}, 공격력 : {}, 주 무기 : {} , 주요 스킬 : {} 입니다.".format(self.life,self.attackpower,self.weapon,self.skill))

class Monster:
    def __init__(self,name,life,attackpower,rewardmoney):
        self.life = life
        self.attackpower = attackpower
        self.name = name
        self.skill = '몸통박치기'
        self.rewardmoney=rewardmoney
    def meetmonster(self,character):
        if attackcount == 1:
            print('{} 가 나타났습니다. 이 몬스터의 생명력은 {} , 공격력은 {} 입니다.'.format(self.name,self.life,self.attackpower))
        elif attackcount > 1 :
            if self.life > 0 :
                print('{} 의 생명력이 {} 남았습니다.'.format(self.name,self.life))
            elif self.life <= 0 :
                print('{} 가 사망하였습니다.보상으로 {} 골드를 얻습니다.'.format(self.name,self.rewardmoney))
                character.ownmoney=character.ownmoney+self.rewardmoney
    def attackchar(self,character):
        print('{}가 {}에게 {}를 시전합니다 ! {}의 생명력이 {} 깎였습니다.'.format(self.name,character.charname,self.skill,character.charname,self.attackpower))
        character.life = character.life - self.attackpower
        if character.life <= 0:
            print('{}가 사망하였습니다.'.format(character.charname))
        elif character.life > 0 :
            print('{}의 생명력이 {} 남았습니다.'.format(character.charname,character.life))




print("======게임 시작!======")
charname = str(input("캐릭터명을 입력하세요: "))
char = Character(charname)
char.create_char()
mon=Monster(("".join([random.choice(string.ascii_uppercase) for _ in range(5)])),random.randrange(100,500,10),random.randrange(5,50,5)\
            ,random.randrange(23,160,2))
attackcount=0
classchoicecount=0


while True:
    print("-------------------------")
    print("1. 전직하기")
    print("2. 레벨업")
    print("3. 공격하기")
    print("4. 점프하기")
    print("5. 내 캐릭터 정보 확인")
    print("Z : 게임 종료 ")
    print("-------------------------")
    a=str(input("원하는 기능을 선택하세요: "))
    print("-------------------------")
    if a=='1':
        classchoicecount+=1
        print("-------------------------")
        print("1. 전사")
        print("2. 나이트")
        print("3. 매지션")
        print("4. 액슬러")
        print("-------------------------")
        b=str(input("원하는 클래스를 선택하세요: "))
        print("-------------------------")
        if classchoicecount == 1 :
            if b=='1':
                char=Warrior(char)
            elif b=='2':
                char = Knight(char)
            elif b=='3':
                char = Magician(char)
            elif b=='4':
                char = Axler(char)
        elif classchoicecount > 1 :
            print("더이상 전직할 수 없습니다. 다른 기능을 선택하세요")
        continue
    elif a=='2':
        char.levelup()
    elif a=='3':
        attackcount += 1
        mon.meetmonster(char)
        if mon.life <= 0:
            mon = Monster(("".join([random.choice(string.ascii_uppercase) for _ in range(5)])),
                          random.randrange(100, 500, 10), random.randrange(5, 50, 5),random.randrange(23,160,2))
            print("현재 몬스터가 사망하였으므로 새 몬스터 {} 가 나타납니다.생명력은 {}, 공격력은 {} 입니다.".format(mon.name,mon.life,mon.attackpower))
        mon.attackchar(char)
        if char.life <= 0 :
            print("{}의 막타 {} 데미지로 {} 캐릭터가 사망하였으므로 게임을 종료합니다.".format(mon.name,mon.attackpower,char.charname))
            break
        char.attackmonster(mon)
    elif a=='4':
        char.jump()
    elif a=='5':
        char.showstatus()
    elif a=='Z' or a=='z':
        print("======게임종료======")
        break


