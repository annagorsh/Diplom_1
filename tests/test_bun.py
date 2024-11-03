class TestBun:

    def test_init_successful(self, bun):
        assert bun.name == "Ржаная" and bun.price == 80.5

    def test_get_bun_name_returns_name(self, bun):
        bun.get_name()
        assert bun.get_name() == "Ржаная"

    def test_get_bun_price_returns_price(self, bun):
        bun.get_price()
        assert bun.get_price() == 80.5
