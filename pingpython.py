from ping3 import ping , verbose_ping

response = ping('192.168.0.123')

print(response)

if response:
    print('float')
else:
    print('none o false')

