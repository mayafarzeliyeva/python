def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Uzunluq 2 ilə 6 arasında olmalıdır
    if len(s) < 2 or len(s) > 6:
        return False
    
    # 2. İlk iki simvol mütləq hərf olmalıdır
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    return True


main()
