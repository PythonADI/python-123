import helpers
# import module_2
from exa.module_2 import (
    f,
    g,
)


def main():
    helpers.greet_user("Luka")
    print(f(5))
    print(g(2))


if __name__ == "__main__":
    main()
