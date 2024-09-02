from task1.task1 import get_path
import pytest


@pytest.mark.parametrize(
        'array_length, interval_length, expected_result',
        [
            pytest.param(
                0,
                3,
                'Пожалуйста, введите значения больше нуля',
                id='array length is equal to zero',
            ),
            pytest.param(
                3,
                0,
                'Пожалуйста, введите значения больше нуля',
                id='interval length is equal to zero',
            ),
            pytest.param(
                0,
                0,
                'Пожалуйста, введите значения больше нуля',
                id='array length and interval length is equal to zero',
            ),
        ],
)
def test__get_path__array_length_or_interval_length_is_equal_to_zero(
    array_length,
    interval_length, expected_result
):
    assert get_path(array_length, interval_length) == expected_result


def test__get_path__array_length_or_interval_length_is_more_than_zero():
    assert get_path(array_length=3, interval_length=5) == '123'

