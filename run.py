import yaml
import pyupbit

def get_config():
    with open(r'config.yaml', encoding='UTF-8') as f:
        env = yaml.load(f, Loader=yaml.FullLoader)
    return env

if __name__ == "__main__":
    # get env
    config = get_config()

    # Quotaion
    print(pyupbit.markets().head())
    print(pyupbit.candles(1, "KRW-BTC", count=10).head())
    print(pyupbit.orderbook("KRW-BTC").head())

    # Exchange
    upbit = pyupbit.create_upbit(**config['upbit'])
    print(upbit.accounts())
