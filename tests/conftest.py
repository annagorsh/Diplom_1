import pytest

from praktikum.ingredient import *
from praktikum.ingredient_types import *
from praktikum.burger import *
from praktikum.bun import *
from praktikum.database import *


@pytest.fixture
def ingredient():
    return Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="1000 островов", price=30.0)

@pytest.fixture
def bun():
    return Bun(name="Ржаная", price=80.5)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()