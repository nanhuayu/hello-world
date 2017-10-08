import argparse
parser = argparse.ArgumentParser(prefix_chars='+')
parser.add_argument('+book')
#parser.add_argument('+foo', nargs = "*")
parser.add_argument('word', nargs = "*", help='word search')
a = parser.parse_args("foo hello f world +book nice".split())
parser.print_help()
print(a.word)
print (a.book)
