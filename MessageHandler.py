class MessageHandler(object):
    def __init__(self, pmsg: dict):
        self.messages = pmsg

    def getMessage(self, msgid: str) -> str:
        path = msgid.split("-")
        res = self.messages
        for p in path:
            res = res[p]
        return res