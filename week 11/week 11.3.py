
def main():
    min_range = 1
    max_range = 100

    try:
        num = int(input())
        if num < min_range or num > max_range:
            print("Error: Number out of allowed range")
        else:
            print("Valid input.")
    except ValueError:
        print("Error: invalid literal for int()")


if __name__ == "__main__":
     main()
