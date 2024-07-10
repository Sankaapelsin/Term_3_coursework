from src.utils import five_last_operations, loads


def test_five_last_operations():
    assert len(five_last_operations()) == 5
