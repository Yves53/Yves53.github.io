def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            for j in range(0, i):
                print "*",
            print ''
        else:
            for k in range(0, len(i)):
                print i[0].lower(),
            print ''


draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
