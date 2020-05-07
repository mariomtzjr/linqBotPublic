import connector
import psycopg2


def queryExecute(query):

    db = connector.Connect().db
    cursor = db.cursor()

    try:
        cursor.execute(query)

        result = cursor.fetchall()
    except (Exception, psycopg2.Error) as e:
            print("Error while connecting to PostgreSQL ", e)
    # finally:
    #     if(db):
    #         cursor.close()
    #         db.close()

    return result
