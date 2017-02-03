import os
import sys
import time
import string
import argparse
import itertools

# example: python wgen_ham_radio_callsign.py --prefix_chars=ABCD --prefix_min_length=1 --prefix_max_length=2 --class_chars=123 --class_min_length=1 --class_max_length=1 --suffix_chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ --suffix_min_length=3 --suffix_max_length=4 --out=output/callsign_wordlist.txt
# example: python wgen_ham_radio_callsign.py --prefix_chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ --prefix_min_length=1 --prefix_max_length=2 --class_chars=123 --class_min_length=1 --class_max_length=1 --suffix_chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ --suffix_min_length=3 --suffix_max_length=4 --out=output/callsign_wordlist.txt


def createWordList(prefix_chrs, prefix_min_length, prefix_max_length, class_chrs, class_min_length, class_max_length, suffix_chrs, suffix_min_length, suffix_max_length, output):
    """
    :param `prefix_chrs` is prefix characters to iterate.
    :param `prefix_min_length` is minimum length of prefix characters.
    :param `prefix_max_length` is maximum length of prefix characters.
    :param `class_chrs` is class characters to iterate.
    :param `class_min_length` is minimum length of class characters.
    :param `class_max_length` is maximum length of class characters.
    :param `suffix_chrs` is suffix characters to iterate.
    :param `suffix_min_length` is minimum length of suffix characters.
    :param `suffix_max_length` is maximum length of suffix characters.
    :param `output` is output of wordlist file.
    """
    if prefix_min_length > prefix_max_length:
        print ("[!] Please `prefix_min_length` must be smaller or same as with `prefix_max_length`")
        sys.exit()
    if class_min_length > class_max_length:
        print ("[!] Please `class_min_length` must be smaller or same as with `class_max_length`")
        sys.exit()
    if suffix_min_length > suffix_max_length:
        print ("[!] Please `suffix_min_length` must be smaller or same as with `suffix_max_length`")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print ('[+] Creating wordlist at `%s`...' % output)
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))

    output = open(output, 'w')

    for np in range(prefix_min_length, prefix_max_length + 1):
        for hamPrefix in itertools.product(prefix_chrs, repeat=np):
            charsPrefix = ''.join(hamPrefix)
            print ('\n[+] Generating wordlist for `%s`...' % charsPrefix)
            for nc in range(class_min_length, class_max_length + 1):
                for hamClass in itertools.product(class_chrs, repeat=nc):
                    charsClass = ''.join(hamClass)
                    print ('\n[+] Generating wordlist for `%s`...' % (charsPrefix + charsClass))
                    for nx in range(suffix_min_length, suffix_max_length + 1):
                        for xs in itertools.product(suffix_chrs, repeat=nx):
                            chars = ''.join(xs)
                            output.write("%s\n" % (charsPrefix + charsClass + chars))
                            sys.stdout.write('\r[+] saving character `%s`' % (charsPrefix + charsClass + chars))
                            sys.stdout.flush()
    output.close()

    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python Wordlist Generator')
    parser.add_argument(
        '-pchr', '--prefix_chars',
        default=None, help='characters to prefix iterate')
    parser.add_argument(
        '-pmin', '--prefix_min_length', type=int,
        default=1, help='minimum length of prefix characters')
    parser.add_argument(
        '-pmax', '--prefix_max_length', type=int,
        default=2, help='maximum length of prefix characters')
    parser.add_argument(
        '-cchr', '--class_chars',
        default=None, help='characters to class iterate')
    parser.add_argument(
        '-cmin', '--class_min_length', type=int,
        default=1, help='minimum length of class characters')
    parser.add_argument(
        '-cmax', '--class_max_length', type=int,
        default=2, help='maximum length of class characters')
    parser.add_argument(
        '-schr', '--suffix_chars',
        default=None, help='characters to suffix iterate')
    parser.add_argument(
        '-smin', '--suffix_min_length', type=int,
        default=1, help='minimum length of suffix characters')
    parser.add_argument(
        '-smax', '--suffix_max_length', type=int,
        default=2, help='maximum length of suffix characters')
    parser.add_argument(
        '-out', '--output',
        default='output/wordlist.txt', help='output of wordlist file.')

    args = parser.parse_args()
    if args.prefix_chars is None:
        args.prefix_chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    if args.class_chars is None:
        args.class_chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    if args.suffix_chars is None:
        args.suffix_chars = string.printable.replace(' \t\n\r\x0b\x0c', '')

    createWordList(args.prefix_chars, args.prefix_min_length, args.prefix_max_length, args.class_chars, args.class_min_length, args.class_max_length, args.suffix_chars, args.suffix_min_length, args.suffix_max_length, args.output)
