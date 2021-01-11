
buffer_list = []

for n in range(25):
    interface = "Loopback133"+str(n)
    buffer_list.append(interface)

loopbacks = buffer_list