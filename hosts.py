import os

HOSTS_PATH = "C:/Windows/System32/drivers/etc/hosts"


class Hosts:
    def __init__(self):
        self.filename: str = None
        self.serv_ip: str = None
        self.serv_mirror: str = None

        # shit shit
        self.header: str = "butta dawg"


        # internal shit
        self._lines: list = None

    @classmethod
    def fromFile(cls, ip:str, mirror: str = None) -> 'Hosts':
        h = cls()

        #filename = filename or HOSTS_PATH
        filename = HOSTS_PATH

        # meme
        h.filename = filename
        h.serv_ip = ip
        h.serv_mirror = mirror

        # checks if filename is a directory
        if os.path.isdir(filename):
            raise IsADirectoryError()



        return h

    @property
    def lines(self) -> list:
        #if not self._lines:
        with open(self.filename, 'r') as file:
            return file.read().splitlines() 

        #return self._lines



    @property
    def is_connected(self) -> bool:
        for line in self.lines:
            
            if line.startswith('#') or 'ppy.sh' not in line:
                continue

            if self.serv_ip in line or self.serv_mirror in line:
                return True

        return False




    def connect(self) -> bool:
        if self.is_connected:
            return False


        for n, line in enumerate(self.lines):
            if not line.startswith("#") and 'ppy.sh' in line:
                self.lines[n] = '#' + line


        # write shit
        address = self.serv_ip
        hosts = self.lines

        #hosts.append("\n")
        hosts.append(f"# {self.header}")
        hosts.append("{} osu.ppy.sh".format(address))
        hosts.append("{} a.ppy.sh".format(address))
        hosts.append("{} i.ppy.sh".format(address))
        hosts.append("{} c.ppy.sh".format(address))
        hosts.append("{} ce.ppy.sh".format(address))

        for x in range(4, 7):
            hosts.append("{} c{}.ppy.sh".format(address, x))


        if self.serv_mirror:
            ...
            #for x in range(4, 7):
                #hosts.append("{} bm{}.ppy.sh".format(self.serv_mirror, x))

        hosts.append("\n")

        file = open(self.filename, 'w')
        file.write('\n'.join(hosts))
        file.close()

        # True if shit is fayn else False
        return True

    def disconnect(self) -> bool:
        if not self.is_connected:
            return False

        hosts = self.lines
        for n, line in enumerate(hosts):
            # check for header
            if line.startswith("#") and self.header in line:
                for j in range(n, n+10):
                    hosts[j] = "-1|"

                break

        hosts = [line.strip() for line in hosts if line != '-1|']

        file = open(self.filename, 'w')
        file.write('\n'.join(hosts))
        file.close()

        return True
        









        

        

if __name__ == '__main__':
    t = Hosts.fromFile(HOSTS_PATH, '51.161.34.235')
    #t.connect()
    print(t.is_connected)
    t.disconnect()


