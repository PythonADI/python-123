import random
import module


def test_sell_order():
    assert module.place_bet(110, 100) == 1


def test_purchase_order():
    assert module.place_bet(90, 100) == 2


def test_do_nothing():
    assert module.place_bet(91, 100) is None
    assert module.place_bet(101, 100) is None
    assert module.place_bet(109, 100) is None
    assert module.place_bet(100, 100) is None


# def test_random():
#     prev_price = random.randint(100, 100_000)

#     lower_bound = int(prev_price * 0.8)
#     upper_bound = int(prev_price * 1.2)
#     price = random.randint(lower_bound, upper_bound)
#     assert module.place_bet(price, prev_price)


if __name__ == "__main__":
    test_sell_order()
    test_purchase_order()
    test_do_nothing()
    # test_random()
    print("All ")
