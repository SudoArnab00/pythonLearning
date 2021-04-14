import string
def defang(ipaddr):
    newaddr = ""
    split_addr = ipaddr.split(".")
    seperator = "[.]"
    newaddr = seperator.join(split_addr)  #seperator comes after each iterable item
    return newaddr

ipaddr = defang('192.168.0.1')
print(ipaddr)