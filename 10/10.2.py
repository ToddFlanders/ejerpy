listaComida = ["pan", "vino", "caracol", "sandia"]
list5 = []
errores =[]

for comidas in listaComida:
    try:
        list5.append(comidas[4])
    except IndexError:
        errores.append(comidas)
        continue
print(f""" 
Lista original: 
{listaComida}

Lista con la 5 letra: 
{list5}

Las siguientes palabras no han podido introducirse en la lista anterior:
{errores}
""")