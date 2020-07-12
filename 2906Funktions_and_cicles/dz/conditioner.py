def reg(t_room, t_cond, reg):
    if reg == 'freeze':
        if t_room > t_cond:
            return t_cond
        else:
            return t_room
    elif reg == 'heat':
        if t_room < t_cond:
            return t_cond
        else:
            return t_room
    elif reg == 'fan':
        return t_room

    elif reg == 'auto':
        return t_cond

def main():
    t_room = int(input('Введите температуру в комнате: '))
    t_cond = int(input('Введите желаемую температуру на кондиционере: '))
    r = str(input('Установите режим: '))
    temperature_in_hour = reg(t_room, t_cond, r)
    print(f'Через час температура будет {temperature_in_hour}')
main()