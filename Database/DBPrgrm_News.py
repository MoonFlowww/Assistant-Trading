import sqlite3

# Setup DB

TA_NEWS_DB_path = "database/common/TA_NEWS_DB.db"

conn = sqlite3.connect(TA_NEWS_DB_path)
c = conn.cursor()



def LoggoutNews(conn):
    conn.close()


def AddTableDBNews():
    c.execute("""CREATE TABLE IF NOT EXISTS TA_NEWS_DB (
        News TEXT,
        Exchange TEXT,
        Taux REAL
    )""")
    conn.commit()

def DeleteLigneNews(News):
    rowid = FetchIdUnknowNews(News)
    if rowid:
        c.execute("DELETE FROM TA_NEWS_DB WHERE rowid  = ?", (rowid,))
        conn.commit()
        print(f"La News {News} supprimée avec succès.")
    else:
        print(f"Aucun enregistrement trouvé pour l'actif {News}.")

def FetchValuesNews():
    c.execute("SELECT * FROM TA_NEWS_DB")
    data = c.fetchall()
    for row in data:
        print(row)



def FetchSpecificValueNews(News):
    c.execute("SELECT News, Exchange, Taux FROM TA_NEWS_DB WHERE News = ?", (News,))
    specific_value = c.fetchone()

    if specific_value:
        NewsFetched, ExchangeFetched, TauxFetched = specific_value

        print(f"\n {NewsFetched} has been found in the DB, here is the result : \n")
        print(f" -->  Taux is {TauxFetched}")
    else:
        raise ValueError(f"No data found for News: {News}")

def FetchIdUnknowNews(News):
    c.execute("SELECT rowid FROM TA_NEWS_DB WHERE News = ?", (News,))
    result = c.fetchone()

    if result:
        id = result[0]
        #debug print(f"L'ID de la ligne avec {ValLookingFor} est : {id}")
        return id
    else:
        #debug print(f"Aucune ligne trouvée avec {ValLookingFor}")
        return None
    


def FetchSettingsNews():
    c.execute(f"SELECT News, exchange FROM TA_NEWS_DB")

    result = c.fetchall()

    NewsList = []
    ExchangeList = []
    for row in result:
        NewsList.append(row[0])
        ExchangeList.append(row[1])
    return NewsList, ExchangeList



def InsertOrUpdateValueNews(News, Exchange, Taux,):
    existing_id = FetchIdUnknowNews(News)

    if existing_id is not None:
        c.execute("UPDATE TA_NEWS_DB SET Exchange = ?, Taux = ? WHERE rowid = ?",
                  (Exchange, Taux, existing_id))
        print(f"La valeur pour {News} existe déjà. Mise à jour effectuée.")
    else:
        c.execute("INSERT INTO TA_NEWS_DB VALUES (?, ?, ?)", (News, Exchange, Taux))
        print(f"La valeur pour {News} n'existe pas. Insertion effectuée.")

    conn.commit()






