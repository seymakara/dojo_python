x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(x):
    for i in x:
        if type(i) == int:
            print "*" * i
        elif type(i) == str:
            print i[0].lower() * len(i)
draw_stars(x)
