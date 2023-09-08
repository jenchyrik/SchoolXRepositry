from import_this import RACE_DATA
def timefunc(a):
    h = a // 3600
    m = (a % 3600) // 60
    s = (a % 60)
    return (h,m,s)
    # print (h, 'час(а/ов) и', m, 'минут(а/ы)', s, 'секунд(а/ы)')

win: str = ""
for i in RACE_DATA.values():
    if i.get("FinishedPlace") == 1:
        win = f"Выиграл - {i.get('RacerName').upper()} !!! Поздравляем!"
        break
win += "\n"+"_"*len(win)
print(win)

print("\nПервые три места:\n")
for place in range(1, 4):
    answer = f"\tГонщик на {'первом' if place == 1 else 'втором' if place == 2 else 'третьем'} месте:\n"
    for i in RACE_DATA.values():
        if i.get("FinishedPlace",-1) == place:
            answer += f"\t\tИмя:{i.get('RacerName')}\n"
            answer += f"\t\tКоманда:{i.get('RacerTeam')}\n"
            time = timefunc(i.get('FinishedTimeSeconds',0))
            answer += f"\t\tВремя:{time[0]}:{time[1]}:{time[2]}\n"
    print(answer)
