from tests.conftest import expected_ingredients


class TestDatabase:

    def test_available_buns_returns_list_of_buns(self, database, expected_buns):
        result = database.available_buns()
        assert result == expected_buns

    def test_available_ingredients_returns_list_of_ingredients(self, database, expected_ingredients):
        result = database.available_ingredients()
        assert result == expected_ingredients

