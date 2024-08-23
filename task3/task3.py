import json
from typing import Any


def fill_values(tests: list[dict[str, Any]], values_dict: dict[int, str]) -> list[dict[str, Any]]:
    for test in tests:
        test_id = test.get("id")
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        if "values" in test:
            fill_values(test["values"], values_dict)
    return tests


if __name__ == "__main__":
    with open(input(
        'Введите наименование файла с результатами тестов или путь до него '
    ), 'r') as f:
        values_data = json.load(f)

    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    with open(input(
        'Введите наименование файла с информацией о тестах или путь до него '
    ), 'r') as f:
        tests_data = json.load(f)

    filled_tests = fill_values(tests_data["tests"], values_dict)

    with open(input(
        'Введите наименование файла с отчетом о выполненных тестах или путь до него '
    ), 'w') as f:
        json.dump({"tests": filled_tests}, f, indent=2)