from tradeiros.okx.okx import Okx
from tradeiros.bybit.bybit import Bybit
from tradeiros.bitget.bitget import Bitget
import os
from dotenv import load_dotenv, find_dotenv

class Tradeiros:
    def __init__(self, exchange, **kwargs):
        load_dotenv(find_dotenv()) 
        
        self.exchange_name = exchange
        
        if exchange == "okx":
            self.exchange = Okx(**kwargs)
        elif exchange == "bybit":
            self.exchange = Bybit(**kwargs)
        elif exchange == "bitget":
            self.exchange = Bitget(**kwargs)
        else:
            raise ValueError("Exchange não suportada")

    def atualizar(self):
        df, patrimonio = self.exchange.atualizar()
        self._df = df
        self._patrimonio = patrimonio
        return self._df

    def patrimonio(self):
        return self._patrimonio
        
if __name__ == "__main__":
    tradeiros = Tradeiros("okx")
    df = tradeiros.atualizar()
    print(df)
    print("Patrimônio: ", tradeiros.patrimonio())
    print("1% do patrimônio: ", tradeiros.patrimonio()*0.01)

    print("\n")
    
    #tradeiros = Tradeiros("bitget")
    #df, patrimonio = tradeiros.atualizar()
    #print(df)
    #print("Patrimônio: ", patrimonio)
    #print("1% do patrimônio: ", patrimonio*0.01)

        