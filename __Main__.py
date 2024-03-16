from tvDatafeed import TvDatafeed, Interval
from __Animation__ import ProcessAnimation, RunWithAnimation
import threading
import sys


sys.path.append("database")
from DBPrgrm_Actif import AddTableDBActif, InsertOrUpdateValueActif, FetchValuesActif, FetchSpecificValueActif, DeleteLigneActif, FetchSettingsActif, LoggoutActif
from DBPrgrm_News import AddTableDBNews, InsertOrUpdateValueNews, FetchValuesNews, FetchSpecificValueNews, DeleteLigneNews, FetchSettingsNews, LoggoutNews

sys.path.append("technical_suite")
from LucasPrgrm import Lucas
from PadovanPrgrm import Padovan
from PellPrgrm import Pell
from PerrinPrgrm import Perrin  
from SyracusePrgrm import Syracuse
from FibonacciPrgrm import Fibonacci
from TribonacciPrgrm import Tribonacci

sys.path.append("Analyse Math/Probability")
from KhyDeuxPrgrm import Chi2

tv = TvDatafeed()
Fetch = None
Actif = None
Exchange = None
x = None







def Beginning():
    while True:
        print("------------------------------ Menu ------------------------------\nQue souhaitez vous faire ? \n 1) Get Price \n 2) Sharpe Ratio \n 3) Probability \n 4) Database \n 5) Math Fonc \n 6) kill")
        global x
        x = input()
        if x == '1' or x == 'Get Price':
            PriceAsk = input("\nDo you want a single price or several on the time scale (Single/Several) : ")
            if PriceAsk == '1' or PriceAsk == 'Single':
                PriceUniqueProcess()
            elif PriceAsk == '2' or PriceAsk == 'Several':
                PriceSeveralProcess()

        elif x == '2' or x == 'Sharpe Ratio': #faire rebrique analyse avec Delta Velta et Gamma
            SharpeProcess()
        elif x =='3' or x == 'Probability':
            AskSettings()
            Fetch = GetSeveralPrice(Actif, Exchange)
            Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=50)

            if Fetch is None:
                return None

            list_open = Fetch['open'].tolist()
            Forecast = input("What is the actual Forecast : ")
            Chi2(Forecast)
        elif x == '4' or x == 'Database':
            print("------------------------------ DataBase ------------------------------\nQue souhaitez vous faire ? \n 1) Fetch \n 2) Add \n 3) Delete \n 4) Update Database \n 5) Create Database")
            DBAsk = input()
            if DBAsk == '1' or DBAsk == 'Fetch':
                print("\n1) Fetch All Values\n2) Fetch a single Value")
                DBAsk_Fetch = input()
                if DBAsk_Fetch == '1' or DBAsk == 'Fetch All Values':
                        print(" -> Here is the list of registered News : ")
                        FetchValuesNews()
                        print("\n -> And here is the list of tracked Assets")
                        FetchValuesActif()
                elif DBAsk_Fetch == '2' or DBAsk == 'fetch one specific value':
                    actif = input("Which assets would you like to research in the DB : ").upper()
                    if Exchange == "ECONOMICS":
                        FetchSpecificValueNews(Exchange, actif)
                    else:
                        FetchSpecificValueActif(Exchange, actif)

            elif DBAsk == '2' or DBAsk == 'Add':
                AddProcess()
                
            elif DBAsk == '3' or DBAsk == 'Delete':
                actif = input("Which assets would you like to delete in the DB : ").upper()
                
                if Exchange == "ECONOMICS":
                    DeleteLigneNews(actif)
                else:
                    DeleteLigneActif(actif)
            elif DBAsk == '4' or DBAsk == 'Update Database':
                UpdateDB()   
            elif DBAsk == '5' or DBAsk == 'Create Database':
                AddTableDBNews()
                AddTableDBActif()
                
        elif x == '5' or x == 'Math Fonc':
            print("------------------------------ Math Fonction ------------------------------\nQue souhaitez vous faire ? \n 1) Lucas \n 2) Padovan \n 3) Pell \n 4) Perrin \n 5) Sycaruse \n 6) Fibonacci \n 7) Tribonacci")
            MathAsk = input()


            if MathAsk == '1' or MathAsk == 'Lucas':
                suite = Lucas()
                print(f"Les termes de la suite de Lucas sont : {suite}")

            elif MathAsk == '2' or MathAsk == 'Padovan':
                suite = Padovan()
                print(f"Les termes de la suite de Padovan sont : {suite}")
                    
            elif MathAsk == '3' or MathAsk == 'Pell':
                suite = Pell()
                print(f"Les termes de la suite de Pell sont : {suite}")

            elif MathAsk == '4' or MathAsk == 'Perrin':
                suite = Perrin()
                print(f"Les termes de la suite de Perrin sont : {suite}")

            elif MathAsk == '5' or MathAsk == 'Syracuse':
                n = int(input("What's your initial value : "))
                suite = Syracuse(n)
                print(f"Les termes du cycle de Sycaruse suivant la valeur initial {n} sont : {suite}")
            
            elif MathAsk == '6' or MathAsk == 'Fibonacci':
                suite = Fibonacci()
                print(f"Les termes de la suite de Fibonacci sont : {suite}")


            elif MathAsk == '7' or MathAsk == 'Tribonacci':
                suite = Tribonacci()
                print(f"Les termes de la suite de Tribonacci sont : {suite}")


        elif x == '6' or x == 'Kill':
            LoggoutActif()
            LoggoutNews()
            ProcessAnimation(3)
            break

        restart_process = input("Do you want to restart the process (Yes/No): ").lower()
        if restart_process != 'yes':
            restart_program = input("Would you like to restart the program (Yes/No): ").lower()
            if restart_program != 'yes':
                LoggoutActif()
                LoggoutNews()
                ProcessAnimation(3)
                break
            else:
                print('\n')
                Beginning()
                

        




