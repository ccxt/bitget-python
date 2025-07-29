# bitget-python
Python SDK (sync and async) for Bitget cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitget)
- You can check Bitget's docs here: [Docs](https://www.google.com/search?q=google+bitget+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/bitget-python
- Pypi package: https://pypi.org/project/bitget


## Installation

```
pip install bitget
```

## Usage

### Sync

```Python
from bitget import BitgetSync

def main():
    instance = BitgetSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from bitget import BitgetAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitgetAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from bitget import BitgetWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitgetWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_convert_trade(self, id: str, fromCode: str, toCode: str, amount: Num = None, params={})`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_canceled_and_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_canceled_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_convert_currencies(self, params={})`
- `fetch_convert_quote(self, fromCode: str, toCode: str, amount: Num = None, params={})`
- `fetch_convert_trade_history(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_cross_borrow_rate(self, code: str, params={})`
- `fetch_currencies(self, params={})`
- `fetch_default_markets(self, params)`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_isolated_borrow_rate(self, symbol: str, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_long_short_ratio_history(self, symbol: Str = None, timeframe: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_margin_mode(self, symbol: str, params={})`
- `fetch_mark_price(self, symbol: str, params={})`
- `fetch_market_leverage_tiers(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_liquidations(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest(self, symbol: str, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions_history(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_uta_markets(self, params)`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `borrow_cross_margin(self, code: str, amount: float, params={})`
- `borrow_isolated_margin(self, symbol: str, code: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `close_all_positions(self, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `modify_margin_helper(self, symbol: str, amount, type, params={})`
- `nonce(self)`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `repay_cross_margin(self, code: str, amount, params={})`
- `repay_isolated_margin(self, symbol: str, code: str, amount, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `set_sandbox_mode(self, enabled)`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `public_common_get_v2_public_annoucements(request)`
- `public_common_get_v2_public_time(request)`
- `public_spot_get_spot_v1_notice_queryallnotices(request)`
- `public_spot_get_spot_v1_public_time(request)`
- `public_spot_get_spot_v1_public_currencies(request)`
- `public_spot_get_spot_v1_public_products(request)`
- `public_spot_get_spot_v1_public_product(request)`
- `public_spot_get_spot_v1_market_ticker(request)`
- `public_spot_get_spot_v1_market_tickers(request)`
- `public_spot_get_spot_v1_market_fills(request)`
- `public_spot_get_spot_v1_market_fills_history(request)`
- `public_spot_get_spot_v1_market_candles(request)`
- `public_spot_get_spot_v1_market_depth(request)`
- `public_spot_get_spot_v1_market_spot_vip_level(request)`
- `public_spot_get_spot_v1_market_merge_depth(request)`
- `public_spot_get_spot_v1_market_history_candles(request)`
- `public_spot_get_spot_v1_public_loan_coininfos(request)`
- `public_spot_get_spot_v1_public_loan_hour_interest(request)`
- `public_spot_get_v2_spot_public_coins(request)`
- `public_spot_get_v2_spot_public_symbols(request)`
- `public_spot_get_v2_spot_market_vip_fee_rate(request)`
- `public_spot_get_v2_spot_market_tickers(request)`
- `public_spot_get_v2_spot_market_merge_depth(request)`
- `public_spot_get_v2_spot_market_orderbook(request)`
- `public_spot_get_v2_spot_market_candles(request)`
- `public_spot_get_v2_spot_market_history_candles(request)`
- `public_spot_get_v2_spot_market_fills(request)`
- `public_spot_get_v2_spot_market_fills_history(request)`
- `public_mix_get_mix_v1_market_contracts(request)`
- `public_mix_get_mix_v1_market_depth(request)`
- `public_mix_get_mix_v1_market_ticker(request)`
- `public_mix_get_mix_v1_market_tickers(request)`
- `public_mix_get_mix_v1_market_contract_vip_level(request)`
- `public_mix_get_mix_v1_market_fills(request)`
- `public_mix_get_mix_v1_market_fills_history(request)`
- `public_mix_get_mix_v1_market_candles(request)`
- `public_mix_get_mix_v1_market_index(request)`
- `public_mix_get_mix_v1_market_funding_time(request)`
- `public_mix_get_mix_v1_market_history_fundrate(request)`
- `public_mix_get_mix_v1_market_current_fundrate(request)`
- `public_mix_get_mix_v1_market_open_interest(request)`
- `public_mix_get_mix_v1_market_mark_price(request)`
- `public_mix_get_mix_v1_market_symbol_leverage(request)`
- `public_mix_get_mix_v1_market_querypositionlever(request)`
- `public_mix_get_mix_v1_market_open_limit(request)`
- `public_mix_get_mix_v1_market_history_candles(request)`
- `public_mix_get_mix_v1_market_history_index_candles(request)`
- `public_mix_get_mix_v1_market_history_mark_candles(request)`
- `public_mix_get_mix_v1_market_merge_depth(request)`
- `public_mix_get_v2_mix_market_vip_fee_rate(request)`
- `public_mix_get_v2_mix_market_merge_depth(request)`
- `public_mix_get_v2_mix_market_ticker(request)`
- `public_mix_get_v2_mix_market_tickers(request)`
- `public_mix_get_v2_mix_market_fills(request)`
- `public_mix_get_v2_mix_market_fills_history(request)`
- `public_mix_get_v2_mix_market_candles(request)`
- `public_mix_get_v2_mix_market_history_candles(request)`
- `public_mix_get_v2_mix_market_history_index_candles(request)`
- `public_mix_get_v2_mix_market_history_mark_candles(request)`
- `public_mix_get_v2_mix_market_open_interest(request)`
- `public_mix_get_v2_mix_market_funding_time(request)`
- `public_mix_get_v2_mix_market_symbol_price(request)`
- `public_mix_get_v2_mix_market_history_fund_rate(request)`
- `public_mix_get_v2_mix_market_current_fund_rate(request)`
- `public_mix_get_v2_mix_market_contracts(request)`
- `public_mix_get_v2_mix_market_query_position_lever(request)`
- `public_mix_get_v2_mix_market_account_long_short(request)`
- `public_margin_get_margin_v1_cross_public_interestrateandlimit(request)`
- `public_margin_get_margin_v1_isolated_public_interestrateandlimit(request)`
- `public_margin_get_margin_v1_cross_public_tierdata(request)`
- `public_margin_get_margin_v1_isolated_public_tierdata(request)`
- `public_margin_get_margin_v1_public_currencies(request)`
- `public_margin_get_v2_margin_currencies(request)`
- `public_margin_get_v2_margin_market_long_short_ratio(request)`
- `public_earn_get_v2_earn_loan_public_coininfos(request)`
- `public_earn_get_v2_earn_loan_public_hour_interest(request)`
- `public_uta_get_v3_market_instruments(request)`
- `public_uta_get_v3_market_tickers(request)`
- `public_uta_get_v3_market_orderbook(request)`
- `public_uta_get_v3_market_fills(request)`
- `public_uta_get_v3_market_open_interest(request)`
- `public_uta_get_v3_market_candles(request)`
- `public_uta_get_v3_market_history_candles(request)`
- `public_uta_get_v3_market_current_fund_rate(request)`
- `public_uta_get_v3_market_history_fund_rate(request)`
- `public_uta_get_v3_market_risk_reserve(request)`
- `public_uta_get_v3_market_discount_rate(request)`
- `public_uta_get_v3_market_margin_loans(request)`
- `public_uta_get_v3_market_position_tier(request)`
- `public_uta_get_v3_market_oi_limit(request)`
- `private_spot_get_spot_v1_wallet_deposit_address(request)`
- `private_spot_get_spot_v1_wallet_withdrawal_list(request)`
- `private_spot_get_spot_v1_wallet_deposit_list(request)`
- `private_spot_get_spot_v1_account_getinfo(request)`
- `private_spot_get_spot_v1_account_assets(request)`
- `private_spot_get_spot_v1_account_assets_lite(request)`
- `private_spot_get_spot_v1_account_transferrecords(request)`
- `private_spot_get_spot_v1_convert_currencies(request)`
- `private_spot_get_spot_v1_convert_convert_record(request)`
- `private_spot_get_spot_v1_loan_ongoing_orders(request)`
- `private_spot_get_spot_v1_loan_repay_history(request)`
- `private_spot_get_spot_v1_loan_revise_history(request)`
- `private_spot_get_spot_v1_loan_borrow_history(request)`
- `private_spot_get_spot_v1_loan_debts(request)`
- `private_spot_get_v2_spot_trade_orderinfo(request)`
- `private_spot_get_v2_spot_trade_unfilled_orders(request)`
- `private_spot_get_v2_spot_trade_history_orders(request)`
- `private_spot_get_v2_spot_trade_fills(request)`
- `private_spot_get_v2_spot_trade_current_plan_order(request)`
- `private_spot_get_v2_spot_trade_history_plan_order(request)`
- `private_spot_get_v2_spot_account_info(request)`
- `private_spot_get_v2_spot_account_assets(request)`
- `private_spot_get_v2_spot_account_subaccount_assets(request)`
- `private_spot_get_v2_spot_account_bills(request)`
- `private_spot_get_v2_spot_account_transferrecords(request)`
- `private_spot_get_v2_account_funding_assets(request)`
- `private_spot_get_v2_account_bot_assets(request)`
- `private_spot_get_v2_account_all_account_balance(request)`
- `private_spot_get_v2_spot_wallet_deposit_address(request)`
- `private_spot_get_v2_spot_wallet_deposit_records(request)`
- `private_spot_get_v2_spot_wallet_withdrawal_records(request)`
- `private_spot_post_spot_v1_wallet_transfer(request)`
- `private_spot_post_spot_v1_wallet_transfer_v2(request)`
- `private_spot_post_spot_v1_wallet_subtransfer(request)`
- `private_spot_post_spot_v1_wallet_withdrawal(request)`
- `private_spot_post_spot_v1_wallet_withdrawal_v2(request)`
- `private_spot_post_spot_v1_wallet_withdrawal_inner(request)`
- `private_spot_post_spot_v1_wallet_withdrawal_inner_v2(request)`
- `private_spot_post_spot_v1_account_sub_account_spot_assets(request)`
- `private_spot_post_spot_v1_account_bills(request)`
- `private_spot_post_spot_v1_trade_orders(request)`
- `private_spot_post_spot_v1_trade_batch_orders(request)`
- `private_spot_post_spot_v1_trade_cancel_order(request)`
- `private_spot_post_spot_v1_trade_cancel_order_v2(request)`
- `private_spot_post_spot_v1_trade_cancel_symbol_order(request)`
- `private_spot_post_spot_v1_trade_cancel_batch_orders(request)`
- `private_spot_post_spot_v1_trade_cancel_batch_orders_v2(request)`
- `private_spot_post_spot_v1_trade_orderinfo(request)`
- `private_spot_post_spot_v1_trade_open_orders(request)`
- `private_spot_post_spot_v1_trade_history(request)`
- `private_spot_post_spot_v1_trade_fills(request)`
- `private_spot_post_spot_v1_plan_placeplan(request)`
- `private_spot_post_spot_v1_plan_modifyplan(request)`
- `private_spot_post_spot_v1_plan_cancelplan(request)`
- `private_spot_post_spot_v1_plan_currentplan(request)`
- `private_spot_post_spot_v1_plan_historyplan(request)`
- `private_spot_post_spot_v1_plan_batchcancelplan(request)`
- `private_spot_post_spot_v1_convert_quoted_price(request)`
- `private_spot_post_spot_v1_convert_trade(request)`
- `private_spot_post_spot_v1_loan_borrow(request)`
- `private_spot_post_spot_v1_loan_repay(request)`
- `private_spot_post_spot_v1_loan_revise_pledge(request)`
- `private_spot_post_spot_v1_trace_order_ordercurrentlist(request)`
- `private_spot_post_spot_v1_trace_order_orderhistorylist(request)`
- `private_spot_post_spot_v1_trace_order_closetrackingorder(request)`
- `private_spot_post_spot_v1_trace_order_updatetpsl(request)`
- `private_spot_post_spot_v1_trace_order_followerendorder(request)`
- `private_spot_post_spot_v1_trace_order_spotinfolist(request)`
- `private_spot_post_spot_v1_trace_config_gettradersettings(request)`
- `private_spot_post_spot_v1_trace_config_getfollowersettings(request)`
- `private_spot_post_spot_v1_trace_user_mytraders(request)`
- `private_spot_post_spot_v1_trace_config_setfollowerconfig(request)`
- `private_spot_post_spot_v1_trace_user_myfollowers(request)`
- `private_spot_post_spot_v1_trace_config_setproductcode(request)`
- `private_spot_post_spot_v1_trace_user_removetrader(request)`
- `private_spot_post_spot_v1_trace_getremovablefollower(request)`
- `private_spot_post_spot_v1_trace_user_removefollower(request)`
- `private_spot_post_spot_v1_trace_profit_totalprofitinfo(request)`
- `private_spot_post_spot_v1_trace_profit_totalprofitlist(request)`
- `private_spot_post_spot_v1_trace_profit_profithislist(request)`
- `private_spot_post_spot_v1_trace_profit_profithisdetaillist(request)`
- `private_spot_post_spot_v1_trace_profit_waitprofitdetaillist(request)`
- `private_spot_post_spot_v1_trace_user_gettraderinfo(request)`
- `private_spot_post_v2_spot_trade_place_order(request)`
- `private_spot_post_v2_spot_trade_cancel_order(request)`
- `private_spot_post_v2_spot_trade_batch_orders(request)`
- `private_spot_post_v2_spot_trade_batch_cancel_order(request)`
- `private_spot_post_v2_spot_trade_cancel_symbol_order(request)`
- `private_spot_post_v2_spot_trade_place_plan_order(request)`
- `private_spot_post_v2_spot_trade_modify_plan_order(request)`
- `private_spot_post_v2_spot_trade_cancel_plan_order(request)`
- `private_spot_post_v2_spot_trade_batch_cancel_plan_order(request)`
- `private_spot_post_v2_spot_wallet_transfer(request)`
- `private_spot_post_v2_spot_wallet_subaccount_transfer(request)`
- `private_spot_post_v2_spot_wallet_withdrawal(request)`
- `private_spot_post_v2_spot_wallet_cancel_withdrawal(request)`
- `private_spot_post_v2_spot_wallet_modify_deposit_account(request)`
- `private_mix_get_mix_v1_account_account(request)`
- `private_mix_get_mix_v1_account_accounts(request)`
- `private_mix_get_mix_v1_position_singleposition(request)`
- `private_mix_get_mix_v1_position_singleposition_v2(request)`
- `private_mix_get_mix_v1_position_allposition(request)`
- `private_mix_get_mix_v1_position_allposition_v2(request)`
- `private_mix_get_mix_v1_position_history_position(request)`
- `private_mix_get_mix_v1_account_accountbill(request)`
- `private_mix_get_mix_v1_account_accountbusinessbill(request)`
- `private_mix_get_mix_v1_order_current(request)`
- `private_mix_get_mix_v1_order_margincoincurrent(request)`
- `private_mix_get_mix_v1_order_history(request)`
- `private_mix_get_mix_v1_order_historyproducttype(request)`
- `private_mix_get_mix_v1_order_detail(request)`
- `private_mix_get_mix_v1_order_fills(request)`
- `private_mix_get_mix_v1_order_allfills(request)`
- `private_mix_get_mix_v1_plan_currentplan(request)`
- `private_mix_get_mix_v1_plan_historyplan(request)`
- `private_mix_get_mix_v1_trace_currenttrack(request)`
- `private_mix_get_mix_v1_trace_followerorder(request)`
- `private_mix_get_mix_v1_trace_followerhistoryorders(request)`
- `private_mix_get_mix_v1_trace_historytrack(request)`
- `private_mix_get_mix_v1_trace_summary(request)`
- `private_mix_get_mix_v1_trace_profitsettletokenidgroup(request)`
- `private_mix_get_mix_v1_trace_profitdategrouplist(request)`
- `private_mix_get_mix_v1_trade_profitdatelist(request)`
- `private_mix_get_mix_v1_trace_waitprofitdatelist(request)`
- `private_mix_get_mix_v1_trace_tradersymbols(request)`
- `private_mix_get_mix_v1_trace_traderlist(request)`
- `private_mix_get_mix_v1_trace_traderdetail(request)`
- `private_mix_get_mix_v1_trace_querytraceconfig(request)`
- `private_mix_get_v2_mix_account_account(request)`
- `private_mix_get_v2_mix_account_accounts(request)`
- `private_mix_get_v2_mix_account_sub_account_assets(request)`
- `private_mix_get_v2_mix_account_open_count(request)`
- `private_mix_get_v2_mix_account_bill(request)`
- `private_mix_get_v2_mix_market_query_position_lever(request)`
- `private_mix_get_v2_mix_position_single_position(request)`
- `private_mix_get_v2_mix_position_all_position(request)`
- `private_mix_get_v2_mix_position_history_position(request)`
- `private_mix_get_v2_mix_order_detail(request)`
- `private_mix_get_v2_mix_order_fills(request)`
- `private_mix_get_v2_mix_order_fill_history(request)`
- `private_mix_get_v2_mix_order_orders_pending(request)`
- `private_mix_get_v2_mix_order_orders_history(request)`
- `private_mix_get_v2_mix_order_orders_plan_pending(request)`
- `private_mix_get_v2_mix_order_orders_plan_history(request)`
- `private_mix_get_v2_mix_market_position_long_short(request)`
- `private_mix_post_mix_v1_account_sub_account_contract_assets(request)`
- `private_mix_post_mix_v1_account_open_count(request)`
- `private_mix_post_mix_v1_account_setleverage(request)`
- `private_mix_post_mix_v1_account_setmargin(request)`
- `private_mix_post_mix_v1_account_setmarginmode(request)`
- `private_mix_post_mix_v1_account_setpositionmode(request)`
- `private_mix_post_mix_v1_order_placeorder(request)`
- `private_mix_post_mix_v1_order_batch_orders(request)`
- `private_mix_post_mix_v1_order_cancel_order(request)`
- `private_mix_post_mix_v1_order_cancel_batch_orders(request)`
- `private_mix_post_mix_v1_order_modifyorder(request)`
- `private_mix_post_mix_v1_order_cancel_symbol_orders(request)`
- `private_mix_post_mix_v1_order_cancel_all_orders(request)`
- `private_mix_post_mix_v1_order_close_all_positions(request)`
- `private_mix_post_mix_v1_plan_placeplan(request)`
- `private_mix_post_mix_v1_plan_modifyplan(request)`
- `private_mix_post_mix_v1_plan_modifyplanpreset(request)`
- `private_mix_post_mix_v1_plan_placetpsl(request)`
- `private_mix_post_mix_v1_plan_placetrailstop(request)`
- `private_mix_post_mix_v1_plan_placepositionstpsl(request)`
- `private_mix_post_mix_v1_plan_modifytpslplan(request)`
- `private_mix_post_mix_v1_plan_cancelplan(request)`
- `private_mix_post_mix_v1_plan_cancelsymbolplan(request)`
- `private_mix_post_mix_v1_plan_cancelallplan(request)`
- `private_mix_post_mix_v1_trace_closetrackorder(request)`
- `private_mix_post_mix_v1_trace_modifytpsl(request)`
- `private_mix_post_mix_v1_trace_closetrackorderbysymbol(request)`
- `private_mix_post_mix_v1_trace_setupcopysymbols(request)`
- `private_mix_post_mix_v1_trace_followersetbatchtraceconfig(request)`
- `private_mix_post_mix_v1_trace_followerclosebytrackingno(request)`
- `private_mix_post_mix_v1_trace_followerclosebyall(request)`
- `private_mix_post_mix_v1_trace_followersettpsl(request)`
- `private_mix_post_mix_v1_trace_cancelcopytrader(request)`
- `private_mix_post_mix_v1_trace_traderupdateconfig(request)`
- `private_mix_post_mix_v1_trace_mytraderlist(request)`
- `private_mix_post_mix_v1_trace_myfollowerlist(request)`
- `private_mix_post_mix_v1_trace_removefollower(request)`
- `private_mix_post_mix_v1_trace_public_getfollowerconfig(request)`
- `private_mix_post_mix_v1_trace_report_order_historylist(request)`
- `private_mix_post_mix_v1_trace_report_order_currentlist(request)`
- `private_mix_post_mix_v1_trace_querytradertpslratioconfig(request)`
- `private_mix_post_mix_v1_trace_traderupdatetpslratioconfig(request)`
- `private_mix_post_v2_mix_account_set_leverage(request)`
- `private_mix_post_v2_mix_account_set_margin(request)`
- `private_mix_post_v2_mix_account_set_margin_mode(request)`
- `private_mix_post_v2_mix_account_set_position_mode(request)`
- `private_mix_post_v2_mix_order_place_order(request)`
- `private_mix_post_v2_mix_order_click_backhand(request)`
- `private_mix_post_v2_mix_order_batch_place_order(request)`
- `private_mix_post_v2_mix_order_modify_order(request)`
- `private_mix_post_v2_mix_order_cancel_order(request)`
- `private_mix_post_v2_mix_order_batch_cancel_orders(request)`
- `private_mix_post_v2_mix_order_close_positions(request)`
- `private_mix_post_v2_mix_order_place_tpsl_order(request)`
- `private_mix_post_v2_mix_order_place_plan_order(request)`
- `private_mix_post_v2_mix_order_modify_tpsl_order(request)`
- `private_mix_post_v2_mix_order_modify_plan_order(request)`
- `private_mix_post_v2_mix_order_cancel_plan_order(request)`
- `private_user_get_user_v1_fee_query(request)`
- `private_user_get_user_v1_sub_virtual_list(request)`
- `private_user_get_user_v1_sub_virtual_api_list(request)`
- `private_user_get_user_v1_tax_spot_record(request)`
- `private_user_get_user_v1_tax_future_record(request)`
- `private_user_get_user_v1_tax_margin_record(request)`
- `private_user_get_user_v1_tax_p2p_record(request)`
- `private_user_get_v2_user_virtual_subaccount_list(request)`
- `private_user_get_v2_user_virtual_subaccount_apikey_list(request)`
- `private_user_post_user_v1_sub_virtual_create(request)`
- `private_user_post_user_v1_sub_virtual_modify(request)`
- `private_user_post_user_v1_sub_virtual_api_batch_create(request)`
- `private_user_post_user_v1_sub_virtual_api_create(request)`
- `private_user_post_user_v1_sub_virtual_api_modify(request)`
- `private_user_post_v2_user_create_virtual_subaccount(request)`
- `private_user_post_v2_user_modify_virtual_subaccount(request)`
- `private_user_post_v2_user_batch_create_subaccount_and_apikey(request)`
- `private_user_post_v2_user_create_virtual_subaccount_apikey(request)`
- `private_user_post_v2_user_modify_virtual_subaccount_apikey(request)`
- `private_p2p_get_p2p_v1_merchant_merchantlist(request)`
- `private_p2p_get_p2p_v1_merchant_merchantinfo(request)`
- `private_p2p_get_p2p_v1_merchant_advlist(request)`
- `private_p2p_get_p2p_v1_merchant_orderlist(request)`
- `private_p2p_get_v2_p2p_merchantlist(request)`
- `private_p2p_get_v2_p2p_merchantinfo(request)`
- `private_p2p_get_v2_p2p_orderlist(request)`
- `private_p2p_get_v2_p2p_advlist(request)`
- `private_broker_get_broker_v1_account_info(request)`
- `private_broker_get_broker_v1_account_sub_list(request)`
- `private_broker_get_broker_v1_account_sub_email(request)`
- `private_broker_get_broker_v1_account_sub_spot_assets(request)`
- `private_broker_get_broker_v1_account_sub_future_assets(request)`
- `private_broker_get_broker_v1_account_subaccount_transfer(request)`
- `private_broker_get_broker_v1_account_subaccount_deposit(request)`
- `private_broker_get_broker_v1_account_subaccount_withdrawal(request)`
- `private_broker_get_broker_v1_account_sub_api_list(request)`
- `private_broker_get_v2_broker_account_info(request)`
- `private_broker_get_v2_broker_account_subaccount_list(request)`
- `private_broker_get_v2_broker_account_subaccount_email(request)`
- `private_broker_get_v2_broker_account_subaccount_spot_assets(request)`
- `private_broker_get_v2_broker_account_subaccount_future_assets(request)`
- `private_broker_get_v2_broker_manage_subaccount_apikey_list(request)`
- `private_broker_post_broker_v1_account_sub_create(request)`
- `private_broker_post_broker_v1_account_sub_modify(request)`
- `private_broker_post_broker_v1_account_sub_modify_email(request)`
- `private_broker_post_broker_v1_account_sub_address(request)`
- `private_broker_post_broker_v1_account_sub_withdrawal(request)`
- `private_broker_post_broker_v1_account_sub_auto_transfer(request)`
- `private_broker_post_broker_v1_account_sub_api_create(request)`
- `private_broker_post_broker_v1_account_sub_api_modify(request)`
- `private_broker_post_v2_broker_account_modify_subaccount_email(request)`
- `private_broker_post_v2_broker_account_create_subaccount(request)`
- `private_broker_post_v2_broker_account_modify_subaccount(request)`
- `private_broker_post_v2_broker_account_subaccount_address(request)`
- `private_broker_post_v2_broker_account_subaccount_withdrawal(request)`
- `private_broker_post_v2_broker_account_set_subaccount_autotransfer(request)`
- `private_broker_post_v2_broker_manage_create_subaccount_apikey(request)`
- `private_broker_post_v2_broker_manage_modify_subaccount_apikey(request)`
- `private_margin_get_margin_v1_cross_account_riskrate(request)`
- `private_margin_get_margin_v1_cross_account_maxtransferoutamount(request)`
- `private_margin_get_margin_v1_isolated_account_maxtransferoutamount(request)`
- `private_margin_get_margin_v1_isolated_order_openorders(request)`
- `private_margin_get_margin_v1_isolated_order_history(request)`
- `private_margin_get_margin_v1_isolated_order_fills(request)`
- `private_margin_get_margin_v1_isolated_loan_list(request)`
- `private_margin_get_margin_v1_isolated_repay_list(request)`
- `private_margin_get_margin_v1_isolated_interest_list(request)`
- `private_margin_get_margin_v1_isolated_liquidation_list(request)`
- `private_margin_get_margin_v1_isolated_fin_list(request)`
- `private_margin_get_margin_v1_cross_order_openorders(request)`
- `private_margin_get_margin_v1_cross_order_history(request)`
- `private_margin_get_margin_v1_cross_order_fills(request)`
- `private_margin_get_margin_v1_cross_loan_list(request)`
- `private_margin_get_margin_v1_cross_repay_list(request)`
- `private_margin_get_margin_v1_cross_interest_list(request)`
- `private_margin_get_margin_v1_cross_liquidation_list(request)`
- `private_margin_get_margin_v1_cross_fin_list(request)`
- `private_margin_get_margin_v1_cross_account_assets(request)`
- `private_margin_get_margin_v1_isolated_account_assets(request)`
- `private_margin_get_v2_margin_crossed_borrow_history(request)`
- `private_margin_get_v2_margin_crossed_repay_history(request)`
- `private_margin_get_v2_margin_crossed_interest_history(request)`
- `private_margin_get_v2_margin_crossed_liquidation_history(request)`
- `private_margin_get_v2_margin_crossed_financial_records(request)`
- `private_margin_get_v2_margin_crossed_account_assets(request)`
- `private_margin_get_v2_margin_crossed_account_risk_rate(request)`
- `private_margin_get_v2_margin_crossed_account_max_borrowable_amount(request)`
- `private_margin_get_v2_margin_crossed_account_max_transfer_out_amount(request)`
- `private_margin_get_v2_margin_crossed_interest_rate_and_limit(request)`
- `private_margin_get_v2_margin_crossed_tier_data(request)`
- `private_margin_get_v2_margin_crossed_open_orders(request)`
- `private_margin_get_v2_margin_crossed_history_orders(request)`
- `private_margin_get_v2_margin_crossed_fills(request)`
- `private_margin_get_v2_margin_isolated_borrow_history(request)`
- `private_margin_get_v2_margin_isolated_repay_history(request)`
- `private_margin_get_v2_margin_isolated_interest_history(request)`
- `private_margin_get_v2_margin_isolated_liquidation_history(request)`
- `private_margin_get_v2_margin_isolated_financial_records(request)`
- `private_margin_get_v2_margin_isolated_account_assets(request)`
- `private_margin_get_v2_margin_isolated_account_risk_rate(request)`
- `private_margin_get_v2_margin_isolated_account_max_borrowable_amount(request)`
- `private_margin_get_v2_margin_isolated_account_max_transfer_out_amount(request)`
- `private_margin_get_v2_margin_isolated_interest_rate_and_limit(request)`
- `private_margin_get_v2_margin_isolated_tier_data(request)`
- `private_margin_get_v2_margin_isolated_open_orders(request)`
- `private_margin_get_v2_margin_isolated_history_orders(request)`
- `private_margin_get_v2_margin_isolated_fills(request)`
- `private_margin_post_margin_v1_cross_account_borrow(request)`
- `private_margin_post_margin_v1_isolated_account_borrow(request)`
- `private_margin_post_margin_v1_cross_account_repay(request)`
- `private_margin_post_margin_v1_isolated_account_repay(request)`
- `private_margin_post_margin_v1_isolated_account_riskrate(request)`
- `private_margin_post_margin_v1_cross_account_maxborrowableamount(request)`
- `private_margin_post_margin_v1_isolated_account_maxborrowableamount(request)`
- `private_margin_post_margin_v1_isolated_account_flashrepay(request)`
- `private_margin_post_margin_v1_isolated_account_queryflashrepaystatus(request)`
- `private_margin_post_margin_v1_cross_account_flashrepay(request)`
- `private_margin_post_margin_v1_cross_account_queryflashrepaystatus(request)`
- `private_margin_post_margin_v1_isolated_order_placeorder(request)`
- `private_margin_post_margin_v1_isolated_order_batchplaceorder(request)`
- `private_margin_post_margin_v1_isolated_order_cancelorder(request)`
- `private_margin_post_margin_v1_isolated_order_batchcancelorder(request)`
- `private_margin_post_margin_v1_cross_order_placeorder(request)`
- `private_margin_post_margin_v1_cross_order_batchplaceorder(request)`
- `private_margin_post_margin_v1_cross_order_cancelorder(request)`
- `private_margin_post_margin_v1_cross_order_batchcancelorder(request)`
- `private_margin_post_v2_margin_crossed_account_borrow(request)`
- `private_margin_post_v2_margin_crossed_account_repay(request)`
- `private_margin_post_v2_margin_crossed_account_flash_repay(request)`
- `private_margin_post_v2_margin_crossed_account_query_flash_repay_status(request)`
- `private_margin_post_v2_margin_crossed_place_order(request)`
- `private_margin_post_v2_margin_crossed_batch_place_order(request)`
- `private_margin_post_v2_margin_crossed_cancel_order(request)`
- `private_margin_post_v2_margin_crossed_batch_cancel_order(request)`
- `private_margin_post_v2_margin_isolated_account_borrow(request)`
- `private_margin_post_v2_margin_isolated_account_repay(request)`
- `private_margin_post_v2_margin_isolated_account_flash_repay(request)`
- `private_margin_post_v2_margin_isolated_account_query_flash_repay_status(request)`
- `private_margin_post_v2_margin_isolated_place_order(request)`
- `private_margin_post_v2_margin_isolated_batch_place_order(request)`
- `private_margin_post_v2_margin_isolated_cancel_order(request)`
- `private_margin_post_v2_margin_isolated_batch_cancel_order(request)`
- `private_copy_get_v2_copy_mix_trader_order_current_track(request)`
- `private_copy_get_v2_copy_mix_trader_order_history_track(request)`
- `private_copy_get_v2_copy_mix_trader_order_total_detail(request)`
- `private_copy_get_v2_copy_mix_trader_profit_history_summarys(request)`
- `private_copy_get_v2_copy_mix_trader_profit_history_details(request)`
- `private_copy_get_v2_copy_mix_trader_profit_details(request)`
- `private_copy_get_v2_copy_mix_trader_profits_group_coin_date(request)`
- `private_copy_get_v2_copy_mix_trader_config_query_symbols(request)`
- `private_copy_get_v2_copy_mix_trader_config_query_followers(request)`
- `private_copy_get_v2_copy_mix_follower_query_current_orders(request)`
- `private_copy_get_v2_copy_mix_follower_query_history_orders(request)`
- `private_copy_get_v2_copy_mix_follower_query_settings(request)`
- `private_copy_get_v2_copy_mix_follower_query_traders(request)`
- `private_copy_get_v2_copy_mix_follower_query_quantity_limit(request)`
- `private_copy_get_v2_copy_mix_broker_query_traders(request)`
- `private_copy_get_v2_copy_mix_broker_query_history_traces(request)`
- `private_copy_get_v2_copy_mix_broker_query_current_traces(request)`
- `private_copy_get_v2_copy_spot_trader_profit_summarys(request)`
- `private_copy_get_v2_copy_spot_trader_profit_history_details(request)`
- `private_copy_get_v2_copy_spot_trader_profit_details(request)`
- `private_copy_get_v2_copy_spot_trader_order_total_detail(request)`
- `private_copy_get_v2_copy_spot_trader_order_history_track(request)`
- `private_copy_get_v2_copy_spot_trader_order_current_track(request)`
- `private_copy_get_v2_copy_spot_trader_config_query_settings(request)`
- `private_copy_get_v2_copy_spot_trader_config_query_followers(request)`
- `private_copy_get_v2_copy_spot_follower_query_traders(request)`
- `private_copy_get_v2_copy_spot_follower_query_trader_symbols(request)`
- `private_copy_get_v2_copy_spot_follower_query_settings(request)`
- `private_copy_get_v2_copy_spot_follower_query_history_orders(request)`
- `private_copy_get_v2_copy_spot_follower_query_current_orders(request)`
- `private_copy_post_v2_copy_mix_trader_order_modify_tpsl(request)`
- `private_copy_post_v2_copy_mix_trader_order_close_positions(request)`
- `private_copy_post_v2_copy_mix_trader_config_setting_symbols(request)`
- `private_copy_post_v2_copy_mix_trader_config_setting_base(request)`
- `private_copy_post_v2_copy_mix_trader_config_remove_follower(request)`
- `private_copy_post_v2_copy_mix_follower_setting_tpsl(request)`
- `private_copy_post_v2_copy_mix_follower_settings(request)`
- `private_copy_post_v2_copy_mix_follower_close_positions(request)`
- `private_copy_post_v2_copy_mix_follower_cancel_trader(request)`
- `private_copy_post_v2_copy_spot_trader_order_modify_tpsl(request)`
- `private_copy_post_v2_copy_spot_trader_order_close_tracking(request)`
- `private_copy_post_v2_copy_spot_trader_config_setting_symbols(request)`
- `private_copy_post_v2_copy_spot_trader_config_remove_follower(request)`
- `private_copy_post_v2_copy_spot_follower_stop_order(request)`
- `private_copy_post_v2_copy_spot_follower_settings(request)`
- `private_copy_post_v2_copy_spot_follower_setting_tpsl(request)`
- `private_copy_post_v2_copy_spot_follower_order_close_tracking(request)`
- `private_copy_post_v2_copy_spot_follower_cancel_trader(request)`
- `private_tax_get_v2_tax_spot_record(request)`
- `private_tax_get_v2_tax_future_record(request)`
- `private_tax_get_v2_tax_margin_record(request)`
- `private_tax_get_v2_tax_p2p_record(request)`
- `private_convert_get_v2_convert_currencies(request)`
- `private_convert_get_v2_convert_quoted_price(request)`
- `private_convert_get_v2_convert_convert_record(request)`
- `private_convert_get_v2_convert_bgb_convert_coin_list(request)`
- `private_convert_get_v2_convert_bgb_convert_records(request)`
- `private_convert_post_v2_convert_trade(request)`
- `private_convert_post_v2_convert_bgb_convert(request)`
- `private_earn_get_v2_earn_savings_product(request)`
- `private_earn_get_v2_earn_savings_account(request)`
- `private_earn_get_v2_earn_savings_assets(request)`
- `private_earn_get_v2_earn_savings_records(request)`
- `private_earn_get_v2_earn_savings_subscribe_info(request)`
- `private_earn_get_v2_earn_savings_subscribe_result(request)`
- `private_earn_get_v2_earn_savings_redeem_result(request)`
- `private_earn_get_v2_earn_sharkfin_product(request)`
- `private_earn_get_v2_earn_sharkfin_account(request)`
- `private_earn_get_v2_earn_sharkfin_assets(request)`
- `private_earn_get_v2_earn_sharkfin_records(request)`
- `private_earn_get_v2_earn_sharkfin_subscribe_info(request)`
- `private_earn_get_v2_earn_sharkfin_subscribe_result(request)`
- `private_earn_get_v2_earn_loan_ongoing_orders(request)`
- `private_earn_get_v2_earn_loan_repay_history(request)`
- `private_earn_get_v2_earn_loan_revise_history(request)`
- `private_earn_get_v2_earn_loan_borrow_history(request)`
- `private_earn_get_v2_earn_loan_debts(request)`
- `private_earn_get_v2_earn_loan_reduces(request)`
- `private_earn_get_v2_earn_account_assets(request)`
- `private_earn_post_v2_earn_savings_subscribe(request)`
- `private_earn_post_v2_earn_savings_redeem(request)`
- `private_earn_post_v2_earn_sharkfin_subscribe(request)`
- `private_earn_post_v2_earn_loan_borrow(request)`
- `private_earn_post_v2_earn_loan_repay(request)`
- `private_earn_post_v2_earn_loan_revise_pledge(request)`
- `private_common_get_v2_common_trade_rate(request)`
- `private_uta_get_v3_account_assets(request)`
- `private_uta_get_v3_account_settings(request)`
- `private_uta_get_v3_account_financial_records(request)`
- `private_uta_get_v3_account_repayable_coins(request)`
- `private_uta_get_v3_account_payment_coins(request)`
- `private_uta_get_v3_account_convert_records(request)`
- `private_uta_get_v3_account_transferable_coins(request)`
- `private_uta_get_v3_account_sub_transfer_record(request)`
- `private_uta_get_v3_ins_loan_transfered(request)`
- `private_uta_get_v3_ins_loan_symbols(request)`
- `private_uta_get_v3_ins_loan_risk_unit(request)`
- `private_uta_get_v3_ins_loan_repaid_history(request)`
- `private_uta_get_v3_ins_loan_product_infos(request)`
- `private_uta_get_v3_ins_loan_loan_order(request)`
- `private_uta_get_v3_ins_loan_ltv_convert(request)`
- `private_uta_get_v3_ins_loan_ensure_coins_convert(request)`
- `private_uta_get_v3_position_current_position(request)`
- `private_uta_get_v3_position_history_position(request)`
- `private_uta_get_v3_trade_order_info(request)`
- `private_uta_get_v3_trade_unfilled_orders(request)`
- `private_uta_get_v3_trade_history_orders(request)`
- `private_uta_get_v3_trade_fills(request)`
- `private_uta_get_v3_user_sub_list(request)`
- `private_uta_get_v3_user_sub_api_list(request)`
- `private_uta_post_v3_account_set_leverage(request)`
- `private_uta_post_v3_account_set_hold_mode(request)`
- `private_uta_post_v3_account_repay(request)`
- `private_uta_post_v3_account_transfer(request)`
- `private_uta_post_v3_account_sub_transfer(request)`
- `private_uta_post_v3_account_max_open_available(request)`
- `private_uta_post_v3_ins_loan_bind_uid(request)`
- `private_uta_post_v3_trade_place_order(request)`
- `private_uta_post_v3_trade_modify_order(request)`
- `private_uta_post_v3_trade_cancel_order(request)`
- `private_uta_post_v3_trade_place_batch(request)`
- `private_uta_post_v3_trade_batch_modify_order(request)`
- `private_uta_post_v3_trade_cancel_batch(request)`
- `private_uta_post_v3_trade_cancel_symbol_order(request)`
- `private_uta_post_v3_trade_close_positions(request)`
- `private_uta_post_v3_user_create_sub(request)`
- `private_uta_post_v3_user_freeze_sub(request)`
- `private_uta_post_v3_user_create_sub_api(request)`
- `private_uta_post_v3_user_update_sub_api(request)`
- `private_uta_post_v3_user_delete_sub_api(request)`

### WS Unified

- `describe(self)`
- `get_inst_type(self, market, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `un_watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `un_watch_ohlcv(self, symbol: str, timeframe='1m', params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `un_watch_channel(self, symbol: str, channel: str, messageHashTopic: str, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `watch_public(self, messageHash, args, params={})`
- `un_watch_public(self, messageHash, args, params={})`
- `watch_public_multiple(self, messageHashes, argsArray, params={})`
- `authenticate(self, params={})`
- `watch_private(self, messageHash, subscriptionHash, args, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.