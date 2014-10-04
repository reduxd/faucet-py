faucet.py
=========

**faucet.py** is a cli downloader for [drip.fm](https://drip.fm/) releases.

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

Clone this repository to get the latest and greatest code
```
(faucet)$ git clone https://github.com/reduxd/faucet-py.git

Cloning into 'faucet-py'...
remote: Counting objects: 12, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 1), reused 2 (delta 0)
Unpacking objects: 100% (12/12), done.
Checking connectivity... done.
```

### Usage
In order to use begin using faucet, you must pass credentials as environment variables
```
(faucet)$ export FUSER=user@gmail.com
(faucet)$ export FPASS=password123
```

Script usage is as follows
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
