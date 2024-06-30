#!/usr/bin/python3
import re
import argparse

CALL_RE = r"^[a-zA-Z0-9-]+$"

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--callsign", dest="callsign", required=True, type=str, help="HAM callsign")
args = parser.parse_args()

callsign = args.callsign
passcode = str()

if re.match(CALL_RE, callsign):
    callsign = callsign.upper()

    i = 0
    tmp_code = 29666
    while i < len(callsign):
        try:
            tmp_code = tmp_code ^ ord(callsign[i]) * 256
            tmp_code = tmp_code ^ ord(callsign[i + 1])
            i += 2
        except IndexError:
            break

    passcode = tmp_code & 32767
    print(f"APRS passcode for {callsign}: {passcode}")

else:
    print("Invalid Callsign, Try Again!")
