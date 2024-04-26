def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(amount):
    coin_counts = {'500원': 0, '100원': 0, '50원': 0, '10원': 0}

    coin_counts['500원'], amount = divmod(amount, 500)
    coin_counts['100원'], amount = divmod(amount, 100)
    coin_counts['50원'], amount = divmod(amount, 50)
    coin_counts['10원'] = amount // 10

    return coin_counts

amount = get_integer("동전으로 교환하고자 하는 금액은? ")
coin_counts = exchange(amount)

print("500원 동전의 개수:", coin_counts['500원'])
print("100원 동전의 개수:", coin_counts['100원'])
print("50원 동전의 개수:", coin_counts['50원'])
print("10원 동전의 개수:", coin_counts['10원'])
#n500=money//500, money=money %500 순서,반복 후 print('500원동전개수:',n500)반복
#def get_integer(prompt):
#res = int(input(prompt))
#return res
#money =get_integer('동전교환액?')
#exchange(money)
