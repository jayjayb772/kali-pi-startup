import netifaces as ni


class Interface:
    ip = ""
    iprange = ""
    iface = ""

    def __init__(self, iface):
        self.iface = iface
        print("hello world")
        # get ip of iface
        ni.ifaddresses(self.iface)
        self.ip = ni.ifaddresses(self.iface)[ni.AF_INET][0]['addr']
        temp = self.ip.split(".")
        temp[3] = "1-255"
        dot = "."
        self.iprange = dot.join(temp)

    def getip(self):
        return self.ipa

    def getrange(self):
        return self.iprange

    def getIfaceName(self):
        return self.iface
