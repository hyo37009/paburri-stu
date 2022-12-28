class station:
    def __init__(self, name: str, line: str):
        self.name = name
        self.line = set(line)
        self.hwan = False
        self.neighbor = [None, None]

    def __str__(self):
        return self.name

    def connection(self, station, prev=0):
        '''
        각 노드를 잇는 작업
        prev가 0이면 station의 앞에, 1이면 뒤에 이음
        '''
        if prev:
            self.neighbor[0] = station
        elif not prev:
            self.neighbor[1] = station
        else:
            raise KeyError('0 또는 1만을 입력하셈')
        return True

    def prevStation(self):
        return self.neighbor[0]

    def nextStation(self):
        return self.neighbor[1]

    def printconnection(self):
        return str(self.prevStation(), self.nextStation())

    def printline(self):
        return ", ".join(self.line)


class line:
    hwan = ['충무로', '총신대입구(이수)', '고속터미널', '노원']

    def __init__(self, linename: str, linenum: int):
        self.linename = linename
        self.linenum = linenum  # 속해있는 역의 개수
        self.linelist = [None] * linenum
        self.linestationNames = []

    def __len__(self):
        return self.linenum

    def setline(self, line: list):
        for i in range(self.linenum):
            # station class를 생성합니다(double linked node)
            self.linelist[i] = station(line[i], [self.linename])
            self.linestationNames.append(line[i])

        for i in range(self.linenum):
            if i != 0 and i != len(self.linelist) - 1:
                # 연결관계를 설정합니다
                self.linelist[i].connection(self.linelist[i - 1], 0)
                self.linelist[i].connection(self.linelist[i + 1], 1)
            if i == 0:
                self.linelist[i].connection(self.linelist[i + 1], 1)
            if i == len(self.linelist) - 1:
                self.linelist[i].connection(self.linelist[i - 1], 0)

            # 환승역 여부를 저장합니다.
            if self.linelist[i].name in self.hwan:
                self.linelist[i].hwan = True

    def ret_station(self, station):
        if type(station) == int:
            return self.linelist[station]
        for i in range(len(self.linelist)):
            if self.linelist[i].name == station:
                return self.linelist[i]
        return False

    def howfar(self, st1: station, st2: station):
        if type(st1) != station or type(st2) != station:
            raise ValueError('입력값이 station이 아닙니다')

        num1 = self.linelist.index(st1)
        num2 = self.linelist.index(st2)
        return abs(num1 - num2)