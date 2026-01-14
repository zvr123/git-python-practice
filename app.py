import datetime

def greet(name):
    return f"Helloooo, {name}!"


if __name__ == "__main__":
    user = "World"
    print(greet(user), datetime.datetime.now())

