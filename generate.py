import sys
from random import choice


pass_len = 12

if len(sys.argv) == 2:
    pass_len = int(sys.argv[1])

chars = [33, 40, 41] + list(range(64, 91)) + list(range(97, 122))

pass_chars = [str(x) for x in list(range(0, 10))] + [chr(x) for x in chars]

password = ''.join([choice(pass_chars) for _ in range(pass_len)])

print(password)

