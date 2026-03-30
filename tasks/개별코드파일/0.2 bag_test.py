# bag_test.py
# 코드 1.2: Bag을 활용한 테스트 프로그램

from bag import * 

myBag = []

# myBag에 물건 추가
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '빗')
insert(myBag, '손수건')
insert(myBag, '자료구조')
insert(myBag, '야구공')

# '내 가방속의 물건:'과 myBag에 있는 것을 출력할거야.
print('내 가방속의 물건:', myBag)

# '내 가방속의 물건 유무:'과 myBag에 '휴대폰'이 있는지 출력할거야.
print('내 가방속의 물건 유무:', contains(myBag, '휴대폰'))

# '내 가방속의 물건 개수:'과 myBag에 있는 것의 개수를 출력할거야.
print('내 가방속의 물건 개수:', count(myBag))

# 코드 1.4: Bag에 특정 원소가 몇 개 있는지 세는 함수 테스트
print('내 가방속의 휴대폰 개수:', numOf(myBag, '휴대폰'))
print('빗 의 개수:', numOf(myBag, '빗'))
print('야구공 의 개수:', numOf(myBag, '야구공'))
