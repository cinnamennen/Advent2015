__author__ = 'caleb'

debug = False
on = 1
off = 0
grid_size = 100
input_file = 'a.txt'
frames = 100

lights = [[off for y in range(grid_size)] for x in range(grid_size)]

with open(input_file) as f:
    lines = f.readlines()
i = 0
for line in lines:
    for j in range(len(line)):
        if line[j] == '#':
            lights[i][j] = on
    i += 1

good_update = [[None for y in range(grid_size)] for x in range(grid_size)]
update = good_update
# print update


def neighbors(n_i, n_j):
    total_on = 0
    for n_x in range(-1, 2):
        my_x = n_x + n_i
        for n_y in range(-1, 2):
            my_y = n_y + n_j
            if my_x < 0 or my_y < 0 or my_x >= grid_size or my_y >= grid_size:
                if debug:
                    print "bad range: my_x: " + str(my_x) + " my_y: " + str(my_y)
                continue
            elif my_x == n_i and my_y == n_j:
                if debug:
                    print "looking at self"
                continue
            elif lights[my_x][my_y] == on:
                if debug:
                    print "adding"
                total_on += 1
                # else:
                # print "nothing happened"
    return total_on


for iteration in range(frames):
    update = good_update
    for a in range(grid_size):
        for b in range(grid_size):
            num_on = neighbors(a, b)
            if lights[a][b] == on:
                if num_on == 2 or num_on == 3:
                    update[a][b] = on
                    if debug:
                        print "{0},{1} should be {2}".format(a, b, 'on')
                else:
                    update[a][b] = off
                    if debug:
                        print "Only " + str(num_on) + " lights were on"
                        print "{0},{1} should be {2}".format(a, b, 'off')

            else:
                if num_on == 3:
                    update[a][b] = on
                    if debug:
                        print "{0},{1} should be {2}".format(a, b, 'on')

                else:
                    if debug:
                        print "Only " + str(num_on) + " lights were on"
                        print "{0},{1} should be {2}".format(a, b, 'off')

                    update[a][b] = off

    for a in range(grid_size):
        for b in range(grid_size):
            if update[a][b] is None:
                if debug:
                    print 'skipping'
            else:
                lights[a][b] = update[a][b]

                # print update[a][b],
        # print ''

print sum(sum(l) for l in lights)