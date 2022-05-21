class TestClass:
    def __init__(self, name):  # contructor with parameter
        self.name = name;

    def greet(self):
        print(f"Hello {self.name}")


class Testsubclass(TestClass):
    pass  # if you dont want to define any method in subclass but want to use parent


# need two blank lines after class
testclass1 = TestClass("John")
testclass1.greet()

testsubclass = Testsubclass("John")
testsubclass.greet()
