from task2.task2 import get_point_position_relative_circle, is_valid_coordinate


def test__get_point_position_relative_circle__distance_squared_less_than_radius_squared():
    assert get_point_position_relative_circle(
        circle_centre=(1, 1),
        circle_radius=6, point=(2, 2)
    ) == '1 - Точка лежит внутри окружности'


def test__get_point_position_relative_circle__distance_squared_more_than_radius_squared():
    assert get_point_position_relative_circle(
        circle_centre=(1, 1),
        circle_radius=6, point=(7, 7)
    ) == '2 - Точка лежит за пределами окружности'


def test__get_point_position_relative_circle__distance_squared_is_equal_to_radius_squared():
    assert get_point_position_relative_circle(
        circle_centre=(1, 2),
        circle_radius=5, point=(5, 5)
    ) == '0 - Точка лежит на окружности'


def test__is_valid_coordinate__is_valid():
    assert is_valid_coordinate(12) is True


def test__is_valid_coordinate__is_not_valid():
    assert is_valid_coordinate(10**39) is False