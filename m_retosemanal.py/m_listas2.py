# Importamos el módulo que creamos
import m_listas as ml

print("=== PROGRAMA DE FILTRADO DE LISTAS EN MÓDULOS ===")

# 2 y 3. El usuario especifica cuántas listas quiere y la longitud de cada una
listas_originales = ml.crear_listas()

# 4. Imprime las listas e indica que son las originales
ml.imprimir_listas(listas_originales, "Listas Originales")

# 5. Se eliminan los elementos de una lista que estén también en las listas posteriores
listas_filtradas = ml.eliminar_elementos_posteriores(listas_originales)

# 6. Imprime las listas indicando que se eliminaron los elementos de listas posteriores
ml# Importamos el módulo que creamos
