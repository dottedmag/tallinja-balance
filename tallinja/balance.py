# LICENSE: MIT (see LICENSE)
import tallinja
import datetime
from decimal import Decimal, InvalidOperation

ENDPOINT = '/appws/Balance/GetBalanceByCustomerNumber'
IN_DATE_FMT=' %d/%m/%Y %H:%M:%S'

def req(num):
    return tallinja.req(ENDPOINT, {'CustomerNumber': num})

def parse_balance(resp):
    num_s = resp['Balance'].lstrip('€')
    try:
        return Decimal(num_s)
    except InvalidOperation as e:
        print("Failed to parse balance ", num_s)

# Returns date in Malta's timezone
def parse_top_up_date(resp):
    try:
        s = resp['LastTopUp']
        return datetime.datetime.strptime(s, IN_DATE_FMT)
    except ValueError as e:
        print("Failed to parse date ", s)

def parse_first_name(resp):
    return resp['FirstName']

def parse_last_name(resp):
    return resp['LastName']
