import time
import telnetlib

HOST ="localhost"
tn=telnetlib.Telnet()
tn.open(HOST,"7373")
tn.write(b"M90\n")
tn.write(b"C\n")
print(tn.read_all().decode('ascii'))