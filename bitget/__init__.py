import sys
import bitget.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from bitget.ccxt import bitget as BitgetSync
from bitget.ccxt.async_support.bitget import bitget as BitgetAsync
from bitget.ccxt.pro.bitget import bitget as BitgetWs
