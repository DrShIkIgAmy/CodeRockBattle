import sys
import datetime
import re


#here goes the class written by myself in my IDE
class Robot:
    def __init__(self, initStr) -> None:
        self.GameOverTime = []
        self.parseString(initStr)

    def parseString(self, robotInfo: str):
        roboName = robotInfo.split('|')[0]
        dateInfo = robotInfo.replace(roboName+'| ','')
        roboName = roboName.replace('R:','')
        self.Name = roboName.replace(' ','')
        reg = r'[0-9]+\s[0-9]+:[0-9]+\s\-\s[0-9]+\s[0-9]+:[0-9]+'
        for i in re.findall(reg,dateInfo):
            s_time, e_time = self.parseStringDate(i)
            self.GameOverTime.append([s_time, e_time])
    
    def parseStringDate(self, str_date: str):
        splited_span = str_date.split(' - ')
        start_date_time = datetime.datetime.strptime(splited_span[0],'%d %H:%M')
        end_date_time = datetime.datetime.strptime(splited_span[1],'%d %H:%M')
        return start_date_time, end_date_time

    def isContinue(self, time_shot) -> bool:
        for i in self.GameOverTime:
            if time_shot >= i[0] and time_shot <= i[1]:
                return False
        return True


def retrieve_data(inp_str):
    lines = inp_str.split('\n')
    robotInfo = []
    queryInfo = []
    for i in lines:
        if len(i) == 0:
            continue
        if i[0] == 'R':
            robotInfo.append(i)
        elif i[0] =='T':
            queryInfo.append(i)
    
    robots = []
    queryTime = []
    reg = r'[0-9]+\s[0-9]+:[0-9]+'
    for i in robotInfo:
        robots.append(Robot(i))
    for i in queryInfo:
        if len(i)==0:
            continue
        q_time = re.findall(reg, i)[0]
        queryTime.append(datetime.datetime.strptime(q_time,'%d %H:%M'))
    return robots, queryTime



response = ''
for line in sys.stdin: # get input strings one by one
    response+=line
robots, query = retrieve_data(response)
for i in query:
    print(i.strftime('%-d %-H:%M'))
    for j in robots:
        status = 'GAME CONTINUES' if j.isContinue(i) else 'GAME OVER'
        res_str = f'{j.Name} {status}'
        print(res_str)