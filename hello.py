def get_summ(one, two, delimiter='&'):
    answer=(f'{one}{delimiter}{two}')
    return answer.upper()
print(get_summ('Learn','python'))

def format_price(price):
    return int(abs(price))
print(format_price(50.24))    
