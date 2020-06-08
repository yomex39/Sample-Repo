"""Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

# Solution

from __future__ import print_function, unicode_literals

show_version = "*0 CISCO881-SEC-K9      FTX0000038X    "
show_version = show_version.strip()

fields = show_version.split()
model = fields[1]
Serial_Number = fields[2]

print()
vendor_cisco = "cisco" in model.lower()
print("checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = "881" in model
print("checking if model contains 881: {}".format(model_881))

print("Serial NumberL {}".format(Serial_Number))
print("Model: {}".format(model))
print()
