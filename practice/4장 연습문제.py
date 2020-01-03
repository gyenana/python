#4.1 연습문제
guess_me = 7
if guess_me <7 :
    print("too low")
elif guess_me>7 :
    print("too high")
else :
    print("just right")

#4.2 연습문제

guess_me = 7
start=1

while True:
    if start < guess_me :
        print("too low")
    if start == guess_me:
        print("found it!")
        break
    if start>guess_me :
        print('oops')
        break
    start+=1

#4.3 연습문제
number_list=[]
number_list=[number for number in range(0,4)]
print(number_list[::-1])

#4.4 연습문제
list_temp=[]
list_temp=[number for number in range(10) if number%2==0]
print(list_temp)

#4.5 연습문지
dict_temp={}
dict_temp = {k:k*k for k in range(10)}
print(dict_temp)

#4.6 연습문제
set_temp={}
set_temp={number for number in range(10) if number%2==1}
print(set_temp)

#4.7 연습문제
gen_temp=()
gen_temp=(number for number in range(10))
for number in gen_temp:
    print('Got',number)


#4.8 연습문제

def good():
    names = ['Harry','Ron','Hermione']
    return names
a=good()
print(a)

#4.9 연습문제 514쪽
def get_odds():
    for n in range(10):
        if n%2==1:
            yield n

gen = get_odds()
print(next(gen))
print(next(gen))
print(next(gen))

#4.10 연습문제 515쪽
def test(argfunc):
    def inner():
        print("hi")
        return argfunc()
    return inner

@test
def start():
    print("start !!")

@test
def end():
    print("End !!")

start()
end()

#4.11 연습문제

#4.12 연습문제
titles=['creature of habit','crewel fate']
plots=['a nun turns into a mon ster','a haunted yarn shop']

movies={}
movies=dict(zip(titles,plots))
print(movies)

