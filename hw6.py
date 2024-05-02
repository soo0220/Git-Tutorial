# 사용자 정의 함수부

def input_positive_number(prompt):
    n = 0
    while n <= 0:
        n = int(input(prompt))
    return n

# 주 프로그램부(구구단표)

def display_multiplication_table(start, end):
    for n in range(start, end + 1):
        for i in range(1, 10):
            print(f'{n} * {i} = {n * i :2d}', end='\t')
            if i % 4 == 0:  # 한 줄에 4개의 결과를 출력하면서 탭으로 구분
                print()
        print()  # 한 구구단 출력 후 한 줄 띄우기

# 2단부터 5단까지 출력
display_multiplication_table(2, 5)

# 한 줄 띄우기
print()

# 6단부터 9단까지 출력
display_multiplication_table(6, 9)
