
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# ==========================================
# PIZZA PRICE - BRANCH TESTS
# ==========================================

def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra-large", 2, False)


def test_valid_size():
    assert pizza_price("medium", 2, False) == 430


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_zero_toppings():
    assert pizza_price("medium", 0, False) == 350


def test_three_toppings():
    assert pizza_price("small", 3, False) == 320


def test_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


def test_cheese_burst_small():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


def test_cheese_burst_available():
    assert pizza_price("medium", 1, True) == 490


def test_no_cheese_burst():
    assert pizza_price("large", 0, False) == 500


# ==========================================
# ORDER DISCOUNT - BRANCH TESTS
# ==========================================

def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_order_exactly_300():
    assert order_discount(300, "monday", False) == 30


def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200


def test_tuesday_student_discount():
    assert order_discount(400, "tuesday", True) == 250


def test_saturday_discount():
    assert order_discount(400, "saturday", False) == 0


def test_sunday_student_discount():
    assert order_discount(400, "sunday", True) == 50


def test_regular_weekday_discount():
    assert order_discount(500, "monday", False) == 50


def test_regular_weekday_student_discount():
    assert order_discount(500, "monday", True) == 100


# ==========================================
# DELIVERY STATUS - BRANCH TESTS
# ==========================================

def test_distance_above_10():
    assert delivery_status(20, 11) == "not deliverable"


def test_distance_exactly_10():
    assert delivery_status(30, 10) == "on time"


def test_delivery_exactly_30_minutes():
    assert delivery_status(30, 5) == "on time"


def test_delivery_31_minutes():
    assert delivery_status(31, 5) == "late"


def test_delivery_exactly_45_minutes():
    assert delivery_status(45, 5) == "late"


def test_delivery_above_45_minutes():
    assert delivery_status(46, 5) == "free pizza"
