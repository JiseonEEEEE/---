# 코드 1.1: Bag의 주요 연산을 일반함수로 구현 예.
# 리스트를 이용한 가방 구현

def contains(bag, e):
    return e in bag

# 원소 추가
def insert(bag, e):
    bag.append(e)

# 원소 삭제
def remove(bag, e):
    bag.remove(e)

# 원소 개수 반환
def count(bag): 
    return len(bag)

# 특정 원소가 몇 개 있는지 세는 함수 c= count
def numOf(bag, e):
    c = 0
    for i in range(len(bag)):
        if bag[i] == e:
            c += 1
    return c
