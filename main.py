class Day:
    def __init__(self, name, sch):
        self.name = name;
        self.sch = sch;

    def __str__(self):
        return f"{self.name}: {', '.join(self.sch)}"

class Week:
    def __init__(self):
        self.days = [Day("Mon", ["a", "b"]),
                     Day("Thu", ["u", "b"]),
                     Day("Wed", ["uf", "j"]),
                     Day("Thr", ["uv", "ur"]),
                     Day("Fri", ["cu", "tj"]),
                     Day("Sat", ["air", "binf"]),
                     Day("Sun", ["jd", "b"])]

    def __iter__(self):
        return iter(self.days)

w = Week()
for i in w:
    print(i)