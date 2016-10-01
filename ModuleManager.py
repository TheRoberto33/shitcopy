
def initManager(client):
    global __client
    global __modules

    __client = client
    __modules = []


def initVoice(vclient):
    global __vclient
    __vclient = vclient

def addmodule(module):
    __modules.append(module)

def modules():
    return __modules

def client():
    return __client

def vclient():
    return __vclient