def AskSettings():
    global Actif
    Actif = input('\n------------------------------ Assets ------------------------------\nWhich assets would you like to analyze : ')
    Actif = Actif.upper()
    global Exchange
    Exchange = input('On which exchange your assets are available : ')
    Exchange = Exchange.upper()
    global Fetch


def GetSeveralPrice(Actif, Exchange):
    Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=50)
    if Fetch is not None:
        print(Fetch,'\n')


def GetUniquePrice(Actif, Exchange):
    try:
        Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=1)
        if Fetch is not None:
            UniquePrice = Fetch['close'].tolist()
            if UniquePrice:
                return UniquePrice[0]
    except Exception as e:
        print("Erreur dans GetUniquePrice:", e)
    
    return None


def GetVol(Actif, Exchange):
    try:
        Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=1)
        if Fetch is not None:
            Vol = Fetch['volume'].tolist()
            if Vol:
                return Vol[0]
    except Exception as e:
        print("Erreur dans GetVol:", e)
    
    return None




def GetSharpe(Actif, Exchange):
    Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=50)

    if Fetch is None:
        return None

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
    UpdateProcess(Actif, Exchange)


def UpdateProcess(Actif, Exchange):
    unique_price = GetUniquePrice(Actif, Exchange)
    volume = GetVol(Actif, Exchange)
    sharpe = GetSharpe(Actif, Exchange)
    if Exchange == "ECONOMICS":
        InsertOrUpdateValueNews(Actif, Exchange, unique_price)
    else:
        InsertOrUpdateValueActif(Actif, Exchange, unique_price, volume, sharpe)


def UpdateDB():
    #DB Update for News
    ActifList, ExchangeList = FetchSettingsNews()
    LenList = len(ActifList)

    for i in range(LenList):
        actif = ActifList[i]
        Exchange = ExchangeList[i]
        FetchPriceDebug(actif, Exchange)

        animation_thread = threading.Thread(target=RunWithAnimation, args=(ProcessAnimation, 1))
        animation_thread.start()
        sys.stdout.write('\b \b')
        UpdateProcess(actif, Exchange)
        animation_thread.join()


    #DB Update for Actifs
    ActifList, ExchangeList = FetchSettingsActif()
    LenList = len(ActifList)

    for i in range(LenList):
        actif = ActifList[i]
        Exchange = ExchangeList[i]
        FetchPriceDebug(actif, Exchange)

        animation_thread = threading.Thread(target=RunWithAnimation, args=(ProcessAnimation, 1))
        animation_thread.start()
        sys.stdout.write('\b \b')
        UpdateProcess(actif, Exchange)
        animation_thread.join()


def PriceSeveralProcess():
    AskSettings()
    GetSeveralPrice(Actif, Exchange)
    UpdateProcess(Actif, Exchange)


def PriceUniqueProcess():
    AskSettings()
    Price = GetUniquePrice(Actif, Exchange)
    print("\nThe Price of", Actif, "is :", Price, '\n')
    UpdateProcess(Actif, Exchange)
    Price = 0


def SharpeProcess():
    AskSettings()
    Sharpe = GetSharpe(Actif, Exchange)
    print("\nThe sharpe index of", Actif, "is :", Sharpe,'\n')
    UpdateProcess(Actif, Exchange)




def FetchPriceDebug(Actif, Exchange):
    if Actif is None or Exchange is None:
        return None

    try:
        Fetch = tv.get_hist(symbol=Actif, exchange=Exchange, interval=Interval.in_monthly, n_bars=1)
        if Fetch is not None:
            UniquePrice = Fetch['close'].tolist()
            if UniquePrice:
                return UniquePrice[0]
    except Exception as e:
        print("Erreur dans FetchPriceDebug:", e)

    return None


