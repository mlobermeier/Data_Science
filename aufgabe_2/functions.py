def find_unique(array):
    counts = {}
    result = 0
    for i in array:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    for k, v in counts.items():
        if v == 1:
            result = k
            return result
    if len(array) % 2 == 0:
        raise ValueError("Array muss ungerade Länge haben")
    if result == 0:
        raise ValueError("Kein eindeutiges Element gefunden")
