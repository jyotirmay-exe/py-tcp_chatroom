
<h1>TCP Chatroom in Python</h1>
  

Simple TCP/IP based chatroom written in python using client-server connection architecture. The listening ip and port, and connecting ip and port can be specified for client and server in `configs\cl-config.json` and `configs\svr-config.json` respectively.


<h1>How to use it?</h1>

There's no need to install any external library/module. All the modules used are distributed in the Python Standard Library.

First off, clone this repo:
`git clone https://github.com/jyotirmay-exe/py-tcp_chatroom.git`

Execute the server script:
`python server.py`

Now execute as many client scripts as you need:
`python client.py`

This works both locally and remotely if there's no port forwarding or firewall issues.

All the chat logs are recorded in `configs\logs.txt` file.

That's it :)