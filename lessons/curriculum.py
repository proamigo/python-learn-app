"""
Curriculum progresivo: Principiante → Intermedio.
Cada lección: id, title, theory (markdown), examples[], exercise{}.
"""
CURRICULUM = [
    {
        "id": "basico",
        "title": "🟢 Módulo 1: Fundamentos",
        "lessons": [
            {
                "id": "variables",
                "title": "1. Variables y tipos de datos",
                "theory": """
[color=#4ec9b0]Variables[/color] son contenedores con nombre para guardar valores.
Python infiere el tipo automáticamente (tipado dinámico).

[color=#dcdcaa]Tipos básicos:[/color]
• [color=#b5cea8]int[/color] — números enteros: [color=#b5cea8]42[/color], [color=#b5cea8]-7[/color]
• [color=#b5cea8]float[/color] — decimales: [color=#b5cea8]3.14[/color], [color=#b5cea8]-0.5[/color]
• [color=#b5cea8]str[/color] — texto: [color=#ce9178]"hola"[/color], [color=#ce9178]'mundo'[/color]
• [color=#b5cea8]bool[/color] — verdaderos/falsos: [color=#569cd6]True[/color], [color=#569cd6]False[/color]
                """,
                "examples": [
                    {
                        "code": "# Asignación simple\nnombre = \"Alejandro\"\nedad = 28\naltura = 1.75\nes_estudiante = True\n\nprint(nombre, edad, altura, es_estudiante)",
                        "explanation": "Asignamos 4 variables de distintos tipos e imprimimos todas."
                    },
                    {
                        "code": "# type() revela el tipo\nprint(type(42))\nprint(type(3.14))\nprint(type(\"hola\"))\nprint(type(True))",
                        "explanation": "Usa [color=#dcdcaa]type()[/color] para inspeccionar el tipo en tiempo de ejecución."
                    }
                ],
                "exercise": {
                    "prompt": "Crea variables: tu_nombre (str), tu_edad (int), tu_altura (float). Imprímelas con print().",
                    "solution": "tu_nombre = \"Tu Nombre\"\ntu_edad = 25\ntu_altura = 1.70\nprint(tu_nombre, tu_edad, tu_altura)"
                }
            },
            {
                "id": "operadores",
                "title": "2. Operadores y expresiones",
                "theory": """
[color=#dcdcaa]Operadores aritméticos:[/color] [color=#b5cea8]+[/color] [color=#b5cea8]-[/color] [color=#b5cea8]*[/color] [color=#b5cea8]/[/color] [color=#b5cea8]//[/color] (división entera) [color=#b5cea8]%[/color] (módulo) [color=#b5cea8]**[/color] (potencia)

[color=#dcdcaa]Comparación:[/color] [color=#b5cea8]==[/color] [color=#b5cea8]!=[/color] [color=#b5cea8]<[/color] [color=#b5cea8]>[/color] [color=#b5cea8]<=[/color] [color=#b5cea8]>=[/color] → devuelven [color=#569cd6]True/False[/color]

[color=#dcdcaa]Lógicos:[/color] [color=#569cd6]and[/color] [color=#569cd6]or[/color] [color=#569cd6]not[/color]
                """,
                "examples": [
                    {
                        "code": "a = 10\nb = 3\nprint(a + b)   # 13\nprint(a - b)   # 7\nprint(a * b)   # 30\nprint(a / b)   # 3.333...\nprint(a // b)  # 3\nprint(a % b)   # 1\nprint(a ** b)  # 1000",
                        "explanation": "Todos los operadores aritméticos con enteros."
                    },
                    {
                        "code": "edad = 20\ntiene_licencia = True\n\npuede_conducir = edad >= 18 and tiene_licencia\nprint(puede_conducir)  # True",
                        "explanation": "Combinando comparación y operador lógico [color=#569cd6]and[/color]."
                    }
                ],
                "exercise": {
                    "prompt": "Dados a=17, b=5. Calcula: división entera, módulo, potencia. Imprime los 3 resultados.",
                    "solution": "a = 17\nb = 5\nprint(a // b)  # 3\nprint(a % b)   # 2\nprint(a ** b)  # 1419857"
                }
            },
            {
                "id": "strings",
                "title": "3. Cadenas de texto (strings)",
                "theory": """
[color=#ce9178]Strings[/color] son inmutables. Se definen con comillas simples o dobles.

[color=#dcdcaa]Métodos útiles:[/color]
• [color=#4ec9b0].upper()[/color] / [color=#4ec9b0].lower()[/color] — mayúsculas/minúsculas
• [color=#4ec9b0].strip()[/color] — quita espacios extremos
• [color=#4ec9b0].replace(viejo, nuevo)[/color] — reemplaza
• [color=#4ec9b0].split(sep)[/color] — divide en lista
• [color=#4ec9b0]f\"{variable}\"[/color] — f-strings (formato moderno)
                """,
                "examples": [
                    {
                        "code": "nombre = \"  python  \"\nprint(nombre.strip())        # \"python\"\nprint(nombre.upper())        # \"  PYTHON  \"\nprint(nombre.replace('p', 'P'))  # \"  Python  \"",
                        "explanation": "Métodos de limpieza y transformación."
                    },
                    {
                        "code": "lenguaje = \"Python\"\nversion = 3.11\nmensaje = f\"Aprendiendo {lenguaje} {version}\"\nprint(mensaje)  # Aprendiendo Python 3.11",
                        "explanation": "[color=#dcdcaa]f-strings[/color] — la forma recomendada de interpolar variables."
                    }
                ],
                "exercise": {
                    "prompt": "Dado nombre = \"  ALEJANDRO  \", obtén: 1) sin espacios, 2) minúsculas, 3) primera letra mayúscula. Imprime los 3.",
                    "solution": "nombre = \"  ALEJANDRO  \"\nlimpio = nombre.strip()\nprint(limpio.lower())\nprint(limpio.capitalize())"
                }
            },
            {
                "id": "listas",
                "title": "4. Listas y tuplas",
                "theory": """
[color=#dcdcaa]Listas[/color] — mutables, ordenadas, [color=#b5cea8][1, 2, 3][/color]
[color=#dcdcaa]Tuplas[/color] — inmutables, [color=#b5cea8](1, 2, 3)[/color]

[color=#dcdcaa]Operaciones listas:[/color]
• [color=#4ec9b0].append(x)[/color], [color=#4ec9b0].extend([...])[/color] — agregar
• [color=#4ec9b0].pop(i)[/color], [color=#4ec9b0].remove(x)[/color] — quitar
• [color=#4ec9b0]len(lista)[/color] — longitud
• [color=#4ec9b0]lista[i][/color] — índice (0-based), negativos = desde el final
• [color=#4ec9b0]lista[inicio:fin][/color] — rebanado (slicing)
                """,
                "examples": [
                    {
                        "code": "numeros = [1, 2, 3, 4, 5]\nprint(numeros[0])      # 1\nprint(numeros[-1])     # 5\nprint(numeros[1:4])    # [2, 3, 4]\nprint(numeros[::2])    # [1, 3, 5] (cada 2)",
                        "explanation": "Indexado y slicing: [inicio:fin:paso]."
                    },
                    {
                        "code": "frutas = [\"manzana\", \"banana\"]\nfrutas.append(\"naranja\")\nfrutas.insert(1, \"uva\")\nprint(frutas)  # ['manzana', 'uva', 'banana', 'naranja']",
                        "explanation": "Métodos de mutación: append, insert."
                    }
                ],
                "exercise": {
                    "prompt": "Crea lista numeros = [10, 20, 30, 40, 50]. Obtén sublista del 2º al 4º elemento. Agrega 60 al final. Imprime lista final y su longitud.",
                    "solution": "numeros = [10, 20, 30, 40, 50]\nsublista = numeros[1:4]  # [20, 30, 40]\nnumeros.append(60)\nprint(numeros)      # [10, 20, 30, 40, 50, 60]\nprint(len(numeros)) # 6"
                }
            },
            {
                "id": "diccionarios",
                "title": "5. Diccionarios y conjuntos",
                "theory": """
[color=#dcdcaa]Dict[/color] — clave:valor, [color=#b5cea8]{"nombre": "Ana", "edad": 25}[/color]
• [color=#4ec9b0]d["clave"][/color] — acceso (KeyError si no existe)
• [color=#4ec9b0]d.get("clave", default)[/color] — seguro
• [color=#4ec9b0]d.keys() / d.values() / d.items()[/color]

[color=#dcdcaa]Set[/color] — únicos, sin orden, [color=#b5cea8]{1, 2, 3}[/color]
• [color=#4ec9b0].add()[/color], [color=#4ec9b0].remove()[/color]
• Operaciones: [color=#b5cea8]union |[/color], [color=#b5cea8]intersección &[/color], [color=#b5cea8]diferencia -[/color]
                """,
                "examples": [
                    {
                        "code": "persona = {\"nombre\": \"Luis\", \"edad\": 30, \"ciudad\": \"Madrid\"}\nprint(persona[\"nombre\"])      # Luis\nprint(persona.get(\"pais\", \"?\"))  # ?\npersona[\"edad\"] = 31\npersona[\"profesion\"] = \"dev\"\nprint(persona)",
                        "explanation": "Acceso, get seguro, mutación y adición de claves."
                    },
                    {
                        "code": "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a | b)  # {1, 2, 3, 4, 5, 6}\nprint(a & b)  # {3, 4}\nprint(a - b)  # {1, 2}",
                        "explanation": "Operaciones de conjuntos: unión, intersección, diferencia."
                    }
                ],
                "exercise": {
                    "prompt": "Crea dict contacto = {\"email\": \"a@b.com\", \"tel\": \"123\"}. Agrega clave \"direccion\". Imprime claves, valores y items por separado.",
                    "solution": "contacto = {\"email\": \"a@b.com\", \"tel\": \"123\"}\ncontacto[\"direccion\"] = \"Calle Falsa 123\"\nprint(list(contacto.keys()))\nprint(list(contacto.values()))\nprint(list(contacto.items()))"
                }
            }
        ]
    },
    {
        "id": "control",
        "title": "🟡 Módulo 2: Control de Flujo",
        "lessons": [
            {
                "id": "condicionales",
                "title": "6. Condicionales if/elif/else",
                "theory": """
[color=#569cd6]if[/color] [color=#dcdcaa]condición:[/color]
    [color=#4ec9b0]bloque[/color]
[color=#569cd6]elif[/color] [color=#dcdcaa]otra_condición:[/color]
    [color=#4ec9b0]bloque[/color]
[color=#569cd6]else:[/color]
    [color=#4ec9b0]bloque[/color]

[color=#ce9178]Indentación (4 espacios) define los bloques.[/color] No llaves {}.

Expresiones ternarias: [color=#dcdcaa]x if cond else y[/color]
                """,
                "examples": [
                    {
                        "code": "nota = 85\nif nota >= 90:\n    print(\"Excelente\")\nelif nota >= 70:\n    print(\"Bien\")\nelse:\n    print(\"Mejorable\")",
                        "explanation": "Cadena if/elif/else evaluada en orden."
                    },
                    {
                        "code": "edad = 17\nestado = \"mayor\" if edad >= 18 else \"menor\"\nprint(estado)  # menor",
                        "explanation": "Expresión condicional en una línea."
                    }
                ],
                "exercise": {
                    "prompt": "Dado numero = -5. Imprime: \"positivo\", \"negativo\" o \"cero\" según su valor.",
                    "solution": "numero = -5\nif numero > 0:\n    print(\"positivo\")\nelif numero < 0:\n    print(\"negativo\")\nelse:\n    print(\"cero\")"
                }
            },
            {
                "id": "bucles_for",
                "title": "7. Bucles for e iterables",
                "theory": """
[color=#569cd6]for[/color] [color=#dcdcaa]variable[/color] [color=#569cd6]in[/color] [color=#dcdcaa]iterable:[/color]
    [color=#4ec9b0]bloque[/color]

Iterables: listas, tuplas, strings, dicts, [color=#4ec9b0]range()[/color], generadores.

[color=#dcdcaa]range(inicio, fin, paso)[/color] — genera secuencia.
• [color=#4ec9b0]break[/color] — sale del bucle
• [color=#4ec9b0]continue[/color] — salta a siguiente iteración
• [color=#4ec9b0]else[/color] del bucle — se ejecuta si NO hubo break
                """,
                "examples": [
                    {
                        "code": "for i in range(5):\n    print(i)  # 0 1 2 3 4\n\nfor i in range(2, 10, 2):\n    print(i)  # 2 4 6 8",
                        "explanation": "[color=#4ec9b0]range()[/color] con 1, 2 y 3 argumentos."
                    },
                    {
                        "code": "frutas = [\"manzana\", \"banana\", \"cereza\"]\nfor i, fruta in enumerate(frutas):\n    print(f\"{i}: {fruta}\")",
                        "explanation": "[color=#4ec9b0]enumerate()[/color] da índice + valor."
                    }
                ],
                "exercise": {
                    "prompt": "Usa range para imprimir números pares del 2 al 20 (inclusive). Usa step=2.",
                    "solution": "for i in range(2, 21, 2):\n    print(i)"
                }
            },
            {
                "id": "bucles_while",
                "title": "8. Bucles while y control",
                "theory": """
[color=#569cd6]while[/color] [color=#dcdcaa]condición:[/color]
    [color=#4ec9b0]bloque[/color]

Se repite mientras la condición sea [color=#569cd6]True[/color].
¡Cuidado con bucles infinitos! Usa [color=#4ec9b0]break[/color] para salir.

Patrón común: [color=#569cd6]while True:[/color] + [color=#4ec9b0]break[/color] condicional.
                """,
                "examples": [
                    {
                        "code": "contador = 0\nwhile contador < 5:\n    print(contador)\n    contador += 1",
                        "explanation": "Bucle while clásico con variable de control."
                    },
                    {
                        "code": "import random\nsecreto = random.randint(1, 10)\nwhile True:\n    guess = int(input(\"Adivina (1-10): \"))\n    if guess == secreto:\n        print(\"¡Correcto!\")\n        break\n    print(\"Intenta de nuevo\")",
                        "explanation": "Patrón while True + break para menús/juegos."
                    }
                ],
                "exercise": {
                    "prompt": "Escribe un while que sume números del 1 al 100 e imprima el total. (Pista: usa contador y acumulador).",
                    "solution": "suma = 0\ni = 1\nwhile i <= 100:\n    suma += i\n    i += 1\nprint(suma)  # 5050"
                }
            },
            {
                "id": "comprehensions",
                "title": "9. Comprensiones (list/dict/set)",
                "theory": """
Sintaxis compacta para crear colecciones transformando/filtrando.

[color=#dcdcaa]Lista:[/color] [color=#b5cea8][expr for x in iterable if cond][/color]
[color=#dcdcaa]Dict:[/color] [color=#b5cea8]{k: v for x in iterable}[/color]
[color=#dcdcaa]Set:[/color] [color=#b5cea8]{expr for x in iterable}[/color]

Equivalen a bucles for + append, más legibles y rápidas.
                """,
                "examples": [
                    {
                        "code": "# Cuadrados del 1 al 10\ncuadrados = [x**2 for x in range(1, 11)]\nprint(cuadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]",
                        "explanation": "Comprensión de lista básica."
                    },
                    {
                        "code": "# Solo pares\npares = [x for x in range(20) if x % 2 == 0]\nprint(pares)  # [0, 2, 4, ..., 18]",
                        "explanation": "Filtrado con [color=#569cd6]if[/color] al final."
                    },
                    {
                        "code": "# Dict: longitud de palabras\npalabras = [\"hola\", \"mundo\", \"python\"]\nlongitudes = {p: len(p) for p in palabras}\nprint(longitudes)  # {'hola': 4, 'mundo': 5, 'python': 6}",
                        "explanation": "Comprensión de diccionario."
                    }
                ],
                "exercise": {
                    "prompt": "Dada lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Crea nueva lista con cubos (x**3) de solo los números impares.",
                    "solution": "lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ncubos_impares = [x**3 for x in lista if x % 2 != 0]\nprint(cubos_impares)  # [1, 27, 125, 343, 729]"
                }
            }
        ]
    },
    {
        "id": "funciones",
        "title": "🟠 Módulo 3: Funciones",
        "lessons": [
            {
                "id": "definir_funciones",
                "title": "10. Definir y llamar funciones",
                "theory": """
[color=#569cd6]def[/color] [color=#dcdcaa]nombre[/color]([color=#9cdcfe]parámetros[/color]):
    [color=#6a9955]\"\"\"Docstring opcional\"\"\"[/color]
    [color=#4ec9b0]cuerpo[/color]
    [color=#569cd6]return[/color] [color=#dcdcaa]valor[/color]

• Parámetros posicionales y por palabra clave
• Valores por defecto: [color=#dcdcaa]def f(x=0):[/color]
• [color=#569cd6]return[/color] sin valor → [color=#569cd6]None[/color]
• Docstring: documenta qué hace, parámetros, retorno
                """,
                "examples": [
                    {
                        "code": "def saludar(nombre, saludo=\"Hola\"):\n    \"\"\"Saluda a una persona.\"\"\"\n    return f\"{saludo}, {nombre}!\"\n\nprint(saludar(\"Ana\"))           # Hola, Ana!\nprint(saludar(\"Luis\", \"Hey\"))  # Hey, Luis!",
                        "explanation": "Parámetro con valor por defecto + f-string en retorno."
                    },
                    {
                        "code": "def dividir(a, b):\n    if b == 0:\n        return None\n    return a / b\n\nresultado = dividir(10, 2)\nprint(resultado)  # 5.0",
                        "explanation": "Validación y retorno temprano con [color=#569cd6]None[/color]."
                    }
                ],
                "exercise": {
                    "prompt": "Escribe función es_par(n) que retorne True si n es par, False si impar. Prueba con 4 y 7.",
                    "solution": "def es_par(n):\n    return n % 2 == 0\n\nprint(es_par(4))  # True\nprint(es_par(7))  # False"
                }
            },
            {
                "id": "args_kwargs",
                "title": "11. *args y **kwargs",
                "theory": """
[color=#dcdcaa]*args[/color] — tupla de argumentos posicionales extra
[color=#dcdcaa]**kwargs[/color] — dict de argumentos por palabra clave extra

Orden: [color=#569cd6]def f(pos, *args, kw=val, **kwargs):[/color]

Útil para funciones flexibles, wrappers, decoradores.
                """,
                "examples": [
                    {
                        "code": "def suma_todos(*args):\n    total = 0\n    for n in args:\n        total += n\n    return total\n\nprint(suma_todos(1, 2, 3))      # 6\nprint(suma_todos(10, 20, 30, 40))  # 100",
                        "explanation": "[color=#dcdcaa]*args[/color] captura cualquier cantidad de posicionales."
                    },
                    {
                        "code": "def configurar(**kwargs):\n    for clave, valor in kwargs.items():\n        print(f\"{clave} = {valor}\")\n\nconfigurar(host=\"localhost\", puerto=8080, debug=True)",
                        "explanation": "[color=#dcdcaa]**kwargs[/color] captura kwargs como diccionario."
                    }
                ],
                "exercise": {
                    "prompt": "Escribe función multiplicar(*args) que retorne el producto de todos sus argumentos. Si no hay args, retorna 1.",
                    "solution": "def multiplicar(*args):\n    resultado = 1\n    for n in args:\n        resultado *= n\n    return resultado\n\nprint(multiplicar(2, 3, 4))  # 24\nprint(multiplicar())         # 1"
                }
            },
            {
                "id": "lambdas",
                "title": "12. Funciones lambda y funciones de orden superior",
                "theory": """
[color=#dcdcaa]lambda[/color] — funciones anónimas de una expresión:
[color=#b5cea8]lambda x, y: x + y[/color]

[color=#dcdcaa]Funciones de orden superior[/color] — toman/retornan funciones:
• [color=#4ec9b0]map(fn, iterable)[/color] — aplica fn a cada elemento
• [color=#4ec9b0]filter(fn, iterable)[/color] — filtra elementos donde fn es True
• [color=#4ec9b0]sorted(iterable, key=fn)[/color] — ordena con clave personalizada
                """,
                "examples": [
                    {
                        "code": "doble = lambda x: x * 2\nprint(doble(5))  # 10",
                        "explanation": "Lambda simple asignada a variable."
                    },
                    {
                        "code": "numeros = [1, 2, 3, 4, 5, 6]\npares = list(filter(lambda x: x % 2 == 0, numeros))\nprint(pares)  # [2, 4, 6]",
                        "explanation": "[color=#4ec9b0]filter[/color] + lambda para filtrar."
                    },
                    {
                        "code": "palabras = [\"casa\", \"sol\", \"programacion\", \"py\"]\nordenadas = sorted(palabras, key=lambda s: len(s))\nprint(ordenadas)  # ['py', 'sol', 'casa', 'programacion']",
                        "explanation": "[color=#4ec9b0]sorted[/color] con key=lambda para criterio personalizado."
                    }
                ],
                "exercise": {
                    "prompt": "Dada lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Usa map + lambda para obtener lista de cuadrados. Usa filter + lambda para quedarte con > 20.",
                    "solution": "lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ncuadrados = list(map(lambda x: x**2, lista))\nprint(cuadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\nmayores_20 = list(filter(lambda x: x > 20, cuadrados))\nprint(mayores_20)  # [25, 36, 49, 64, 81, 100]"
                }
            }
        ]
    },
    {
        "id": "poo",
        "title": "🔴 Módulo 4: Programación Orientada a Objetos",
        "lessons": [
            {
                "id": "clases_objetos",
                "title": "13. Clases, objetos y __init__",
                "theory": """
[color=#569cd6]class[/color] [color=#dcdcaa]Nombre:[/color] define un tipo.
[color=#dcdcaa]__init__(self, ...)[/color] — inicializador (constructor).
[color=#dcdcaa]self[/color] — referencia a la instancia actual.

Atributos: [color=#dcdcaa]self.attr = valor[/color]
Métodos: funciones dentro de la clase con [color=#dcdcaa]self[/color] como primer parámetro.
                """,
                "examples": [
                    {
                        "code": "class Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad\n    \n    def saludar(self):\n        return f\"Hola, soy {self.nombre} y tengo {self.edad} años\"\n\np = Persona(\"Carlos\", 30)\nprint(p.saludar())  # Hola, soy Carlos y tengo 30 años",
                        "explanation": "Clase básica con atributos y método de instancia."
                    }
                ],
                "exercise": {
                    "prompt": "Crea clase Rectangulo con __init__(base, altura) y metodo area() que retorne base * altura. Crea instancia y muestra su área.",
                    "solution": "class Rectangulo:\n    def __init__(self, base, altura):\n        self.base = base\n        self.altura = altura\n    \n    def area(self):\n        return self.base * self.altura\n\nr = Rectangulo(5, 3)\nprint(r.area())  # 15"
                }
            },
            {
                "id": "herencia",
                "title": "14. Herencia y polimorfismo",
                "theory": """
[color=#569cd6]class Hija(Padre):[/color] — hereda atributos y métodos.
[color=#569cd6]super()[/color] — llama a método del padre.
Sobrescritura: redefinir método en hija.

[color=#dcdcaa]Polimorfismo[/color] — mismo nombre, comportamiento distinto según tipo.
                """,
                "examples": [
                    {
                        "code": "class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    def sonido(self):\n        return \"...\"\n\nclass Perro(Animal):\n    def sonido(self):\n        return \"Guau!\"\n\nclass Gato(Animal):\n    def sonido(self):\n        return \"Miau!\"\n\nfor a in [Perro(\"Rex\"), Gato(\"Mishi\")]:\n    print(f\"{a.nombre}: {a.sonido()}\")",
                        "explanation": "Herencia + sobrescritura + polimorfismo en bucle."
                    }
                ],
                "exercise": {
                    "prompt": "Crea clase Vehiculo con __init__(marca, velocidad=0) y acelerar(incremento). Crea clase Coche(Vehiculo) que sobrescriba acelerar para sumar el doble del incremento.",
                    "solution": "class Vehiculo:\n    def __init__(self, marca, velocidad=0):\n        self.marca = marca\n        self.velocidad = velocidad\n    def acelerar(self, inc):\n        self.velocidad += inc\n\nclass Coche(Vehiculo):\n    def acelerar(self, inc):\n        self.velocidad += inc * 2\n\nc = Coche(\"Toyota\")\nc.acelerar(10)\nprint(c.velocidad)  # 20"
                }
            },
            {
                "id": "metodos_especiales",
                "title": "15. Métodos especiales (__str__, __repr__, __len__, etc.)",
                "theory": """
Métodos dunder (doble guion) que Python llama automáticamente:
• [color=#4ec9b0]__str__(self)[/color] — str(obj), print(obj)
• [color=#4ec9b0]__repr__(self)[/color] — repr(obj), depuración
• [color=#4ec9b0]__len__(self)[/color] — len(obj)
• [color=#4ec9b0]__getitem__(self, key)[/color] — obj[key]
• [color=#4ec9b0]__eq__(self, other)[/color] — obj1 == obj2
• [color=#4ec9b0]__add__(self, other)[/color] — obj1 + obj2
                """,
                "examples": [
                    {
                        "code": "class Libro:\n    def __init__(self, titulo, autor, paginas):\n        self.titulo = titulo\n        self.autor = autor\n        self.paginas = paginas\n    \n    def __str__(self):\n        return f'\"{self.titulo}\" por {self.autor}'\n    \n    def __len__(self):\n        return self.paginas\n    \n    def __eq__(self, other):\n        return self.titulo == other.titulo and self.autor == other.autor\n\nl1 = Libro(\"1984\", \"Orwell\", 328)\nprint(l1)        # \"1984\" por Orwell\nprint(len(l1))   # 328",
                        "explanation": "__str__, __len__, __eq__ en acción."
                    }
                ],
                "exercise": {
                    "prompt": "Crea clase Pila con lista interna. Implementa __len__, __getitem__, __str__, y metodos push(), pop().",
                    "solution": "class Pila:\n    def __init__(self):\n        self._items = []\n    def push(self, item):\n        self._items.append(item)\n    def pop(self):\n        return self._items.pop()\n    def __len__(self):\n        return len(self._items)\n    def __getitem__(self, i):\n        return self._items[i]\n    def __str__(self):\n        return f'Pila({self._items})'\n\np = Pila()\np.push(1); p.push(2); p.push(3)\nprint(p)      # Pila([1, 2, 3])\nprint(len(p)) # 3\nprint(p[0])   # 1"
                }
            }
        ]
    },
    {
        "id": "archivos",
        "title": "🔵 Módulo 5: Archivos y Excepciones",
        "lessons": [
            {
                "id": "lectura_escritura",
                "title": "16. Leer y escribir archivos",
                "theory": """
[color=#4ec9b0]open(ruta, modo)[/color] — contexto preferido con [color=#569cd6]with[/color]:
[color=#569cd6]with[/color] open(...) as f: — cierra automático.

Modos: [color=#b5cea8]'r'[/color] leer, [color=#b5cea8]'w'[/color] escribir (trunca), [color=#b5cea8]'a'[/color] añadir, [color=#b5cea8]'r+'[/color] leer+escribir.

[color=#dcdcaa]Métodos:[/color]
• [color=#4ec9b0]f.read()[/color] — todo el contenido
• [color=#4ec9b0]f.readline()[/color] — una línea
• [color=#4ec9b0]f.readlines()[/color] — lista de líneas
• [color=#4ec9b0]f.write(str)[/color] — escribe string
• [color=#4ec9b0]f.writelines(lista)[/color] — escribe lista
                """,
                "examples": [
                    {
                        "code": "# Escribir\nwith open(\"notas.txt\", \"w\") as f:\n    f.write(\"Línea 1\\n\")\n    f.write(\"Línea 2\\n\")\n\n# Leer todo\nwith open(\"notas.txt\", \"r\") as f:\n    contenido = f.read()\nprint(contenido)",
                        "explanation": "Escritura y lectura básica con with."
                    },
                    {
                        "code": "# Leer línea a línea\nwith open(\"notas.txt\") as f:\n    for linea in f:\n        print(linea.strip())",
                        "explanation": "Iterar el archivo línea a línea (eficiente en memoria)."
                    }
                ],
                "exercise": {
                    "prompt": "Escribe función contar_palabras(archivo) que abra un archivo, cuente cuántas palabras tiene (split por espacios) y retorne el conteo.",
                    "solution": "def contar_palabras(archivo):\n    with open(archivo, 'r') as f:\n        texto = f.read()\n    palabras = texto.split()\n    return len(palabras)\n\n# Uso (crea un archivo de prueba primero)\nwith open('test.txt', 'w') as f:\n    f.write('hola mundo python')\nprint(contar_palabras('test.txt'))  # 3"
                }
            },
            {
                "id": "excepciones",
                "title": "17. Manejo de excepciones try/except",
                "theory": """
[color=#569cd6]try:[/color]
    [color=#4ec9b0]código riesgoso[/color]
[color=#569cd6]except[/color] [color=#dcdcaa]TipoError[/color] [color=#569cd6]as[/color] [color=#dcdcaa]e:[/color]
    [color=#4ec9b0]manejo[/color]
[color=#569cd6]except[/color] [color=#dcdcaa]OtroError:[/color]
    ...
[color=#569cd6]else:[/color]  # si no hubo excepción
[color=#569cd6]finally:[/color]  # siempre se ejecuta

Excepciones comunes: [color=#b5cea8]ValueError[/color], [color=#b5cea8]FileNotFoundError[/color], [color=#b5cea8]ZeroDivisionError[/color], [color=#b5cea8]KeyError[/color], [color=#b5cea8]IndexError[/color].
                """,
                "examples": [
                    {
                        "code": "def dividir_seguro(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return \"Error: división por cero\"\n    except TypeError:\n        return \"Error: tipos inválidos\"\n\nprint(dividir_seguro(10, 2))   # 5.0\nprint(dividir_seguro(10, 0))   # Error: división por cero\nprint(dividir_seguro(\"10\", 2)) # Error: tipos inválidos",
                        "explanation": "Múltiples except para distintos tipos de error."
                    },
                    {
                        "code": "try:\n    with open(\"no_existe.txt\") as f:\n        print(f.read())\nexcept FileNotFoundError as e:\n    print(f\"Archivo no encontrado: {e}\")\nfinally:\n    print(\"Fin del intento\")",
                        "explanation": "[color=#569cd6]finally[/color] siempre corre, útil para limpieza."
                    }
                ],
                "exercise": {
                    "prompt": "Escribe función leer_entero() que pida input al usuario, intente convertirlo a int, y si falla (ValueError), imprima error y pida de nuevo (bucle while).",
                    "solution": "def leer_entero():\n    while True:\n        try:\n            return int(input(\"Ingresa un entero: \"))\n        except ValueError:\n            print(\"Eso no es un entero válido. Intenta de nuevo.\")\n\n# numero = leer_entero()  # Descomenta para probar"
                }
            },
            {
                "id": "json_csv",
                "title": "18. JSON y CSV — librería estándar",
                "theory": """
[color=#dcdcaa]json[/color] — serialización ligera:
• [color=#4ec9b0]json.dump(obj, archivo)[/color] — escribir
• [color=#4ec9b0]json.load(archivo)[/color] — leer
• [color=#4ec9b0]json.dumps(obj)[/color] — string
• [color=#4ec9b0]json.loads(str)[/color] — parsear string

[color=#dcdcaa]csv[/color] — valores separados por comas:
• [color=#4ec9b0]csv.writer(f)[/color] — escribir filas
• [color=#4ec9b0]csv.reader(f)[/color] — leer filas
• [color=#4ec9b0]csv.DictWriter/Reader[/color] — con diccionarios
                """,
                "examples": [
                    {
                        "code": "import json\n\ndatos = {\"usuario\": \"Ana\", \"puntos\": [10, 20, 30], \"activo\": True}\n\n# Guardar\nwith open(\"datos.json\", \"w\") as f:\n    json.dump(datos, f, indent=2)\n\n# Cargar\nwith open(\"datos.json\") as f:\n    cargado = json.load(f)\nprint(cargado)",
                        "explanation": "JSON nativo para dicts/listas/valores básicos."
                    },
                    {
                        "code": "import csv\n\n# Escribir CSV\nwith open(\"productos.csv\", \"w\", newline='') as f:\n    writer = csv.writer(f)\n    writer.writerow([\"nombre\", \"precio\"])\n    writer.writerow([\"Manzana\", 1.5])\n    writer.writerow([\"Pera\", 2.0])\n\n# Leer CSV\nwith open(\"productos.csv\") as f:\n    reader = csv.DictReader(f)\n    for fila in reader:\n        print(fila)",
                        "explanation": "CSV con DictReader para acceso por nombre de columna."
                    }
                ],
                "exercise": {
                    "prompt": "Crea lista de 3 diccionarios con claves 'producto', 'precio'. Guárdala en JSON. Luego léela y muestra solo los productos con precio > 5.",
                    "solution": "import json\n\nproductos = [\n    {\"producto\": \"A\", \"precio\": 10},\n    {\"producto\": \"B\", \"precio\": 3},\n    {\"producto\": \"C\", \"precio\": 7}\n]\nwith open('prod.json', 'w') as f:\n    json.dump(productos, f)\n\nwith open('prod.json') as f:\n    cargados = json.load(f)\n\nfor p in cargados:\n    if p['precio'] > 5:\n        print(p['producto'], p['precio'])"
                }
            }
        ]
    },
    {
        "id": "stdlib",
        "title": "🟣 Módulo 6: Librería Estándar Útil",
        "lessons": [
            {
                "id": "datetime",
                "title": "19. Fechas y horas — datetime",
                "theory": """
[color=#dcdcaa]from datetime import datetime, date, time, timedelta[/color]

• [color=#4ec9b0]datetime.now()[/color] — ahora local
• [color=#4ec9b0]datetime.strptime(str, fmt)[/color] — parsear string
• [color=#4ec9b0]dt.strftime(fmt)[/color] — formatear a string
• [color=#4ec9b0]timedelta(days=, hours=)[/color] — aritmética de fechas

Formatos: [color=#b5cea8]%Y-%m-%d %H:%M:%S[/color]
                """,
                "examples": [
                    {
                        "code": "from datetime import datetime, timedelta\n\nahora = datetime.now()\nprint(ahora)                    # 2024-01-15 14:30:45.123456\nprint(ahora.strftime(\"%d/%m/%Y\"))  # 15/01/2024\n\nmañana = ahora + timedelta(days=1)\nprint(mañana)\n\nfecha_str = \"2024-12-25\"\nnavidad = datetime.strptime(fecha_str, \"%Y-%m-%d\")\nprint(navidad)",
                        "explanation": "Crear, formatear, operar y parsear fechas."
                    }
                ],
                "exercise": {
                    "prompt": "Calcula cuántos días faltan para tu próximo cumpleaños. Usa date.today() y date(año, mes, dia).",
                    "solution": "from datetime import date\n\nhoy = date.today()\n# Suponiendo cumpleaños 15 de marzo\ncumple = date(hoy.year, 3, 15)\nif cumple < hoy:\n    cumple = date(hoy.year + 1, 3, 15)\ndias = (cumple - hoy).days\nprint(f\"Faltan {dias} días\")"
                }
            },
            {
                "id": "pathlib",
                "title": "20. Rutas de archivos — pathlib",
                "theory": """
[color=#dcdcaa]from pathlib import Path[/color] — orientado a objetos, multiplataforma.

• [color=#4ec9b0]Path(\"carpeta/archivo.txt\")[/color] — crear ruta
• [color=#4ec9b0]p.exists()[/color], [color=#4ec9b0]p.is_file()[/color], [color=#4ec9b0]p.is_dir()[/color]
• [color=#4ec9b0]p.read_text()[/color], [color=#4ec9b0]p.write_text(str)[/color]
• [color=#4ec9b0]p.mkdir(parents=True, exist_ok=True)[/color]
• [color=#4ec9b0]p.iterdir()[/color] — listar directorio
• [color=#4ec9b0]p.glob(\"*.py\")[/color] — buscar patrón
• [color=#4ec9b0]p.parent / p.name / p.suffix / p.stem[/color]
                """,
                "examples": [
                    {
                        "code": "from pathlib import Path\n\np = Path(\"datos/archivo.txt\")\np.parent.mkdir(parents=True, exist_ok=True)\np.write_text(\"Hola pathlib\")\nprint(p.read_text())\nprint(p.exists(), p.suffix, p.stem)",
                        "explanation": "Crear directorios, escribir/leer, inspeccionar componentes."
                    },
                    {
                        "code": "from pathlib import Path\n\nfor archivo in Path(\".\").glob(\"*.py\"):\n    print(archivo.name, archivo.stat().st_size, \"bytes\")",
                        "explanation": "Buscar archivos .py en directorio actual."
                    }
                ],
                "exercise": {
                    "prompt": "Usa pathlib para: 1) crear carpeta 'backups', 2) escribir 'backup_1.txt' con contenido 'datos', 3) listar archivos en 'backups'.",
                    "solution": "from pathlib import Path\n\ncarpeta = Path('backups')\ncarpeta.mkdir(exist_ok=True)\narchivo = carpeta / 'backup_1.txt'\narchivo.write_text('datos')\n\nfor f in carpeta.iterdir():\n    print(f.name)"
                }
            },
            {
                "id": "collections_itertools",
                "title": "21. collections e itertools",
                "theory": """
[color=#dcdcaa]collections[/color] — contenedores especializados:
• [color=#4ec9b0]Counter[/color] — conteo de elementos
• [color=#4ec9b0]defaultdict[/color] — dict con valor por defecto
• [color=#4ec9b0]namedtuple[/color] — tupla con nombres de campos
• [color=#4ec9b0]deque[/color] — cola doble (append/pop ambos extremos O(1))

[color=#dcdcaa]itertools[/color] — iteradores eficientes:
• [color=#4ec9b0]count()[/color], [color=#4ec9b0]cycle()[/color], [color=#4ec9b0]repeat()[/color]
• [color=#4ec9b0]chain()[/color], [color=#4ec9b0]islice()[/color]
• [color=#4ec9b0]combinations()[/color], [color=#4ec9b0]permutations()[/color]
                """,
                "examples": [
                    {
                        "code": "from collections import Counter, defaultdict\n\n# Counter\ntexto = \"abracadabra\"\nprint(Counter(texto))  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})\n\n# defaultdict\nagrupado = defaultdict(list)\nfor palabra in [\"hola\", \"mundo\", \"hola\", \"python\"]:\n    agrupado[len(palabra)].append(palabra)\nprint(dict(agrupado))  # {4: ['hola', 'hola'], 5: ['mundo'], 6: ['python']}",
                        "explanation": "Counter para frecuencias, defaultdict para agrupar sin KeyError."
                    },
                    {
                        "code": "from itertools import islice, cycle\n\n# Primeros 5 de un ciclo infinito\ninf = cycle([1, 2, 3])\nprint(list(islice(inf, 5)))  # [1, 2, 3, 1, 2]",
                        "explanation": "[color=#4ec9b0]islice[/color] corta iteradores infinitos."
                    }
                ],
                "exercise": {
                    "prompt": "Dada lista = ['a', 'b', 'a', 'c', 'b', 'a', 'd']. Usa Counter para obtener las 2 más comunes. Usa defaultdict(list) para agrupar índices por letra.",
                    "solution": "from collections import Counter, defaultdict\n\nlista = ['a', 'b', 'a', 'c', 'b', 'a', 'd']\nprint(Counter(lista).most_common(2))  # [('a', 3), ('b', 2)]\n\nindices = defaultdict(list)\nfor i, letra in enumerate(lista):\n    indices[letra].append(i)\nprint(dict(indices))  # {'a': [0, 2, 5], 'b': [1, 4], 'c': [3], 'd': [6]}"
                }
            }
        ]
    }
]