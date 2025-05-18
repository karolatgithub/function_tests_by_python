from name_function import get_formattes_name

print('Wpisz q aby zakonczyc program')
while True:
    first=input('podaj imie: ')
    if first=='q':
        break

    last=input('podaj nazwisko: ')
    if first=='q':
        break

    formatted_name=get_formattes_name(first, last)
    print(f'eleganckie imie i nazwisko: {formatted_name}.')
