
class Construction:
    student = "ankit"

    def greet(self):
        print("my name is something.")

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Construction('aman', 12)

obj.greet()

print(obj.name)
print(obj.age)