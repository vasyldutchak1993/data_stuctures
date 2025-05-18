class Stack:
    def __init__(self, size, stack_type=str):
        self.__stack = []
        self.__size = size
        self.__stack_type = stack_type

    @staticmethod
    def type_check(func):
            def wrapper(self, value):
                if not isinstance(value, self.__stack_type):
                    raise TypeError(f"Argument must be of type {self.__stack_type.__name__}")
                return func(self, value)
            return wrapper

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        return self.__stack.pop()

    @type_check
    def push(self, value):
        if self.is_full():
            raise IndexError('Stack is full')

        self.__stack.append(value)

    def count(self):
        return len(self.__stack)

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return self.__size == len(self.__stack)

    def clear(self):
        self.__stack = []

    def __str__(self):
        return str(self.__stack)


if __name__ == '__main__':
    s = Stack(5)
    print(s.is_empty())
    print(s.is_full())
    s.push("a")
    s.push("b")
    s.push("c")
    s.push("d")
    print(s)
    print(s.peek())
    print(s.peek())
    print(s.pop())
    print(s.is_empty())
    print(s.is_full())
    print(s)
    print(s.count())

