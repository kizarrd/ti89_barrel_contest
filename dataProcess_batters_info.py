import csv
# 0. GYEAR
# 1. G_ID
# 2. PIT_ID
# 3. PCODE
# 4. T_ID
# 5. INN
# 6. HIT_VEL
# 7. HIT_ANG_VER
# 8. HIT_RESULT
# 9. PIT_VEL
# 10. STADIUM
NUM_DATA = 120746
NUM_VEL = 201
VEL_MIN = 10
VEL_MAX = 210
NUM_ANG = 160
ANG_MIN = -69
ANG_MAX = 90
filename='combined_wo_emptyEnd.csv'
filename2='batter_info.csv'
hitList = [[] for _ in range(120746)]
batterList = [[] for _ in range(1099)]
count = 0
i = 0
j = 0
with open(filename,'r', encoding='UTF8') as data:
   for line in csv.reader(data):
       hitList[i]=line
       i+=1
with open(filename2,'r', encoding='UTF8') as data:
   for line2 in csv.reader(data):
       batterList[j]=line2
       j+=1
def roundUp(num):
    if num>=0:
        return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)
    else:
        return int(num) if (num-int(num)) >= -0.5 else int(num)-1

batterDict = {}
for eachHit in hitList[1:]:
    hitVel = roundUp(float(eachHit[6]))
    hitAng = roundUp(float(eachHit[7]))
    batterCode = eachHit[3]
    hitResult = eachHit[8]
    barrel=False
    if hitVel>=149 and 7<=hitAng<=46 :
        barrel = (hitVel==149 and 26<=hitAng<=27)or(hitVel==150 and 26<=hitAng<=34)or(hitVel==151 and 24<=hitAng<=34)or(hitVel==152 and 22<=hitAng<=34)or(hitVel==153 and 22<=hitAng<=33)or(154<=hitVel<=155 and 22<=hitAng<=35)or(156<=hitVel<=157 and 21<=hitAng<=36)or(hitVel==158 and 21<=hitAng<=37)or(hitVel==159 and 19<=hitAng<=38)or(160<=hitVel<=161 and 20<=hitAng<=38)or(162<=hitVel<=163 and 19<=hitAng<=42)or(hitVel==164 and 18<=hitAng<=42)or(hitVel==165 and 19<=hitAng<=46)or(166<=hitVel<=167 and 18<=hitAng<=41)or(hitVel==168 and 8<=hitAng<=42)or(hitVel==169 and 9<=hitAng<=38)or(hitVel==170 and 9<=hitAng<=44)or(hitVel==171 and 7<=hitAng<=37)or(hitVel==172 and 12<=hitAng<=32)or(hitVel==173 and 8<=hitAng<=33)or(hitVel==174 and 10<=hitAng<=36)or(hitVel==175 and 12<=hitAng<=38)or(hitVel==176 and 11<=hitAng<=26)or(hitVel==177 and 24<=hitAng<=30)or(hitVel==178 and 10<=hitAng<=36)or(hitVel==179 and 17<=hitAng<=42)or(hitVel==181 and hitAng==14)
    if batterCode not in batterDict:
        batterDict[batterCode] = {
            'ab': 1,
            'b1': 0,
            'b2': 0,
            'b3': 0,
            'hr': 0,
            'h': 0,
            'ba': 0,
            'slg': 0,
            'wobacon': 0,
            'barrel': 0
        }
    if barrel:
        batterDict[batterCode]['barrel']+=1
    ab=b1=b2=b3=hr=h=0
    if hitResult not in ('????????????', '???????????????'):
        ab+=1
        batterDict[batterCode]['ab']+=1

    if hitResult in ('1??????', '????????????(1??????)', '????????????'):
        b1+=1
        batterDict[batterCode]['b1']+=1
    elif hitResult=='2??????':
        b2+=1
        batterDict[batterCode]['b2']+=1
    elif hitResult=='3??????':
        b3+=1
        batterDict[batterCode]['b3']+=1
    elif hitResult=='??????':
        hr+=1
        batterDict[batterCode]['hr']+=1

for eachBatterCode in batterDict:
    ab=b1=b2=b3=hr=h=0
    ab=int(batterDict[eachBatterCode]['ab'])
    b1=int(batterDict[eachBatterCode]['b1'])
    b2=int(batterDict[eachBatterCode]['b2'])
    b3=int(batterDict[eachBatterCode]['b3'])
    hr=int(batterDict[eachBatterCode]['hr'])

    h = b1+b2+b3+hr
    ba = h/ab
    slg = (b1+2*b2+3*b3+4*hr)/ab
    wobacon = (ba*0.6)+(slg*0.4)

    batterDict[eachBatterCode]['h']=h
    batterDict[eachBatterCode]['ba']=ba
    batterDict[eachBatterCode]['slg']=slg
    batterDict[eachBatterCode]['wobacon']=wobacon
#[0]GYEAR,[1]PCODE,[2]GAMENUM,[3]PA,[4]AB,[5]BA,[6]HIT,[7]HR,[8]TOTB,[9]SLG,[10]SF,[11]BB,[12]KK,[13]IB,[14]HP,[15]GD
newBatterDict = {}
for eachBatter in batterList[1:]:
    if eachBatter[1] not in newBatterDict:
        newBatterDict[eachBatter[1]] = [eachBatter[k] for k in range(16)]
    else:
        for l in range(2, 16):
            newBatterDict[eachBatter[1]][l]=float(newBatterDict[eachBatter[1]][l])+float(eachBatter[l])

openfilename = 'batterData_allHitResults.csv'
with open(openfilename, 'w', encoding='UTF8') as f:
    f.write('GYEAR,PCODE,GAMENUM,PA,AB,BA,HIT,HR,TOTB,SLG,SF,BB,KK,IB,HP,GD,ab,b1,b2,b3,hr,h,ba,slg,wobacon,brl\n')
    for eachBatter2 in newBatterDict:
        for data2 in newBatterDict[eachBatter2]:
            f.write(str(data2)+',')
        if eachBatter2 in batterDict:
            f.write(str(batterDict[eachBatter2]['ab'])+','+str(batterDict[eachBatter2]['b1'])+','+str(batterDict[eachBatter2]['b2'])+','+str(batterDict[eachBatter2]['b3'])+','+str(batterDict[eachBatter2]['hr'])+','+str(batterDict[eachBatter2]['h'])+','+str(batterDict[eachBatter2]['ba'])+','+str(batterDict[eachBatter2]['slg'])+','+str(batterDict[eachBatter2]['wobacon'])+','+str(batterDict[eachBatter2]['barrel'])+'\n')
        else:
            f.write('.,.,.,.,.,.,.,.,.,.\n')
            
#  ?????? ?????? ??????(??? 17??????)
#   1> 1??????
#   2> 2??????
#   3> 3??????
#   4> ????????????(1??????)
#   5> ????????????
#   6> ????????????
#   7> ????????????
#   8> ?????????
#   9> ????????????
#   10> ????????????
#   11> ??????????????????
#   12> ?????????
#   13> ???????????????
#   14> ?????????
#   15> ??????
#   16> ????????????
#   17> ???????????????