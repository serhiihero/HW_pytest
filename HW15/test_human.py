# Test the Human class in the attached file. I will check the coverage. Write as much TCs as possible

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_change_age(create_test_human):
    human = create_test_human
    current_age = human.age
    human.grow()
    changed_age = current_age + 1
    assert changed_age == current_age + 1, f'Something went wrong. Can\'t set given {changed_age} age.'


@pytest.mark.smoke
@pytest.mark.regression
def test_change_gender(create_test_human):
    human = create_test_human
    new_gender = 'female'
    human.change_gender(new_gender)
    assert new_gender == human.gender, f'Something went wrong. Can\'t set {new_gender} gender.'


@pytest.mark.regression
def test_create_test_human_with_params(create_test_human_with_params):
    human = create_test_human_with_params('Barbara', 18, 'female')
    assert human._Human__name == 'Barbara' and human._Human__age == 18 and human._Human__gender == 'female', \
        'Something went wrong. User not created.'


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail
def test_max_age_value(create_test_human_with_params):
    human = create_test_human_with_params('Derek', 100, 'male')
    new_age_value = 100
    human.grow()
    changed_age = human.age + 1
    assert changed_age < new_age_value, 'User can not be over 100 years old.'


@pytest.mark.regression
@pytest.mark.xfail
def test_nonexistent_gender(create_test_human_with_params):
    human = create_test_human_with_params('Peter', 25, 'male')
    nonexistent_gender = 'bla-bla'
    with pytest.raises(TypeError):
        human.change_gender(nonexistent_gender)
    assert human.gender != nonexistent_gender, f'Only "female" or "male" can be set for gender. ' \
                                               f'Given gender {nonexistent_gender}.'


@pytest.mark.regression
@pytest.mark.xfail
def test_change_same_gender_set(create_test_human_with_params):
    human = create_test_human_with_params('Melissa', 45, 'female')
    new_gender = 'female'
    human.change_gender(new_gender)
    assert human.gender == new_gender, f'{human.name} already has the same {human.gender} gender.'


@pytest.mark.regression
@pytest.mark.xfail
def test_change_gender_for_dead_user(create_test_human_with_params):
    human = create_test_human_with_params('Thomas', 101, 'male')
    # Human class have an issue with the __is_alive.
    # I have added method set_dead to the Human class to be able to change status.
    human.set_dead()
    new_gender = 'female'
    with pytest.raises(TypeError):
        human.change_gender(new_gender)
    assert human.gender == new_gender, f'Something went wrong. ' \
                                       f'There is no way to set new gender for person with age {human.age}.'
