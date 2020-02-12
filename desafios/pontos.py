def adiciona_pontos(texto):
    if isinstance(texto, str):
        return ".".join(list(texto))
    return None


def remove_pontos(texto):
    return "".join(texto.split("."))
