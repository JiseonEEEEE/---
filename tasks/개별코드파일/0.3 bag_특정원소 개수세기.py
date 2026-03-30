from bag import insert

# 코드 1.3: Bag에 특정 원소가 몇 개 있는지 세는 함수
def numOf(bag, e) :
    c = 0
    for i in range(len(bag)):
        if bag[i] == e:
            c += 1
    return c

# 테스트를 위한 초기화
myBag = []
insert(myBag, '휴대폰')
insert(myBag, '빗')
insert(myBag, '야구공')
insert(myBag, '야구공')

# 코드 1.4: Bag에 특정 원소가 몇 개 있는지 세는 함수를 활용한 테스트 프로그램
print('내 가방속의 휴대폰 개수:', numOf(myBag, '휴대폰'))

#
print('빗 의 개수:', numOf(myBag, '빗'))
print('야구공 의 개수:', numOf(myBag, '야구공'))
