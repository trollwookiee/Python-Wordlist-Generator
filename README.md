# Python Wordlist Generator

> Creating Awesome Wordlist with Python.
> You can check sample this file: [`output/wordlist.txt`](output/wordlist.txt)

### Usage

```
usage: wgen.py [-h] [-chr CHARS] [-min MIN_LENGTH] [-max MAX_LENGTH]
               [-out OUTPUT]

Python Wordlist Generator

optional arguments:
  -h, --help            show this help message and exit
  -chr CHARS, --chars CHARS
                        characters to iterate
  -min MIN_LENGTH, --min_length MIN_LENGTH
                        minimum length of characters
  -max MAX_LENGTH, --max_length MAX_LENGTH
                        maximum length of characters
  -out OUTPUT, --output OUTPUT
                        output of wordlist file.

usage: wgen_ham_radio_callsign.py [-h] [-pchr PREFIX_CHARS]
                                  [-pmin PREFIX_MIN_LENGTH]
                                  [-pmax PREFIX_MAX_LENGTH]
                                  [-cchr CLASS_CHARS] [-cmin CLASS_MIN_LENGTH]
                                  [-cmax CLASS_MAX_LENGTH]
                                  [-schr SUFFIX_CHARS]
                                  [-smin SUFFIX_MIN_LENGTH]
                                  [-smax SUFFIX_MAX_LENGTH] [-out OUTPUT]

Python Wordlist Generator

optional arguments:
  -h, --help            show this help message and exit
  -pchr PREFIX_CHARS, --prefix_chars PREFIX_CHARS
                        characters to prefix iterate
  -pmin PREFIX_MIN_LENGTH, --prefix_min_length PREFIX_MIN_LENGTH
                        minimum length of prefix characters
  -pmax PREFIX_MAX_LENGTH, --prefix_max_length PREFIX_MAX_LENGTH
                        maximum length of prefix characters
  -cchr CLASS_CHARS, --class_chars CLASS_CHARS
                        characters to class iterate
  -cmin CLASS_MIN_LENGTH, --class_min_length CLASS_MIN_LENGTH
                        minimum length of class characters
  -cmax CLASS_MAX_LENGTH, --class_max_length CLASS_MAX_LENGTH
                        maximum length of class characters
  -schr SUFFIX_CHARS, --suffix_chars SUFFIX_CHARS
                        characters to suffix iterate
  -smin SUFFIX_MIN_LENGTH, --suffix_min_length SUFFIX_MIN_LENGTH
                        minimum length of suffix characters
  -smax SUFFIX_MAX_LENGTH, --suffix_max_length SUFFIX_MAX_LENGTH
                        maximum length of suffix characters
  -out OUTPUT, --output OUTPUT
                        output of wordlist file.

```

### Example

```
$ python3 wgen.py -chr=abc -min=1 -max=4 -out=output/wordlist.txt

# or

$ python3 wgen.py --chars=abc --min_length=1 --max_length=4 --output=output/wordlist.txt

# or

python wgen_ham_radio_callsign.py --prefix_chars=F --prefix_min_length=1 --prefix_max_length=1 --class_chars=123456789 --class_min_length=1 --class_max_length=1 --suffix_chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ --suffix_min_length=3 --suffix_max_length=3 --out=output/callsign_wordlist_france.txt
[+] Creating wordlist at `output/callsign_wordlist_france.txt`...
[i] Starting time: 11:04:55

[+] Generating wordlist for `F`...

[+] Generating wordlist for `F1`...
[+] saving character `F1ZZZ`
[+] Generating wordlist for `F2`...
[+] saving character `F2ZZZ`
[+] Generating wordlist for `F3`...
[+] saving character `F3ZZZ`
[+] Generating wordlist for `F4`...
[+] saving character `F4ZZZ`
[+] Generating wordlist for `F5`...
[+] saving character `F5ZZZ`
[+] Generating wordlist for `F6`...
[+] saving character `F6ZZZ`
[+] Generating wordlist for `F7`...
[+] saving character `F7ZZZ`
[+] Generating wordlist for `F8`...
[+] saving character `F8ZZZ`
[+] Generating wordlist for `F9`...
[+] saving character `F9ZZZ`
[i] End time: 11:04:56


```

### Disclaimer

> Because many are violating the ITE Law,
> therefore this disclaimer we made to protect us from legal related undesirable actions of other parties,
> such as using this scripts or code for unlawful activities.
>
> Therefore we with **EXPRESSLY** stating **NOT RESPONSIBLE** and **FREE FROM CLAIMS OF LAW**
> for any misuse of script or code that we provide on this repository.
