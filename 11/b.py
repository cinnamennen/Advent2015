import string, re

word = 'hepxcrrq'

master = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l',
          'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
          'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
lookup = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k', 'k': 'm', 'm': 'n',
          'n': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
          'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}

wrong_answers = ['hepxxyzz','hepyyzaa']

def valid(s):
    if s in wrong_answers :
        return False
    if len(s) < 3:
        # print "  Too short"
        return False
    if 'i' in s or 'o' in s or 'l' in s:
        # print "  Bad letter"
        return False
    search = re.search(
        r".*(\w)\1.*(\w)\2.*", s)
    if search is None:
        # print "  Bad search"
        return False
    else:
        handle = []
        handle += s
        for j in range(0, len(handle) - 2):
            if handle[j] in ('y','z'):
                return False
            if master[handle[j]] == handle[j + 1] and master[handle[j + 1]] == handle[j + 2]:
                print '  seq: ' + str(handle[j]) + str(handle[j+1]) + str(handle[j+2])
                return True
    # print("  General fail")
    #     return False
    return False


def increment(s):
    # #print s

    handle = []
    handle += s
    # #print "Handle is:"
    # #print handle

    done = False
    j = len(handle) - 1
    while not done:
        if handle[j] in master and handle[j] not in lookup:
            # print "Need to skip"
            handle[j] = master[handle[j]]
        else:
            if handle[j] == 'z':
                found_z = False
                for k in range(j - 1, 0 - 1, -1):
                    if handle[k] != 'z':
                        found_z = True
                if not found_z:
                    # print "  Can't go higher"
                    exit()
            handle[j] = lookup[handle[j]]
        if handle[j] == 'a':
            j -= 1
            if j < 0:
                done = True
        else:
            break

    return string.join(handle, '')


    # if 'i' in word or 'o' in word or 'l' in word:
    #     # #print "jumping " + s
    #     my_set = [word.find('i'), word.find('o'), word.find('l')]
    #     w = word
    #     w = w.replace('i', 'j')
    #     w = w.replace('o', 'p')
    #     w = w.replace('l', 'm')
    #
    #     for n, i in enumerate(my_set):
    #         if i == -1:
    #             my_set[n] = 100000
    #
    #     start_point = min(my_set) + 1
    #     #print "starting at " + str(start_point)
    #     word = []
    #     word += w
    #
    #     for j in range(start_point, len(word)):
    #         word[j] = 'a'
    #     word = string.join(word, '')
    # print "prepped word is " + word


# word = increment(word)
print "changed to " + word
while not valid(word):
    word = increment(word)
    # #print "--"
    # print word
print word
