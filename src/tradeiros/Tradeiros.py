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
        return df, patrimonio
        

if __name__ == "__main__":
    tradeiros = Tradeiros("okx")
    df, patrimonio = tradeiros.atualizar()
    print(df)
    print("Patrimônio: ", patrimonio)
    print("1% do patrimônio: ", patrimonio*0.01)

    print("\n")
    
    #tradeiros = Tradeiros("bitget")
    #df, patrimonio = tradeiros.atualizar()
    #print(df)
    #print("Patrimônio: ", patrimonio)
    #print("1% do patrimônio: ", patrimonio*0.01)

        