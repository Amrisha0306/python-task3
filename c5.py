W= input('Please enter a string: ')

def most_frequent(string, reverse= False):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

print (most_frequent(W, True))
