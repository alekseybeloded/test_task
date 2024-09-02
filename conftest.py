import pytest


@pytest.fixture
def test_data():
    return [
    {
        "id": 2,
        "title": "Smoke test",
        "value": ""
    },
    {
        "id": 41,
        "title": "Debug test",
        "value": ""
    },
    {
        "id": 73,
        "title": "Performance test",
        "value": "",
        "values": [
            {
                "id": 345,
                "title": "Maxperf",
                "value": "",
                "values": [
                    {
                        "id": 230,
                        "title": "Percent",
                        "values": [
                            {
                                "id": 234,
                                "title": "200",
                                "value": ""
                            },
                            {
                                "id": 653,
                                "title": "300",
                                "value": ""
                            }
                        ]
                    }
                ]
            },
            {
                "id": 110,
                "title": "Stability test",
                "value": "",
                "values": [
                    {
                        "id": 261,
                        "title": "Percent",
                        "values": [
                            {
                                "id": 238,
                                "title": "160",
                                "value": ""
                            },
                            {
                                "id": 690,
                                "title": "240",
                                "value": ""
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": 122,
        "title": "Security test",
        "value": "",
        "values": [
            {
                "id": 5321,
                "title": "Confidentiality",
                "value": ""
            },
            {
                "id": 5322,
                "title": "Integrity",
                "value": ""
            }
        ]
    }
]


@pytest.fixture
def value_data():
    return {
        2: 'passed',
        41: 'passed',
        73: 'passed',
        110: 'failed',
        122: 'failed',
        234: 'passed',
        238: 'passed',
        345: 'passed',
        653: 'passed',
        690: 'failed',
        5321: 'passed',
        5322: 'failed'
    }
