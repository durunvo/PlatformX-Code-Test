
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person("User1", "1", None)
person_b = Person("User2", "2", person_a)

a = {
    "key1" : 1,
    "key2" : {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b
        }
    }
}

def is_dict(data):
    return isinstance(data, dict)

def is_object(data):
    return getattr(data, "__dict__")

def is_string(data):
    return isinstance(data, str)

def is_integer(data):
    return isinstance(data, int)

def object_depth(data, depth=1):
    result = []
    if data is None: pass
    elif is_dict(data):
        for key in data:
            result.append("{} {}".format(key, depth))
            if data[key] is None: pass
            elif is_string(data[key]) or is_integer(data[key]): pass
            elif is_dict(data[key]) or is_object(data[key]):
                result += object_depth(data[key], depth+1)
    elif is_object(data):
        for key in filter(lambda a: not a.startswith('__'), dir(data)):
            result.append("{} {}".format(key, depth))
            if getattr(data, key) is None: pass
            elif is_string(getattr(data, key)) or is_integer(getattr(data, key)): pass
            elif is_dict(getattr(data, key)) or is_object(getattr(data, key)):
                result += object_depth(getattr(data, key), depth+1)

    return result

def print_depth(a):
    print("\n".join(object_depth(a, 1)))

if __name__ == "__main__":
    print_depth(a)
