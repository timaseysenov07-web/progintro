def circle_area(d):
    result = 3.1415*(d/2)**2
    return result

def tube_cross_section(d_out, d_in,):
    tube_area = circle_area(d_out) - circle_area(d_in)
    return tube_area
def tube_mass(d_out, d_in, length , density = 7850):
    tube_area = tube_cross_section(d_out, d_in)
    mass = tube_area * length * density
    return mass

print(circle_area(10))

result = circle_area(10)
print(result)
print(tube_mass(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg