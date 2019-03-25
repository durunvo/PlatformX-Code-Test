from main import print_depth, object_depth

def test():
    a = {
        "key1": 1
    }
    assert len(object_depth(a)) == 1
    assert object_depth(a) == ["key1 1"]
    b = {
        "key1": 1,
        "key2": 2
    }
    assert len(object_depth(b)) == 2
    assert "key1 1" in object_depth(b)
    assert "key2 1" in object_depth(b)
    c = {
        "key1": 1,
        "key2": {

        }
    }
    assert len(object_depth(c)) == 2
    assert "key1 1" in object_depth(c)
    assert "key2 1" in object_depth(c)
    d = {
        "key1": 1,
        "key2": {
            "key3": 1
        }
    }
    assert len(object_depth(d)) == 3
    assert "key1 1" in object_depth(d)
    assert "key2 1" in object_depth(d)
    assert "key3 2" in object_depth(d)
    e = {
        "key2": {
            "key1": 1,
            "key3": 1
        }
    }
    assert len(object_depth(e)) == 3
    assert "key1 1" not in object_depth(e)
    assert "key1 2" in object_depth(e)
    assert "key2 1" in object_depth(e)
    assert "key3 2" in object_depth(e)
    f = {}
    assert len(object_depth(f)) == 0
    g = {
        "a": 1
    }
    assert len(object_depth(g)) == 1
    assert "key1 1" not in object_depth(g)
    assert "a 1" in object_depth(g)


if __name__ == "__main__":
    test()
    print('Pass all test')
