def find_it(seq):
    for item in seq:
        count = seq.count(item)
        if count % 2 != 0:
            return item




find_it([0,1,0,1,0])