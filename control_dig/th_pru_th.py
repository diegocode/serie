import threading

def hello(arg, dos, numero):
    print dos, arg, numero * 5

a = "toto"
b = "poroto"
c = 5

t = threading.Timer(2, hello, [a,b, c])
t.start()

while 1:
    pass