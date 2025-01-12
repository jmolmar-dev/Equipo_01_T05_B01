def suma(a, b):
    """Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b


def resta(a, b):
    """Resta dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la resta.
    """
    return a - b


def multiplicacion(a, b):
    """Multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b


def division(a, b):
    """Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor. No puede ser cero.

    Returns:
        float: Resultado de la división.

    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b


def operaciones_basicas(a, b):
    """Realiza todas las operaciones básicas entre dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        dict: Diccionario con los resultados de suma, resta, multiplicación y división.

    Raises:
        ValueError: Si el divisor es cero al intentar dividir.
    """
    try:
        return {
            "suma": suma(a, b),
            "resta": resta(a, b),
            "multiplicacion": multiplicacion(a, b),
            "division": division(a, b),
        }
    except ValueError as e:
        return {"error": str(e)}
