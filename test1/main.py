

a = {
    "key1" : 1,
    "key2" : {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

def object_depth(data, depth=1):
    result = []
    for key in data:
        result.append("{} {}".format(key, depth))
        if isinstance(data[key], dict):
            result += object_depth(data[key], depth+1)

    return result

def print_depth(a):
    print("\n".join(object_depth(a, 1)))

if __name__ == "__main__":
    print_depth(a)
