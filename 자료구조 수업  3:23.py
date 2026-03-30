# 코드 1.1: Bag의 주요 연산을 일반함수로 구현 예.
# 리스트를 이용한 가방 구현
def contains(bag, e) :
    return e in bag

# 원소 추가
def insert(bag, e) :
    bag.append(e)

# 원소 삭제
def remove(bag, e) :
    bag.remove(e)

# 원소 개수 반환
def count(bag) : 
    return len(bag)
    
# 코드 1.2: Bag을 활용한 테스트 프로그램
myBag = [ ]

# myBag에 휴대폰 추가
insert(myBag, '휴대폰')

# '내 가방속의 물건:'과 myBag에 있는 것을 출력할거야.
print('내 가방속의 물건:', myBag)

# 'myBag'에 자료구조, 야구공 넣을거고 '내 가방속의 물건:'으로 출력시켜
insert(myBag, '자료구조')
insert(myBag, '야구공')
print('내 가방속의 물건:', myBag)

insert(myBag, '빗')
# '야구공'을 지워버려
remove(myBag, '야구공')
# '내 가방속의 물건:'과 myBag에 있는 것을 출력할거야.
print('내 가방속의 물건:', myBag)
# '내 가방속의 물건 유무:'과 myBag에 '휴대폰'이 있는지 출력할거야.
print('내 가방속의 물건 유무:', contains(myBag, '휴대폰'))
# '내 가방속의 물건 개수:'과 myBag에 있는 것의 개수를 출력할거야.
print('내 가방속의 물건 개수:', count(myBag))

# 코드 1.3: Bag에 특정 원소가 몇 개 있는지 세는 함수
def numOf(bag, e) :
    for i in range(len(bag)):
        if bag[i] == e:
            count = count + 1
    return count

# 코드 1.4: Bag에 특정 원소가 몇 개 있는지 세는 함수를 활용한 테스트 프로그램
print('내 가방속의 물건 개수:', numOf(myBag, '휴대폰'))

#
print('빗 의 개수', numOf(myBag, '빗'))
print('야구공 의 개수', numOf(myBag, '야구공'))

