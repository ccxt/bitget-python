# bitget-python
Python SDK (sync and async) for Bitget with Rest and WS capabilities.

You can check Bitget's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitget)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install bitget
```

## Usage

### Async

```Python
from bitget import BitgetAsync

async def main():
    instance = BitgetAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from bitget import BitgetSync

def main():
    instance = BitgetSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from bitget import BitgetWs

async def main():
    instance = BitgetWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

