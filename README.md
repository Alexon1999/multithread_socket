```
$ python3 -m venv env
$ source env/bin/activate

$ python3 multithreadserver.py
$ python3 multithreadserver.py 8001

$ python3 multihreadclient.py
$ python3 multihreadclient.py 8001

-------------------------

# docker-compose throws EOFError: EOF when reading a line, because we use inputs in our script (should run on terminal in interactive way) :

$ docker build -t socket_server .
$ docker run -it -p 8000:8000 socket_server 

https://stackoverflow.com/questions/44210435/docker-python-file-input-selector

```