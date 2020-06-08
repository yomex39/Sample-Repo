from __future__ import print_function

try:
    # Python 2 compatible
    ip_addr = raw_input("Please enter an IP address: ")
except NameError:
    # Python 3 compatible
    ip_addr = input("Please enter an IP address: ")
octets = ip_addr.split(".")
print()
print("{:^15}{:^15}{:^15}{:^15}".format("octet1", "octet2", "octet3", "octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print(
    "{:^15}{:^15}{:^15}{:^15}".format(
        bin(int(octets[0])),
        bin(int(octets[1])),
        bin(int(octets[2])),
        bin(int(octets[3])),
    )
)
print(
    "{:^15}{:^15}{:^15}{:^15}".format(
        hex(int(octets[0])),
        hex(int(octets[1])),
        hex(int(octets[2])),
        hex(int(octets[3])),
    )
)
print("-" * 60)
print()
