print("HELLO WORD")

from clases import Partido

partido1 = Partido("A", "B", 100, 101)
partido2 = Partido("C", "D", 99, 98)

print(partido1.__str__())
print(partido1.get_contador(Partido))