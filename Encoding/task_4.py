dev='разработка'
admin = 'администрирование'
prot = 'protocol'
std = 'standard'

print(type(dev))
dev_b = dev.encode('utf-8')
print(dev_b)
print(type(dev_b))
dev = dev_b.decode('utf-8')
print(type(dev))
#маленькая проверка для себя

admin_b = admin.encode('utf-8')
admin = admin_b.decode('utf-8')


prot_b = prot.encode('utf-8')
prot = prot_b.decode('utf-8')


std_b = std.encode('utf-8')
std = std_b.decode('utf-8')

