import math


def get_point_position_relative_circle(
        circle_centre: tuple[int, int],
        circle_radius: int, point: tuple[int, int]
    ) -> str:
    distance_squared = (
        (circle_centre[0] - point[0]) ** 2 +
        (circle_centre[1] - point[1]) ** 2
    )
    radius_squared = circle_radius ** 2
    if distance_squared < radius_squared:    
        return '1 - Точка лежит внутри окружности'
    elif distance_squared > radius_squared:
        return '2 - Точка лежит за пределами окружности'
    else:
        return '0 - Точка лежит на окружности'
    

def is_valid_coordinate(value: int) -> bool:
    return math.isfinite(value) and 10**-38 <= abs(value) <= 10**38


if __name__ == '__main__':
    try:
        with open(input('Введите наименование файла или путь до него '), 'r') as circle_file:
            lines = circle_file.readlines()
            lines = [line.strip() for line in lines]
            circle_centre = tuple(map(int, lines[0].split()))
            circle_radius = int(lines[1])

        if not any(is_valid_coordinate(coord) for coord in circle_centre):
                raise ValueError('Координаты центра окружности не соответствуют диапазону.')

        if not is_valid_coordinate(circle_radius):
                raise ValueError('Радиус окружности не соответствует диапазону.')

        with open(input('Введите наименование файла или путь до него '), 'r') as points_file:
            points = []
            for line in points_file:
                x, y = map(int, line.split())

                if not (is_valid_coordinate(x) and is_valid_coordinate(y)):
                    raise ValueError(f'Координаты точки ({x}, {y}) не соответствуют диапазону.')
                
                points.append((x, y))
            
            if 1 > len(points) or len(points) > 100:
                raise ValueError('Количество точек не соответствует условию')

        for point in points:
            result = get_point_position_relative_circle(circle_centre, circle_radius, point)
            print(result)

    except (ValueError, FileNotFoundError) as e:
        print(f'Ошибка ввода: {e}')