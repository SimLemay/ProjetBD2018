import pymysql


def open_connection_and_cursor():
    conn = pymysql.connect(host='localhost',
                           user='projetbduser',
                           password='gUPqV1qOGG4jVcn4Ab8uuPeiCV42Pm4N4Eh1hJ7SUVctzeH7cbep1EMRUVmUGNnv',
                           db='ProjetBD')
    cursor = conn.cursor()
    return conn, cursor


def close_connection_and_cursor(connection, cursor):
    connection.close()
    cursor.close()


def execute_requete_lecture(requete, fetchall=False):
    conn, cursor = open_connection_and_cursor()
    cursor.execute(requete)
    if fetchall:
        r = cursor.fetchall()
    else:
        r = cursor.fetchone()
    close_connection_and_cursor(conn, cursor)
    return r


def execute_requete_ecriture(requete):
    conn, cursor = open_connection_and_cursor()
    try:
        cursor.execute(requete)
        conn.commit()
    except Exception as e:
        print(e)
    close_connection_and_cursor(conn, cursor)


def execute_script_creation(fichier):
    script = open(fichier, 'r')
    conn, cursor = open_connection_and_cursor()
    cmds = script.read().split(';')
    for cmd in cmds[:-1]:
        cursor.execute(cmd)
    close_connection_and_cursor(conn, cursor)


def execute_script_insertion(fichier):
    script = open(fichier, 'r')
    conn, cursor = open_connection_and_cursor()
    cmds = script.read().split(';')
    for cmd in cmds[:-1]:
        cursor.execute(cmd)
        conn.commit()
    close_connection_and_cursor(conn, cursor)
