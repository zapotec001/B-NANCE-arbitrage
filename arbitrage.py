import time
from binance.client import Client
from binance.enums import *

"""----BİNANCE ARBİTRAJ HESAPLAYICI """

api_key = 'YOUR APİ'
api_secret = 'APİ SECRET'
##################################################
trdPair1 = 'BTC'                                    #EDİT AND TRY OTHER PAİRS
trdPair2 = 'USDT'
trdPair3 = 'TRY'
##################################################
client = Client(api_key, api_secret)
while True:
    #         USDT-TRY
    islemcifti1 = trdPair2 + trdPair3
    price = client.get_ticker(symbol=islemcifti1)
    coiprice1 = format(float(price['askPrice']), '.3f')
    print("USDT-TRY:            ",coiprice1)
    birdolar = coiprice1

    #          BTC-USDT
    islemcifti2 = trdPair1 + trdPair2
    price = client.get_ticker(symbol=islemcifti2)
    coiprice2 = format(float(price['askPrice']), '.3f')
    print("BTC-USDT:            ",coiprice2)
    usdtl = float(coiprice2) * float(birdolar)
    print("BTC-USDT to Tl:      ",usdtl)

    #           BTC-TRY
    islemcifti3 = trdPair1 + trdPair3
    price = client.get_ticker(symbol=islemcifti3)
    coiprice3 = format(float(price['askPrice']), '.3f')
    print("BTC-TRY:             ",coiprice3)
    coiprice3 = float(coiprice3)
    fark = (coiprice3-usdtl)
    yuzde = (fark/coiprice3)*100
    print("yuzde: ",str(yuzde)[:6])
    print("BTC-USDT ile BTC-TRY farkı:              ",str(fark)[:6], "Tl")

    #balance
    balance1 = client.get_asset_balance(asset = trdPair1)
    balance2 = client.get_asset_balance(asset = trdPair2)
    balance3 = client.get_asset_balance(asset = trdPair3)

    coiNumber1 = format(float(balance1['free'])- 0.0005,'.4f') #BTC
    coiNumber2 = format(float(balance2['free'])- 0.0005,'.4f') #USDT
    coiNumber3 = format(float(balance3['free'])- 0.0005,'.4f') #TRY
    print("----------------")
    """
    print("bnb balance: ",coiNumber1)
    print("usdt balance: ",coiNumber2)
    print("try balance: ",coiNumber3)
    """
    time.sleep(3)