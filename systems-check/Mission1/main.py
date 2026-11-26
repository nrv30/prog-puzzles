import sys

if len(sys.argv) < 2:
    print("forgot input file")

with open(sys.argv[1]) as f:
    content = f.read()

lines = content.split('\n')
ids = set()
# count the unique ids in advnace so we can use parallel array
for line in lines:
    _, num_id, _ = line.split(' ')
    num_id = int(num_id[num_id.index('#') + 1:])
    ids.add(num_id)

id_count = len(ids)
cell_states = [None] * id_count

disabled_at_time = {}

last_time = 0
longest_single_downtime = 0

for line in lines:
    time, num_id, status = line.split(' ')
    num_id = int(num_id[num_id.index('#') + 1:])
    time = int(time[time.index('=') + 1:])
    if cell_states[num_id] == None:
        cell_states[num_id] = [time, False]
    else:
        # We are enabling it
        if cell_states[num_id][1] == False:
            downtime = time - cell_states[num_id][0]
            longest_single_downtime = max(downtime, longest_single_downtime)
            cell_states[num_id][1] = True
        # We are disabling it
        else:
            cell_states[num_id][0] = time
            cell_states[num_id][1] = False
    last_time = time

    def isDown(cell):
        return cell is not None and not cell[1]

    down_cells = list(filter(isDown, cell_states))
    down_count = len(down_cells)

    disabled_at_time[time] = down_count

for cell in cell_states:
    if cell[1] == False:
        downtime = (last_time + 1) - cell[0]
        longest_single_downtime = max(downtime, longest_single_downtime)

print (f"Part 1: {longest_single_downtime}")

max_key  = max(disabled_at_time, key=disabled_at_time.get)
max_disabled = disabled_at_time[max_key]

max_ = 0
start_t = -1
for k in sorted(disabled_at_time.keys()):
    val = disabled_at_time[k]
    if val == max_disabled:
        start_t = k
    elif start_t != -1:
        max_ = max(max_, k - start_t)
        start_t = -1
print(f"Part 2 is {max_}")

