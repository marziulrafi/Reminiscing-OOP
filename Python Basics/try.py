try:
    x = int("hello")   # invalid conversion
except ValueError:
    print("Invalid number!")

finally:
    print("This always runs.")