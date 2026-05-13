from typing import ClassVar
from dataclasses import dataclass

@dataclass
class SharedSymbol:
    name : str
    nobitex_name : str
    bitpin_name : str

class SharedSymbols:
    BTCUSDT : ClassVar[SharedSymbol] = SharedSymbol('BTCUSDT', nobitex_name='BTCUSDT', bitpin_name='BTC_USDT')
    ETHUSDT : ClassVar[SharedSymbol] = SharedSymbol('ETHUSDT', nobitex_name='ETHUSDT', bitpin_name='ETH_USDT')
    TONUSDT : ClassVar[SharedSymbol] = SharedSymbol('TONUSDT', nobitex_name='TONUSDT', bitpin_name='TON_USDT')
    DAIUSDT : ClassVar[SharedSymbol] = SharedSymbol('DAIUSDT', nobitex_name='DAIUSDT', bitpin_name='DAI_USDT')
    XMRUSDT : ClassVar[SharedSymbol] = SharedSymbol('XMRUSDT', nobitex_name='XMRUSDT', bitpin_name='XMR_USDT')
    XRPUSDT : ClassVar[SharedSymbol] = SharedSymbol('XRPUSDT', nobitex_name='XRPUSDT', bitpin_name='XRP_USDT')
    SOLUSDT : ClassVar[SharedSymbol] = SharedSymbol('SOLUSDT', nobitex_name='SOLUSDT', bitpin_name='SOL_USDT')
    TRXUSDT : ClassVar[SharedSymbol] = SharedSymbol('TRXUSDT', nobitex_name='TRXUSDT', bitpin_name='TRX_USDT')
    USDCUSDT : ClassVar[SharedSymbol] = SharedSymbol('USDCUSDT', nobitex_name='USDCUSDT', bitpin_name='USDC_USDT')
    BNBUSDT : ClassVar[SharedSymbol] = SharedSymbol('BNBUSDT', nobitex_name='BNBUSDT', bitpin_name='BNB_USDT')