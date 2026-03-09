# core/gamma_transform.py

def natural_log(x, iterations=50):
    """
    Aproximación de ln(x) usando expansión de serie:
    ln(x) = 2 * sum( ((x-1)/(x+1))^(2k+1) / (2k+1) )

    Convergencia buena para x > 0
    """

    if x <= 0:
        raise ValueError("Log undefined for x <= 0")

    y = (x - 1) / (x + 1)
    y_power = y
    result = 0.0

    for k in range(iterations):
        result += y_power / (2 * k + 1)
        y_power *= y * y

    return 2 * result


def gamma_from_uniforms(uniforms, beta):
    """
    Gamma(α, β) cuando α entero:
    Gamma = -β * sum(ln(U_i))
    """

    summation = 0.0

    for u in uniforms:
        if u <= 0:
            raise ValueError("Uniform values must be > 0")

        summation += natural_log(u)

    return -beta * summation