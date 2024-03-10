from tvDatafeed import TvDatafeed, Interval
from __Animation__ import ProcessAnimation
from __DataBasePgrm__ import AddTableDB, InsertOrUpdateValue, FetchValues, FetchSpecificValue, DeleteLigne, FetchAllActifs, FetchAllExchange, UpdatePrice,  loggout


tv = TvDatafeed()
Fetch = None
AskCotation = None
AskExchange = None
x = None



def Beginning():
    print("------------------------------ Menu ------------------------------\nQue souhaitez vous faire ? \n 1) Get Price \n 2) Sharpe Ratio \n 3) Database \n 4) kill")
    global x
    x = input()
    while True:
        if x == None :
            Beginning()

        if x == '1' or x == 'Get Price':
            PriceAsk = input("\nDo you want a single price or several on the time scale (Single/Several) : ")
            if PriceAsk == '1' or PriceAsk == 'Single':
                PriceUniqueProcess()
            elif PriceAsk == '2' or PriceAsk == 'Several':
                PriceSeveralProcess()

        if x == '2' or x == 'Sharpe Ratio':
            SharpeProcess()

        if x == '3' or x == 'Database':
            print("------------------------------ DataBase ------------------------------\nQue souhaitez vous faire ? \n 1) Fetch \n 2) Add \n 3) Delete \n 4) Update Database \n 5) Create Database")
            DBAsk = input()
            if DBAsk == '1' or DBAsk == 'Fetch':
                print("\n1) Fetch All Values\n2) Fetch a single Value \n")
                DBAsk_Fetch = input()
                if DBAsk_Fetch == '1' or DBAsk == 'Fetch':
                    FetchValues()
                elif DBAsk_Fetch == '2' or DBAsk == 'Fetch One Specific Value':
                    FetchSpecificValue()
            elif DBAsk == '2' or DBAsk == 'Add':
                AddProcess()
                
            elif DBAsk == '3' or DBAsk == 'Delete':
                DeleteProcess()
            elif DBAsk == '4' or DBAsk == 'Update Database':
                UpdateDB()   
            elif DBAsk == '5' or DBAsk == 'Create Database':
                AddTableDB()        



        if x == '4' or x == 'kill':
            loggout()
            ProcessAnimation()
            break

        RestartProcess = input("Do you want to restart the process (Yes/No): ")
        if RestartProcess.lower() != 'yes':
            RestartPrgrm = input("Would you like to restart the program (Yes/No): ")
            if RestartPrgrm.lower() != 'yes':
                loggout()
                ProcessAnimation()
                break
            else:
                print('\n')
                Beginning()

def AskSettings():
    global AskCotation
    AskCotation = input('\n------------------------------ Assets ------------------------------\nWhich assets would you like to analyze : ')
    AskCotation = AskCotation.upper()
    global AskExchange
    AskExchange = input('On which exchange your assets are available : ')
    AskExchange = AskExchange.upper()
    global Fetch
    Fetch = tv.get_hist(symbol=AskCotation, exchange=AskExchange, interval=Interval.in_monthly, n_bars=50)
    return Fetch


def GetPrice():
    print(Fetch,'\n')

def GetUniquePrice():
    try:
        Fetch = tv.get_hist(symbol=AskCotation, exchange=AskExchange, interval=Interval.in_monthly, n_bars=1)
        if Fetch is not None:
            UniquePrice = Fetch['close'].tolist()
            if UniquePrice:
                return UniquePrice[0]
    except Exception as e:
        print()
    
    return None


def GetVol():
    try:
        Fetch = tv.get_hist(symbol=AskCotation, exchange=AskExchange, interval=Interval.in_monthly, n_bars=1)
        if Fetch is not None:
            Vol = Fetch['volume'].tolist()
            if Vol:
                return Vol[0]
    except Exception as e:
        print()
    return None



def GetSharpe():
    if Fetch is None:
        return

    list_open = Fetch['open'].tolist()
    list_open_pos = [valeur for valeur in list_open if valeur > 0]
    taux_evolutions = []

    for i in range(1, len(list_open_pos)):
        taux_evo = ((list_open_pos[i] - list_open_pos[i-1]) / list_open_pos[i-1]) * 100
        taux_evolutions.append(taux_evo)

    moyenne = sum(taux_evolutions) / len(taux_evolutions)
    variance = sum((x - moyenne) ** 2 for x in taux_evolutions) / len(taux_evolutions)
    ecart_type = variance**0.5

    CountVal = len(taux_evolutions)
    FreeRisk = 3

    FreeRiskAdjusted = (FreeRisk/12)*CountVal

    Expected_Return = moyenne*FreeRiskAdjusted
    Sharpe = Expected_Return/ecart_type
    return Sharpe

def AddProcess():
    AskSettings()
    UpdateProcess()

def DeleteProcess():
    AskSettings()
    DeleteLigne(AskCotation)

def UpdateProcess(AskCotation):
    unique_price = GetUniquePrice()
    volume = GetVol()
    sharpe = GetSharpe()
    InsertOrUpdateValue(AskCotation, AskExchange, unique_price, volume, sharpe)

def UpdateDB():
    actifs = FetchAllActifs()

    for actif in actifs:
        UpdateProcess(actif)

    # Nouvelle ligne pour mettre à jour les données du premier script avec celles de la base de données
    UpdateDataFromDB()


def UpdateDataFromDB():
    actifs = FetchAllActifs()
    exchanges = FetchAllExchange()

    for actif in actifs:
        for exchange in exchanges:
            # Suppose que la fonction FetchValues renvoie une liste de données
            data = FetchValues(actif, exchange)
            
            if data:
                new_price = data['price']  # Modifier selon la structure réelle des données
                new_vol = data['vol']  # Modifier selon la structure réelle des données
                new_sharpe = data['sharpe']  # Modifier selon la structure réelle des données

                UpdatePrice(actif, exchange, new_price, new_vol, new_sharpe)

def PriceSeveralProcess():
    AskSettings()
    GetPrice()
    Price = GetSharpe()
    print("\nThe Price of", AskCotation, "is :", Price,'\n')
    UpdateProcess()
    Price = 0

def PriceUniqueProcess():
    AskSettings()
    GetUniquePrice()
    Price = GetUniquePrice()
    print("\nThe Price of", AskCotation, "is :", Price,'\n')
    UpdateProcess()
    Price = 0


def SharpeProcess():
    AskSettings()
    GetSharpe()
    Sharpe = GetSharpe()
    print("\nThe sharpe index of", AskCotation, "is :", Sharpe,'\n')
    UpdateProcess()
