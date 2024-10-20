from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup, aula.DescAula FROM alumne JOIN aula ON alumne.idAula = aula.idAula"
        cur.execute(query)
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"{e}"}
    
    finally:
        if cur: cur.close()
        if conn: conn.close()
    
    return alumnes