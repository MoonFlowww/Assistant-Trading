import sqlite3


# Setup DB
conn = sqlite3.connect('TA_DB.db')
c = conn.cursor()


def loggout():
    conn.close()



def AddTableDB():
    c.execute("""CREATE TABLE IF NOT EXISTS TA_DB (
            Actif TEXT,
            Exchange TEXT,
            Price REAL,
            Vol REAL,
            Sharpe REAL
    )""")
    conn.commit()

def InsertValuesDB(actif, exchange, price, vol, sharpe):
    c.execute(f"INSERT INTO TA_DB VALUES ({actif}, {exchange}, {price}, {vol}, {sharpe})")
    conn.commit()

def DeleteLigne(actif):
    c.execute("DELETE FROM TA_DB WHERE rowid = ?", (actif,))
    conn.commit()
    print(f"L'actif {actif} supprimée avec succès.")

def FetchValues():
    c.execute("SELECT * FROM TA_DB")
    data = c.fetchall()
    for row in data:
        print(row)

def FetchSpecificValue():
    c.execute("SELECT Actif, Price FROM TA_DB") #possibilité de modifier la colone de recherche
    specific_value = c.fetchone()
    print(specific_value)

def FetchIdUnknow(ValLookingFor):
    c.execute("SELECT rowid FROM TA_DB WHERE Actif = ?", (ValLookingFor,))
    result = c.fetchone()

    if result:
        id = result[0]
        #debug print(f"L'ID de la ligne avec {ValLookingFor} est : {id}")
        return id
    else:
        #debug print(f"Aucune ligne trouvée avec {ValLookingFor}")
        return None
    

def FetchAllActifs():
    # Exécute la requête SQL pour récupérer toutes les valeurs de la colonne 'Actif'
    c.execute("SELECT Actif FROM TA_DB")
    
    # Récupère tous les résultats de la requête
    resultats = c.fetchall()

    # Retourne une liste des valeurs de la colonne 'Actif'
    return [resultat[0] for resultat in resultats]

def FetchAllExchange():
    # Exécute la requête SQL pour récupérer toutes les valeurs de la colonne 'Actif'
    c.execute("SELECT Exchange FROM TA_DB")
    
    # Récupère tous les résultats de la requête
    result = c.fetchall()

    # Retourne une liste des valeurs de la colonne 'Actif'
    return [result[0] for result in result]





def InsertOrUpdateValue(Actif, Exchange, Price, Vol, Sharpe):
    existing_id = FetchIdUnknow(Actif)

    if existing_id is not None:
        c.execute("UPDATE TA_DB SET Exchange = ?, Price = ?, Vol = ?, Sharpe = ? WHERE rowid = ?",
                  (Exchange, Price, Vol, Sharpe, existing_id))
        print(f"La valeur pour {Actif} existe déjà. Mise à jour effectuée.")
    else:
        c.execute("INSERT INTO TA_DB VALUES (?, ?, ?, ?, ?)", (Actif, Exchange, Price, Vol, Sharpe))
        print(f"La valeur pour {Actif} n'existe pas. Insertion effectuée.")

    conn.commit()




def UpdatePrice(actif, exchange, new_price, new_vol, new_sharpe):
    existing_id = FetchIdUnknow(actif)

    if existing_id is not None:
        c.execute("UPDATE TA_DB SET Price = ? WHERE rowid = ?", (new_price, existing_id))
        print(f"Prix pour {actif} mis à jour avec succès.")
        conn.commit()
    else:
        print(f"Aucune ligne trouvée avec {actif}.")
        InsertValuesDB(actif, exchange, new_price, new_vol, new_sharpe)
        print(f"Updated Successfully for {actif} ! ")

def UpdateVol(actif, new_vol):
    existing_id = FetchIdUnknow(actif)

    if existing_id is not None:
        c.execute("UPDATE TA_DB SET Price = ? WHERE rowid = ?", (new_vol, existing_id))
        print(f"Volume pour {actif} mis à jour avec succès.")
        conn.commit()

def UpdateSharpe(actif, new_Sharpe):
    existing_id = FetchIdUnknow(actif)

    if existing_id is not None:
        c.execute("UPDATE TA_DB SET Price = ? WHERE rowid = ?", (new_Sharpe, existing_id))
        print(f"Sharpe pour {actif} mis à jour avec succès.")
        conn.commit()


conn.commit()

# -------------Debug----------------
#AddTableDB()
#InsertValuesDB()
#FetchValues()
#FetchSpecificValue()
#ModValue()
#UpdatePrice() Besoin d'un actif et new_price
#UpdateVol() Besoin d'un actif et new_vol
#UpdateSharpe() Besoin d'un actif et new_sharpe




