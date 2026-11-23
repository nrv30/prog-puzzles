import sys

if len(sys.argv) < 2:
    print("forgot input file")

with open(sys.argv[1]) as f:
    content = f.read()

lines = content.split('\n')
ids = set()
for line in lines:
    _, num_id, _ = line.split(' ')
    num_id = int(num_id[num_id.index('#') + 1:])
    ids.add(num_id)

id_count = len(ids)
cell_states = [None] * id_count

last_time = 0
longest_donwtime = 0
for line in lines:
    time, num_id, status = line.split(' ')
    num_id = int(num_id[num_id.index('#') + 1:])
    time = int(time[time.index('=') + 1:])
    if cell_states[num_id] == None:
        cell_states[num_id] = [time, False]
    else:
        if cell_states[num_id][1] == False:
            downtime = time - cell_states[num_id][0]
            cell_states[num_id][0] = time
            if downtime > longest_donwtime:
                longest_donwtime = downtime
        else:
            cell_states[num_id[1]] = True
    last_time = time

for cell in cell_states:
    if cell[1] == False:
        downtime = (last_time + 1) - cell[0]
        if downtime > longest_donwtime:
            longest_donwtime = downtime

print (f"Part 1: {longest_donwtime}")
        

