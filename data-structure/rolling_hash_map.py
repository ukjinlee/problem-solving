def hash(str):
    h = 0
    a = 256  # bigger than ascii max value 255
    b = 3571  # prime number
    for ch in str:
        h = (h * a + ord(ch)) % b
    return h


class KeyValue:
    def __init__(self):
        self.key = ""
        self.value = ""


class Map:
    def __init__(self):
        self.keyArray = [[] for _ in range(3571)]

    def add(self, key, value):
        h = hash(key)
        self.keyArray[h].append((key, value))

    def get(self, key):
        h = hash(key)
        tuples = self.keyArray[h]
        for pair in tuples:
            if pair[0] == key:
                return pair[1]
        print(f'Not Found: {key}')
        return ""

    def print(self):
        for i in range(len(self.keyArray)):
            if len(self.keyArray[i]) == 0:
                continue
            print(f"{i}: {self.keyArray[i]}")


def test():
    print(hash("hello world"))
    print(hash("hello world"))
    print(hash("hello world!"))
    print(hash("hello world."))
    print(hash("hello world. I'm Joel."))
    print(hash("Joel"))
    print(hash("Rachel"))
    print()
    m = Map()
    m.add("Joel", 42)
    m.add("Rachel", 39)
    m.print()
    value = m.get('Joel')
    print(value)
    value = m.get('Rachel')
    print(value)
    value = m.get('Tom')
    print(value)


if __name__ == '__main__':
    test()
