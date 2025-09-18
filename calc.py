# calc.py
def suma(a, b):
    try:
        # Convertir a float para validar que son números
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "error"
