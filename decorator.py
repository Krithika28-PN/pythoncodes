def greet(funct):
    def inner_funct():
        print("Initializer")
        funct()
        print("Finaliser")
    return inner_funct

@greet
def hello():
    print("main function")

hello()

# I can say that by example let suppose some TC needs new token every time so we can use that funct as decorator