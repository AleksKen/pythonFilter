from panflute import *
import sys

headers = {}


def textFilter(elem, doc):
    if type(elem) == Header:
        if stringify(elem) in headers.keys():
            if headers.get(stringify(elem)) == elem.level:
                sys.stderr.write(
                    "Повторный заголовок уровня: " + str(elem.level) + " с таким содержанием: " + stringify(elem) + " ")
        else:
            headers[stringify(elem)] = elem.level

    if type(elem) == Header:
        if elem.level <= 3:
            name = [Str(stringify(elem).upper())]
            return Header(*name, level=elem.level)

    if type(elem) == Str:
        if str(elem.text).lower() == "bold":
            name = [Str(elem.text)]
            return Strong(*name)


def main(doc=None):
    return run_filter(textFilter, doc=doc)


if __name__ == "__main__":
    main()
