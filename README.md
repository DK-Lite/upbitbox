upbitbox is Python module for Upbit exchange api 

## Use Python Package (Dependencies)
upbitbox requires:

- requests (>= 2.27.1)
- pandas (>= 1.4.2)
- PyJWT (>= 2.3.0)
- PyYAML (>= 6.0)

## Installation
```cmd
python3 -m venv .venv
pip install -r requirements.txt
```

## Get Started (Example)
```python
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
```
```cmd
python run.py
```

### config.yaml
```yaml
upbit:
    access_key: ""
    secret_key: ""
```



## Source code
You can check the lastest sources with the command:
```cmd
git clone https://github.com/DK-Lite/upbitbox.git
```

## Testing
```cmd
pytest upbitbox
```
