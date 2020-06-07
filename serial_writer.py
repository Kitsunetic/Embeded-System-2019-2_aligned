"""
https://github.com/Kitsunetic/Simple-Python-Serial-Communication
"""
import argparse
import sys

import serial

from getch import Getch


MainArgumentParser = argparse.ArgumentParser(description='Simple python serial writer for Linux')
MainArgumentParser.add_argument('--device', '-d', type=str, default='/dev/ttyS1', help='device path[/dev/ttyS1]')
MainArgumentParser.add_argument('--baud', '-b', type=int, default=38400, help='Baudrate[38400]')
MainArgumentParser.add_argument('--canonical', '-c', action='store_true', help='canonical mode')


def main(device, baud, canonical):
    with serial.Serial(device, baud) as ser:
        print('Connect to', device, baud, 'as', 'canonical' if canonical else 'non-canonical', 'mode.')
        if canonical:
            while True:
                try:
                    line = input() + '\n'
                    ser.write(line.encode(encoding='utf-8'))
                except KeyboardInterrupt:
                    break
        else:
            getch = Getch()
            buf = ''
            print()
            while True:
                c = getch()
                if c == '\x03':
                    break
                buf += c
                if c in ('\n', '\r'):
                    print('\033[F' + buf + '\n')
                    buf = ''
                else:
                    print('\033[F' + buf)
                s = c.encode('utf-8')
                ser.write(s)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        MainArgumentParser.print_help()
        sys.exit(0)
    
    argp = MainArgumentParser.parse_args(sys.argv[1:])
    main(argp.device, argp.baud, argp.canonical)
