import re
textfile = open('Feb 07 5_28 PM.txt', 'r')
filetext = textfile.read()
textfile.close()


domains = re.findall(r"www\.*\.*", filetext) # directives not clear on how to address the and identify domains
ipaddres = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', filetext)
ipaddres = str(ipaddres)

print("1. Domains :" + str(domains))
print("2. IP addresses :" + ipaddres)