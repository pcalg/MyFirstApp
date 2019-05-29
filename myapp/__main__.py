import sys
import myapp.calculations.calculate as calculate


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("NEW VERSION!")
    print("My new application.")

    print(args)

    # calculate something really interesting!
    n = calculate.calculate(34, 5)

    print(n)


if __name__ == "__main__":
    main()
