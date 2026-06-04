def Operation():
    while True:
        name = input("choise one opération between, Add, Sub, Mult, Div, Mod :").strip().lower()
        match name:
            case "add" | "sub" | "mult" | "div" | "mod":
                return name
            case _:
                print("Invalid operation")


def GetInt(_prompt):
    while True:
        try:
            return int(input(_prompt))
        except ValueError:
            pass


def main():
    x = GetInt("Choise X")
    y = GetInt("Choise Y")
    operation = Operation()
    result = 0
    match operation:
        case "Add":
            result = x + y
        case "Sub":
            result = x - y
        case "Mult":
            result = x * y
        case "Div":
            if y != 0:
               result = x / y
            else:
              print("You can't divide by 0")
        case "Mod":
            if y != 0:
               result = x % y
            else:
              print("You can't divide by 0")
        case _:
            print("Invalid operation")

    print(f"The result of your calcul is {result}")


main()
