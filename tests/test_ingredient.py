from praktikum.ingredient_types import *

class TestIngredient:

    def test_init_successful(self, ingredient):
        assert ingredient.type == INGREDIENT_TYPE_SAUCE and ingredient.name == "1000 островов" and ingredient.price == 30.0

    def test_get_price_returns_price(self, ingredient):
        price = ingredient.get_price()
        assert price == 30.0

    def test_get_name_returns_name(self, ingredient):
        name = ingredient.get_name()
        assert name == "1000 островов"

    def test_get_type_returns_type(self, ingredient):
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
