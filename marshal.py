#!/usr/bin/env python
import marshal, sys
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    print Y + '0{' + 37 * '=' + '}0'
    print Y + '|' + B + ' Code by : ' + W + 'Debby anggraini ' + R + 'a.k.a' + W + ' Ci Ku' + Y + ' |'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/ciku370' + Y + '  |'
    print Y + '0{' + 37 * '=' + '}0\n'


try:
    file = sys.argv[1]
    o = file.replace('.py', '')
except IndexError:
    banner()
    print B + '[' + W + '+' + B + '] ' + W + 'python2 ' + sys.argv[0] + ' [file]\n'
    sys.exit()

try:
    strng = open(file, 'r').read()
except IOError:
    banner()
    print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
    sys.exit()

try:
    code = compile(strng, '<debby>', 'exec')
    data = marshal.dumps(code)
except TypeError:
    banner()
    print R + '[' + W + '!' + R + '] ' + W + 'file already compiled\n'
    sys.exit()

fileout = open(o + 'enc.py', 'wb')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + o + 'enc.py\n'
