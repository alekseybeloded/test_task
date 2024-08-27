import sys


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
    
    return ''.join(map(str, path))


if __name__ == '__main__':
    try:
        array_length = int(sys.argv[1])
        interval_length = int(sys.argv[2])
        
        result = get_path(array_length, interval_length)
        print(result)
    except (ValueError, IndexError) as e:
        print(f'Ошибка: {e}')