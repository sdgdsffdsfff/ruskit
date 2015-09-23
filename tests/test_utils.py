from ruskit.utils import spread


def test_spread():
    data = {
        "192.168.0.1": [1, 2],
        "192.168.0.2": [3, 4],
        "192.168.0.3": [5, 6]
    }

    res = spread(data, 4)
    assert res == [1, 3, 5, 2]
