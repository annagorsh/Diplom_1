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

@pytest.fixture
def expected_buns():
    expected_buns = []
    expected_buns.append(Bun("black bun", 100))
    expected_buns.append(Bun("white bun", 200))
    expected_buns.append(Bun("red bun", 300))
    return expected_buns

@pytest.fixture
def expected_ingredients():
    expected_ingredients = []
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200))
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300))
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200))
    expected_ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
    return expected_ingredients