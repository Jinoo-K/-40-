import itertools

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range (1,4) :
    to_attempt = itertools.product(passwd_string, repeat=i)
    for attempt in to_attempt :
        passwd = ''.join(attempt)
        print(passwd)