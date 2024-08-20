calls = 0
def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('dixi'))
print(string_info('ora et labora'))
print(is_contains('Olga', ['Olga', 'lga', 'olGa']))
print(is_contains('Ivan', ['iv', 'ivan', 'an']))
print(is_contains('Ivan', ['iv', 'van', 'an']))
print(is_contains('1,2,3',  ['1,2,3', '1', '2', '3']))

print(calls)