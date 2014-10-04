faucet.py
=========

**faucet.py** is a cli downloader for drip.fm releases

### Pre-requisites
As with anything Python, it is recommended to use virtualenv.

```
$ wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.6.tar.gz
$ tar xvfz virtualenv-1.11.6.tar.gz
$ python virtualenv-1.11.6/virtualenv.py --system-site-packages -p /usr/bin/python2.7 ~/faucet/
$ source ~/faucet/bin/activate
```

### Installation
Once virtualenv is set up, requests must be installed

```
(faucet)$ pip install requests

Downloading/unpacking requests
  Downloading requests-2.4.1-py2.py3-none-any.whl (458kB): 458kB downloaded
Installing collected packages: requests
Successfully installed requests
Cleaning up...
```

### Usage
```
(faucet)$ python faucet.py <drip url> <format> <output>
```

### Example
```
(faucet)$ python faucet.py https://drip.fm/owsla/releases/jack-u-take-u-there mp3 jacku.zip

[!] faucet.py by reduxd
[!] drip.fm downloader client
[!] http://github.com/reduxd/faucet-py

[!] Logged in as Itzael Martinez
    - Subscriptions:
      - Mad Decent
      - OWSLA

[!] Processing release:
      - Take Ü There by Jack Ü
      - OWSLA/Mad Decent/Big Beat/Atlantic Records

[!] Download successful!
```
