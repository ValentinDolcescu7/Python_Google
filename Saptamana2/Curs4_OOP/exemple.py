from forme import Cerc, Dreptunghi

cerc1 = Cerc(raza=1)
cerc2 = Cerc(raza=2)
cerc3 = Cerc(raza=3)

print(set([cerc1, cerc2, cerc3]))

print(Dreptunghi.e_patrat(3, 4))
print(Dreptunghi.e_patrat(4, 4))

del(cerc3)