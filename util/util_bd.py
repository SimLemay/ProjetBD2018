import pymysql


def open_connection_and_cursor(obtenir_dict=False):
    arg_cursorclass = {'cursorclass': pymysql.cursors.DictCursor} if obtenir_dict else {}
    conn = pymysql.connect(host='localhost',
                           user='projetbduser',
                           password='gUPqV1qOGG4jVcn4Ab8uuPeiCV42Pm4N4Eh1hJ7SUVctzeH7cbep1EMRUVmUGNnv',
                           db='ProjetBD',
                           **arg_cursorclass)
    cursor = conn.cursor()
    return conn, cursor


def close_connection_and_cursor(connection, cursor):
    connection.close()
    cursor.close()


def execute_requete_lecture(requete, *args, fetchall=False, obtenir_dict=False):
    conn, cursor = open_connection_and_cursor(obtenir_dict)
    cursor.execute(requete, *args)
    if fetchall:
        r = cursor.fetchall()
    else:
        r = cursor.fetchone()
    close_connection_and_cursor(conn, cursor)
    return r


def execute_requete_ecriture(requete, *args):
    conn, cursor = open_connection_and_cursor()
    try:
        cursor.execute(requete, *args)
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
