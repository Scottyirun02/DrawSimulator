

import random

d1=(("Jeonbuk Motors","KOR"),("Buriram United" ,"THA"),("Yokohama Marinos" ,"JPN"),("Ulsan Hyundai","KOR"),("Wuhan","CHN"))
d2=(("Kawasaki Frontale","JPN"),("Pohang Steelers","KOR"),("Shandong","CHN"),("Ventforet Kofu","JPN"),("Bangkok United","THA"))
d3=(("Lion City Sailors","SIN"),("Kaya","PHI"),("Melborun City","AUS"),("Juhor JDT","MAL"),("Hanoi","VIE"))
d4=(("Kitchee","HKG"),("Incheon United","KOR"),("Zhejiang","CHN"),("BG Pathun United","THA"),("Urawa Red Diamonds","JPN"))

f1 = list(d1)
f2 = list(d2)
f3 = list(d3)
f4 = list(d4)
fenzu = []
for i in range(5):
    fenzu.append([])

random.shuffle(f1)
random.shuffle(f2)
random.shuffle(f3)
random.shuffle(f4)
# 抽第一档球队
for m in range(5):
    fenzu[m].append(f1[m])
# 抽第二档球队
for n in range(5):
    availgroup = []
    drawteam = f2[n]
    for j in range(5):
        if len(fenzu[j]) < 2:
            fircountry = fenzu[j][0][1]
            seccountry = drawteam[1]
            if fircountry != seccountry:
                if fircountry == 'RUS' and seccountry == 'UKR':
                    continue
                elif fircountry == 'UKR' and seccountry == 'RUS':
                    continue
                else:
                    availgroup.append(j)

            else:
                continue
    random.shuffle(availgroup)
    fenzu[availgroup[0]].append(drawteam)
# 抽第三档球队
for n in range(5):
    availgroup = []
    drawteam = f3[n]
    for j in range(5):
        if len(fenzu[j]) < 3:
            fircountry = fenzu[j][0][1]
            seccountry = fenzu[j][1][1]
            thircountry = drawteam[1]
            if thircountry != fircountry and thircountry != seccountry:
                if thircountry == 'RUS':
                    if fircountry == 'UKR' or seccountry == 'UKR':
                        continue
                    else:
                        availgroup.append(j)
                elif thircountry == 'UKR':
                    if fircountry == 'RUS' or seccountry == 'RUS':
                        continue

                    else:
                        availgroup.append(j)
                else:
                    availgroup.append(j)

            else:
                continue
    random.shuffle(availgroup)
    fenzu[availgroup[0]].append(drawteam)
# 抽第四档球队
for n in range(5):
    availgroup = []
    drawteam = f4[n]
    for j in range(5):
        if len(fenzu[j]) < 4:
            fircountry = fenzu[j][0][1]
            seccountry = fenzu[j][1][1]
            thircountry = fenzu[j][2][1]
            fourcountry = drawteam[1]
            if fourcountry != fircountry and fourcountry != seccountry and fourcountry != thircountry:
                if fourcountry == 'RUS':
                    if fircountry == 'UKR' or seccountry == 'UKR' or thircountry == 'UKR':
                        continue
                    else:
                        availgroup.append(j)
                elif fourcountry == 'UKR':
                    if fircountry == 'RUS' or seccountry == 'RUS' or thircountry == 'RUS':
                        continue

                    else:
                        availgroup.append(j)
                else:
                    availgroup.append(j)

            else:
                continue
    random.shuffle(availgroup)
    fenzu[availgroup[0]].append(drawteam)

for n in range(5):
    print(fenzu[n])
