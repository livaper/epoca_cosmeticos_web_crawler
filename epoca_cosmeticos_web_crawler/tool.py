r"""Command-line tool to prettify big number as millions, billions and trillions
Usage::
    $ python -m prettifier.tool 12345
    12345
    $ python -m prettifier.tool 1234567899
    1.2B
    $ python -m prettifier.tool number
    The type is not a numeric value
"""

from epoca_cosmeticos_web_crawler.run import main

def main():
    import sys
    import ast

    if len(sys.argv) != 0:
        print('usage : python run_epoca_cosmeticos_web_crawler.py \n The call has no argument. Try again!')
        sys.exit(1)

    try:
        # Usage of ast is the safe 'eval' for string to numbers
        print(main())
    except Exception as e:
        print('There was an error trying to crawl Epoca Cosmeticos Website. Please try again later')
        sys.exit(1)


if __name__ == '__main__':
    main()