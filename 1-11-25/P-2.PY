#GENERATOR
def generate_squares(n):
    for i in range(n):
        yield i * i
for square in generate_squares(10):
    print(square)