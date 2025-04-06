example = "S;M;plasticCup()"

splitted = example.split(";")
if splitted[0] == "S":
    if splitted[1] == "M":
        without_brackets = splitted[-1][0:-2]
        start_indices = [x for x,y in enumerate (without_brackets) if y.isupper()]+[len(without_brackets)]
        start_indices = [0] + start_indices
        print([without_brackets[x:y] for x,y in zip(start_indices, start_indices[1:])])