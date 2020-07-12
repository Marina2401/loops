def check_petrol(v, pr, kml):
    km = (v*pr/100)*kml
    if km > 200:
        return True, km
    else:
        return False, km


#def km(v, pr, kml):
   # km = (v*pr/100)*kml
    #return km

# #def km2(v, pr, kml):
#     #x = km(v, pr, kml)
#     km2 = (v*pr/100)*kml - 200
#     if km2 >= 0:
#         return 'Можно подождать до следующей заправки'
#     else:
#         return 'Заправьтесь сейчас!!!'


def main():
    v = int(input('Введите объём бензобака '))
    pr = int(input(f'Введите заполненность в процентах '))
    kml = float(input('Введите расход бензина, км на литр '))
    check, km = check_petrol(v, pr, kml)
    print(f'Вы можете проехать ещё {km} км')
    if check:
        print ('Можно подождать до следующей заправки')
    else:
        print('Заправьтесь сейчас')

main()

