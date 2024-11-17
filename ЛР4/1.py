# TODO решите задачу
def ochki(data_vhod) -> float:
    import json
    with open(data_vhod) as f:
        data = json.load(f)
    for i in range(len(data)):
        data[i] = data[i]["score"]*data[i]["weight"]
    s = round(sum(data), 3)
    return s
print(ochki("input.json"))
