import json


class FileSystem(object):
    def getData(self, filename):
        f = open("files/" + filename + ".json", 'r')
        s = f.read()
        return json.loads(s)

    def setData(self, filename, data):
        f = open("files/" + filename + ".json", "w")
        f.write(str(data))

