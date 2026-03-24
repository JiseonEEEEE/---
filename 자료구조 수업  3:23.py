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

