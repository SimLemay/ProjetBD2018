import pymysql


def _open_connection_and_cursor():
    conn = pymysql.connect(host='localhost',
                           user='projetbduser',
                           password='gUPqV1qOGG4jVcn4Ab8uuPeiCV42Pm4N4Eh1hJ7SUVctzeH7cbep1EMRUVmUGNnv',
                           db='ProjetBD')
    cursor = conn.cursor()
    return conn, cursor


def _close_connection_and_cursor(connection, cursor):
    connection.close()
    cursor.close()


def execute_requete_lecture(requete, fetchall=False):
    conn, cursor = _open_connection_and_cursor()
    cursor.execute(requete)
    if fetchall:
        r = cursor.fetchall()
    else:
        r = cursor.fetchone()
    _close_connection_and_cursor(conn, cursor)
    return r


def execute_requete_ecriture(requete):
    conn, cursor = _open_connection_and_cursor()
    try:
        cursor.execute(requete)
        conn.commit()
    except Exception as e:
        print(e)
    _close_connection_and_cursor(conn, cursor)


def execute_script(fichier):
    script = open(fichier, 'r')
    conn, cursor = _open_connection_and_cursor()
    cmds = script.read().split(';')
    for cmd in cmds[:-1]:
        cursor.execute(cmd)
    _close_connection_and_cursor(conn, cursor)
