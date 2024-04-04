discounted_rate=0

def set_discounted_rate(rate):
    global discounted_rate
    discounted_rate=rate

def get_fixed_price(d_price):
    return d_price / (1-(discounted_rate /100))

def main():
    set_discounted_rate(int(input('할인율은?')))

    a_d_price=int(input('A 상품의 할인된 가격은?'))
    a_fixed_price= get_fixed_price(a_d_price)
    print('A 상품의 정가는',int(a_fixed_price),'원')

    b_d_price=int(input('B 상품의 할인된 가격은?'))
    b_fixed_price= get_fixed_price(b_d_price)
    print('B 상품의 정가는',int(b_fixed_price),'원')


if __name__== '__main__':
    main()
