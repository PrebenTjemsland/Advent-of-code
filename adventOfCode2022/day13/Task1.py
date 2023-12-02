packet_pairs = []
packet = []
first_in_pair = []
indecies = 0
switch = True

with open('ExampleData.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n':
            packet_pairs.append(packet)
            packet = []
        else:
            packet += line.replace(",", "",).replace("[", "").replace("]", "").strip()

for index_packet_pair, packet in enumerate(packet_pairs):
    if not switch:
        print(index_packet_pair)
        indecies += index_packet_pair
    if index_packet_pair % 2 == 0:
        first_in_pair = packet
        continue
    switch = False
    for index, num in enumerate(packet):
        if num < first_in_pair[index]:
            switch = True
            break
print(indecies)