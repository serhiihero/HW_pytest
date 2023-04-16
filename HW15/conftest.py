import pytest
from HW15.human import Human


@pytest.fixture()
def create_test_human():
    yield Human(name='John', age=35, gender='male')


@pytest.fixture()
def create_test_human_with_params():
    def __create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    yield __create_human
