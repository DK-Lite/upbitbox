import yaml
import upbitbox

def get_config():
    with open(r'config.yaml', encoding='UTF-8') as f:
        env = yaml.load(f, Loader=yaml.FullLoader)
    return env

if __name__ == "__main__":
    # get env
    config = get_config()

    # Quotaion
    print(upbitbox.markets().head())
    print(upbitbox.candles(1, "KRW-BTC", count=10).head())
    print(upbitbox.orderbook("KRW-BTC").head())

    # Exchange
    upbit = upbitbox.create_upbit(**config['upbit'])
    print(upbit.accounts())
