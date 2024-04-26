def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(radius):
    area=3.14*radius*radius
    return area

radius=get_radius("넓이를 구하고자 하는 원의 반지름은?")

print("반지름",radius,"인 원의 넓이=3.14*",radius,"*",radius,"=",3.14*radius*radius)

#4/26 추가. area를 함수 밖에서 의미있게 활용하고 싶다면

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius * radius
    print('반지름', radius, '인 원의 넓이 = 3.14 *', radius, '*', radius, '=', area)

radius = get_radius('넓이를 구하고자 하는 원의 반지름은?')
get_circle_area(radius)
