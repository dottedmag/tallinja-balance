#!/usr/bin/env python3
# LICENSE: MIT (see LICENSE)

import sys
import argparse
import tallinja
from tallinja import balance
OUT_DATE_FMT='%Y-%m-%d %H:%M:%S'

def display(resp, bl=True, name=False, date=False):
    resp = tallinja.check(resp)
    if isinstance(resp, str):
        print(resp)
        return False
    if name:
        print("Name: "+balance.parse_first_name(resp)+' '
              +balance.parse_last_name(resp))
    if date:
        d = balance.parse_top_up_date(resp)
        if not d:
            return False
        print("Last top-up: "+d.strftime(OUT_DATE_FMT))
    if bl:
        b = balance.parse_balance(resp)
        if not b:
            return False
        print("Balance: "+str(b))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('cardnum', metavar='CARDNUM')
    parser.add_argument('--date', help='display top-up date',
                        action='store_true')
    parser.add_argument('--name', help='display card owner\'s name',
                        action='store_true')
    parser.add_argument('--no-balance', help='do not display balance',
                        action='store_false', dest='balance', default=True)
    return parser.parse_args()

def main():
    args = parse_args()
    resp = balance.req(args.cardnum)
    if not display(resp, args.balance, args.name, args.date):
        sys.exit(1)

if __name__=='__main__':
    main()
