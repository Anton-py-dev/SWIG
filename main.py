import example
import importlib
importlib.reload(example)


print(example.add(1, 5))
print(example.multiply(4.3, 6.2))
print(example.subtract(53, 564))
print(example.concatenate("hello", "world"))

