#!/usr/bin/python3
from optparse import OptionParser

def main() :
    # set up the option parser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help = "input filename", metavar="FILE")
    parser.add_option("-v", action="store_true", dest="verbose", help="verbose")
    parser.add_option("-q", action="store_false", dest="verbose", help="make quiet")

    # parse the options list and set the option values
    (options, args) = parser.parse_args()

    # list the options
    print("options:", options, type(options))

    # list the remaining values on the command line that were not options
    print("args:", args)

    # an example of printing out the help message
    parser.print_help()

    # examples of how to fetch options
    print("filename: ", options.filename)
    print("verbose: ", options.verbose)

main()




