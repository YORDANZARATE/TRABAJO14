#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo.
# La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semana



temperaturas =[
    [  # ciudad_1
        [  # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 41},
            {"day": "Domingo", "temp": 47}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],

    ],
    [  # ciudad_2
        [  # Semana 1
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 57},
            {"day": "Jueves", "temp": 47},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 40}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 47},
            {"day": "Miércoles", "temp": 41},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 40}
        ],

    ]
]


def promedio_temp_ciudad(arreglo_temperaturas,ciudad, semana):
    acumulador=0
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador = acumulador + arreglo_temperaturas[ciudad][semana][i]
        promedio=acumulador /len(arreglo_temperaturas[ciudad][semana])
        return promedio
    resultado_prom= promedio_temp_ciudad(temperaturas,ciudad,semana)

    print(resultado_prom)
