def read_single_digit(n):
    single_digit=['영','일','이','삼','사','오','육','칠','팔','구']
    
    if 0 <= n <= 9:
        return single_digit[n]  
    else:
        return"입력된 숫자는 한 자리 정수가 아닙니다."

def read_number(rn):
    result = ""
    for digit in str(rn):
        result += read_single_digit(int(digit))
    return result

num=int(input('세 자리 정수 입력: '))
korean_number = read_number(num)
print(korean_number)




