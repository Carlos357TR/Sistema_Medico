def crear_atencion(codigo, cita):
    return {
        "codigo": codigo,
        "cita": cita
    }

def resumen_atencion(atencion):
    codigo_cita = atencion["cita"].codigo
    return f"Atención {atencion['codigo']} - Cita Asociada: {codigo_cita}"