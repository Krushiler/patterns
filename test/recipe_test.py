import datetime

from working_with_settings.di.di import Di


def test_recipe(inject: Di):
    repository = inject.get_recipe_repository()

    assert len(repository.get_recipes()) == 1

    print(repository.get_recipes())

    assert repository.get_recipes()[0].cooking_time == datetime.timedelta(minutes=25)

    assert len(repository.get_recipes()[0].ingredients) == 8
    assert len(repository.get_recipes()[0].cooking_steps) == 9
