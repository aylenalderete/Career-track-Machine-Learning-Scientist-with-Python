class Sujeto():
    '''Clase para un Sujeto experimental.
    info contiene datos por ejemplo sociodemográficos previos
    en resultados guardaremos los resultados de las pruebas'''
    def __init__(self, sujeto_id, info: dict):
        self.id = sujeto_id
        self.info = info
        self.resultados = dict()
        
    def __repr__(self):
        # Funcion mágica para mostrar los datos del sujeto
        # el :<20 hace un relleno de máximo 20 espacios
        s = f'Datos de ID {self.id:<20}\n\n'
        for k, v in self.info.items():
            s += f"{k:<20} {v:<20}\n"
        for k, v in self.resultados.items():
            s += f"{k:<20} {v:<20}\n"
        return s

info = {'edad':22, 'fecha_nacimiento':'01-01-1998', 'años_educacion':6}
sujeto = Sujeto('123456789', info)

print(sujeto)