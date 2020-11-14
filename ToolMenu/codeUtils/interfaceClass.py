import netifaces as ni


class Interface:
    def __init__(self, iface):
        self.name = iface
        print("hello world")
        # get ip of iface
        ni.ifaddresses(self.name)
        print(ni.ifaddresses(self.name))
        self.ip = ni.ifaddresses(self.name)[ni.AF_INET][0]['addr']
        temp = self.ip.split(".")
        temp[3] = "1-255"
        dot = "."
        self.iprange = dot.join(temp)

    def getip(self):
        return self.ipa

    def getrange(self):
        return self.iprange

    def getIfaceName(self):
        return self.name
