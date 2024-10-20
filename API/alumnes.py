def alumne_schema(Alumnes) -> dict:
    return {
        "NomAlumne": Alumnes[0],
        "Cicle": Alumnes[1],
        "Curs": Alumnes[2],
        "Grup": Alumnes[3],
        "DescAula": Alumnes[4]
    }
def alumnes_schema(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]