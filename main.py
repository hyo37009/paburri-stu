from linePrepare import line3, line4, line7

def search(st, end, stline):
    lines = [line3, line4, line7]

    # 환승을 안하는 경우 (같은 노선인 경우)
    if st.line & end.line:
        # 같은 라인이니까 환승 안함
        route = [st,end]
        return route

    else:
        hwanLine = list(end.line)[0]
        hwan = []

        for linenum in lines:
            if linenum.linename == hwanLine:
                hwanLine = linenum

        for station in hwanLine.linelist:
            if station.hwan:
                if (st.line | end.line) == station.line:
                    hwan.append(station)

        # 환승역 1개만 나옴 -> len(hwan) == 1
        # 환승역 2개 이상 나옴 -> len(hwan) >=2
        # a, b, c

        if len(hwan) == 1:
            route = [st, hwan[0], end]
            return route

        elif len(hwan) >= 2:
            far = []
            for hwanSt in hwan:
                first = stline.howfar(st, hwanSt)
                sec = hwanLine.howfar(hwanSt, end)
                far.append(first+sec)

            hwan = hwan[far.index(min(far))]
            route = [st, hwan, end]
            return route

if __name__ == '__main__':
    # route = search(line3.ret_station('대화'), line7.ret_station('건대입구'), line3)
    # for st in route:
    #     print(st.name, end=' ')

    '''
    지하철 검색 시스템입니다.
    출발 역을 기재해주세요 : /대화역
    끝 역을 기재해주세요 : /성수
    역 이름을 다시 기재해주세요 : 내방
    
    시작 역 : 대화 (3호선)
              |
    환승 역 : 무슨역 (무슨호선)
              |                        
    도착 역 : 내방역 (무슨 호선)
    '''

    stations = line3.linestationNames + line4.linestationNames + line7.linestationNames

    print('지하철 검색 시스템입니다.')
    print('시작역을 입력해 주세요')
    while True:
        st = input()
        if st in stations:
            break
        print('역 이름을 다시 입력해주세요')

    print('도착역을 입력해 주세요')
    while True:
        end = input()
        if end in stations:
            break
        print('역 이름을 다시 입력해주세요')

    print('------ 검색을 시작합니다 ------')
    lines = [line3, line4, line7]
    for linenum in lines:
        if st in linenum.linestationNames:
            stline = linenum
            st = stline.ret_station(st)
        if end in linenum.linestationNames:
            end = linenum.ret_station(end)

    route = search(st, end, stline)
    print('검색이 완료되었습니다.')
    for i in range(len(route)):
        if i == 0:
            print('시작역 : ', route[i])
        elif i == len(route) - 1:
            print('도착역 : ', route[i])
            break
        else:
            print('환승역 : ', route[i])

        print('           | ')
