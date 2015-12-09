import hashlib

secret = "iwrupvqb"
counter = 0


def my_hash(seed):
    m = hashlib.md5()
    m.update(seed)
    return m.hexdigest()


while my_hash(secret + str(counter)).startswith('00000') is False:
    counter += 1

print counter