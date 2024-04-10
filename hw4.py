def rep_char(c, n):
    return c * n

def draw_line(line_length):
    print(rep_char('_', line_length))

def draw_line_string(string, line_length):
    print(f'  {string}  ')

def welcome_message(name):
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'

    line_length = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    draw_line(line_length)
    draw_line_string(msg1, line_length)
    draw_line_string(msg2, line_length)
    draw_line(line_length)

name = input("Input his/her name: ")
welcome_message(name)
