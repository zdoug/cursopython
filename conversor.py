print("Bienvenido al conversor de millas a kilómetros")
print("Escribe un numero em millas:")

millas = input()
print("Tipo de dato de millas:", type(millas))
# Convertir de string a numero
millas = float(millas)
print("Tipo de dato de millas:", type(millas))

# 1 milla = 1.609km
kilometros = millas * 1.609

print("Millas ingresadas:", kilometros)