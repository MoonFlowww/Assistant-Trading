from tvDatafeed import TvDatafeedLive, Interval, TvDatafeed


tvl = TvDatafeedLive()
symbol = 'BTCUSDT'
exchange = 'BINANCE'

seis=tvl.new_seis(symbol, exchange, Interval.in_1_hour, timeout=10)

data=seis.get_hist(n_bars=10, timeout=-1)

def consumer_func1(seis, data):
	print("Open price for "+seis.symbol+" on "+seis.exchange+" exchange with "+seis.interval.name+" interval was "+str(data.open[0]))

def consumer_func2(seis, data):
	print("Volume of "+seis.symbol+" on "+seis.exchange+" exchange with "+seis.interval.name+" interval was "+str(data.volume[0]))

def consumer_func3(seis, data):
	print("Close price for "+seis.symbol+" on "+seis.exchange+" exchange with "+seis.interval.name+" interval was "+str(data.close[0]))

consumer1=tvl.new_consumer(seis, consumer_func1)
consumer2=seis.new_consumer(consumer_func2)
consumer3=seis.new_consumer(consumer_func3)

consumer_func1()
consumer_func2()
consumer_func3()