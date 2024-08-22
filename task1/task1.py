def get_path(array_length: int, interval_length: int) -> str:
    if array_length <=0 or interval_length <= 0:
        return 'Пожалуйста, введите значения больше нуля'
    
    path = []
    current_position = 0
    
    while True:
        path.append(current_position + 1)
        current_position = (current_position + interval_length - 1) % array_length
        if current_position == 0:
            break
    
    path_str = ''.join(map(str, path))
    return f'Полученный путь: {path_str}'


if __name__ == '__main__':
    try:    
        array_length = int(input('Введдите длину массива '))
        interval_length = int(input('Введите интервал длины '))
        result = get_path(array_length, interval_length)
        print(result)
    except ValueError:
        print('Пожалуйста, введите целочисленные значения')