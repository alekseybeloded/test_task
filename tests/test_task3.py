from task3.task3 import fill_values


def test__fill_values__tests_is_empty(value_data):
    assert fill_values(tests=[], values_dict=value_data) == []

def test__fill_values__values_dict_is_empty(test_data):
    assert fill_values(tests=test_data, values_dict={}) == test_data




def test__fill_values__test_id_in_values_dict(test_data, value_data):
    tests = test_data
    values_dict = value_data

    filled_tests = fill_values(tests, values_dict)

    assert filled_tests[0]['value'] == 'passed'
    assert filled_tests[3]['value'] == 'failed'