# IndicoServer
[![Codeship Build Status](https://codeship.com/projects/03f7b580-1487-0133-55c9-6ebb30d8a8ec/status?branch=master)](https://codeship.com/projects/03f7b580-1487-0133-55c9-6ebb30d8a8ec/status?branch=master)

[![Travis Build Status](https://travis-ci.org/indico/indico-Server.svg?branch=master)](https://travis-ci.org/indico/indico-Server)

Python + Tornado + Motor (MongoDb)

 - Maintained at 100% Test Coverage.
 - Built to support a very general use case as an API server
 - Open to issues + pull requests

Installation
--------------------------
Install via setup.py
```
python setup.py develop
```
Automatically installs relevant requirements , as listed in reqs.txt

Testing
--------------------------

Install nosetests:
```
sudo pip install nose
```

Run tests
```
nosetests $IndicoServer
```
