# ======================== CSV FILE: WHAT YOU HAVE TO DO ========================
# 1. In VS Code, create a NEW FILE in the SAME folder as this .py file.
# 2. Name it  exp4.csv
# 3. Copy the lines below into it (WITHOUT the '# ' at the start), save with Ctrl+S.
#
#    client_id,t0_send_ms,t_server_ms,t1_recv_ms
#    C1,1000,1050,1100
#    C2,2000,2130,2060
#    C3,5000,4900,5080
#
# RULES: t1_recv_ms must be bigger than t0_send_ms.
#
# 4. Change DOMAIN below to your chit's domain.   5. Run:  python exp4.py
# ===============================================================================

# WHAT THIS PROGRAM DOES (CRISTIAN'S ALGORITHM):
# Client asks the time server for the time.
#   T0       = when the client sent the question
#   T_server = the time the server answered with
#   T1       = when the client got the answer
# Formulas:
#   RTT          = T1 - T0
#   server time  = T_server + RTT / 2
#   offset       = server time - T1

import csv

DOMAIN = "Distributed Smart Traffic Management System"   # change to your chit
FILE = "exp4.csv"                           # change to your CSV name

print("=== Cristian's Algorithm for", DOMAIN, "===")
print()

file = open(FILE)
for row in csv.DictReader(file):              # one client per row
    t0 = float(row["t0_send_ms"])             # float() turns text into a number
    ts = float(row["t_server_ms"])
    t1 = float(row["t1_recv_ms"])

    rtt = t1 - t0                             # round trip time
    server_time = ts + rtt / 2                # real time now
    offset = server_time - t1                 # how wrong the client clock is

    print("Client", row["client_id"])
    print("   RTT = T1 - T0 =", t1, "-", t0, "=", rtt)
    print("   Estimated server time = T_server + RTT/2 =", ts, "+", rtt / 2, "=", server_time)
    print("   Clock offset =", offset)
    print("   Adjusted client time =", server_time)
    print("-----------------------------------------")
file.close()