import sqlite3

# Setup DB
TA_ACTIF_DB_path = "database/common/TA_ACTIF_DB.db"

conn = sqlite3.connect(TA_ACTIF_DB_path)
c = conn.cursor()

def LoggoutActif():
    conn.close()


def AddTableDBActif():
    c.execute("""CREATE TABLE IF NOT EXISTS TA_NEWS_DB (
        Actif TEXT,
        Exchange TEXT,
        Price REAL,
        Vol REAL,
        Sharpe REAL
    )""")
    conn.commit()

def DeleteLigneActif(actif):
    rowid = FetchIdUnknowActif(actif)
    if rowid:
        c.execute("DELETE FROM TA_ACTIF_DB WHERE rowid  = ?", (rowid,))
        conn.commit()
        print(f"L'actif {actif} supprimée avec succès.")
    else:
        print(f"Aucun enregistrement trouvé pour l'actif {actif}.")

def FetchValuesActif():
    c.execute("SELECT * FROM TA_ACTIF_DB")
    data = c.fetchall()
    for row in data:
        print(row)


def FetchSpecificValueActif(actif):
    c.execute("SELECT Actif, Exchange, Price, Vol, Sharpe FROM TA_ACTIF_DB WHERE Actif = ?", (actif,))
    specific_value = c.fetchone()

    if specific_value:
        ActifFetched, ExchangeFetched, PriceFetched, VolFetched, SharpeFetched = specific_value

        print(f"\n {ActifFetched} has been found in the DB, here is the result : \n")
        print(f" -->  Price is {PriceFetched}")
        print(f" -->  Vol is {VolFetched}")
        print(f" -->  Sharpe is {SharpeFetched}\n")
    else:
        raise ValueError(f"No data found for Actif: {actif}")

def FetchIdUnknowActif(actif):
    c.execute("SELECT rowid FROM TA_ACTIF_DB WHERE Actif = ?", (actif,))
    result = c.fetchone()

    if result:
        id = result[0]
        #debug print(f"L'ID de la ligne avec {ValLookingFor} est : {id}")
        return id
    else:
        #debug print(f"Aucune ligne trouvée avec {ValLookingFor}")
        return None
    


def FetchSettingsActif():
    c.execute(f"SELECT actif, exchange FROM TA_ACTIF_DB")

    result = c.fetchall()

    ActifList = []
    ExchangeList = []
    for row in result:
        ActifList.append(row[0])
        ExchangeList.append(row[1])
    return ActifList, ExchangeList



def InsertOrUpdateValueActif( Actif, Exchange, Price, Vol, Sharpe):
    existing_id = FetchIdUnknowActif(Actif)

    if existing_id is not None:
        c.execute("UPDATE TA_ACTIF_DB SET Exchange = ?, Price = ?, Vol = ?, Sharpe = ? WHERE rowid = ?",
                  (Exchange, Price, Vol, Sharpe, existing_id))
        print(f"La valeur pour {Actif} existe déjà. Mise à jour effectuée.")
    else:
        c.execute("INSERT INTO TA_ACTIF_DB VALUES (?, ?, ?, ?, ?)", (Actif, Exchange, Price, Vol, Sharpe))
        print(f"La valeur pour {Actif} n'existe pas. Insertion effectuée.")

    conn.commit()






