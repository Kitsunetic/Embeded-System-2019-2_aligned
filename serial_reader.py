"""
https://github.com/Kitsunetic/Simple-Python-Serial-Communication
"""
import argparse
import sys

import serial

from getch import Getch


MainArgumentParser = argparse.ArgumentParser(description='Simple python serial reader for Linux')
MainArgumentParser.add_argument('--device', '-d', type=str, default='/dev/ttyS1', help='device path[/dev/ttyS1]')
MainArgumentParser.add_argument('--baud', '-b', type=int, default=38400, help='Baudrate[38400]')


def main(device, baud):
    with serial.Serial(device, baud) as ser:
        print('Connect to', device, baud)
        print()
        buf = ''
        while True:
            try:
                b = ser.read(1)
                if b in (b'\n', b'\r'):
                    print('\033[F' + buf + '\n')
                    buf = ''
                else:
                    buf += str(b, encoding='utf-8')
                    print('\033[F' + buf)
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    if len(sys.argv) == 1:
        MainArgumentParser.print_help()
        sys.exit(0)
    
    argp = MainArgumentParser.parse_args(sys.argv[1:])
    main(argp.device, argp.baud)
