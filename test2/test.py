from main import print_depth, object_depth, Person

person_a = Person("User1", "1", None)
person_b = Person("User2", "2", person_a)

def test():
    a = {
        "key1": 1
    }
    assert len(object_depth(a)) == 1
    assert object_depth(a) == ["key1 1"]
    b = {
        "key1": 1,
        "key2": "string",
        "key3": None,
    }
    assert len(object_depth(b)) == 3
    assert "key1 1" in object_depth(b)
    assert "key2 1" in object_depth(b)
    assert "key3 1" in object_depth(b)
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
    h = {
        "a": person_a
    }
    assert len(object_depth(person_a)) == 3
    assert len(object_depth(h)) == 4
    assert "a 1" in object_depth(h)
    assert "father 2" in object_depth(h)
    assert "first_name 2" in object_depth(h)
    assert "last_name 2" in object_depth(h)
    i = {
        "a": person_a,
        "b": person_b
    }
    assert len(object_depth(person_a)) == 3
    assert len(object_depth(person_b)) == 6
    assert len(object_depth(i)) == 11
    assert "a 1" in object_depth(i)
    assert "b 1" in object_depth(i)
    assert "father 2" in object_depth(i)
    assert "first_name 2" in object_depth(i)
    assert "last_name 2" in object_depth(i)
    assert "last_name 3" in object_depth(i)
    assert not "last_name 4" in object_depth(i)


if __name__ == "__main__":
    test()
    print('Pass all test')
