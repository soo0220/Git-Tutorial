def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False

    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.\n')
    return True

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}\n')

def find(shopping_bag):
    while True:
        print('[검색]')
        item_to_search = input('장바구니에서 확인하고자 하는 상품은? ')
        if item_to_search == '':
            break
        if item_to_search in shopping_bag:
            print(f'{item_to_search}은(는) {shopping_bag[item_to_search]}개 담겨 있습니다.')
        else:
            print(f'{item_to_search}은(는) 장바구니에 없습니다.')

# 주 프로그램 부
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
