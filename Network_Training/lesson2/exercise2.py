""" Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list. 
"""
from __future__ import print_function, unicode_literals

my_list = ["10.1.1.1", "10.1.2.1", "10.1.3.1", "8.8.8.8", "10.1.4.1"]
my_list.append("10.2.1.1")
my_list.extend(["10.4.1.1", "10.4.1.2"])
my_list = my_list + ["10.4.10.1", "10.4.10.2"]

print(my_list)
print(my_list[0])
print(my_list[-1])

first_ip = my_list.pop(0)
last_ip = my_list.pop(-1)
my_list[0] = "2.2.2.2"

print(my_list[0])
