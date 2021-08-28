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
    barrel=False
    if hitVel>=149 and 7<=hitAng<=46 :
        barrel = (hitVel==149 and 26<=hitAng<=27)or(hitVel==150 and 26<=hitAng<=34)or(hitVel==151 and 24<=hitAng<=34)or(hitVel==152 and 22<=hitAng<=34)or(hitVel==153 and 22<=hitAng<=33)or(154<=hitVel<=155 and 22<=hitAng<=35)or(156<=hitVel<=157 and 21<=hitAng<=36)or(hitVel==158 and 21<=hitAng<=37)or(hitVel==159 and 19<=hitAng<=38)or(160<=hitVel<=161 and 20<=hitAng<=38)or(162<=hitVel<=163 and 19<=hitAng<=42)or(hitVel==164 and 18<=hitAng<=42)or(hitVel==165 and 19<=hitAng<=46)or(166<=hitVel<=167 and 18<=hitAng<=41)or(hitVel==168 and 8<=hitAng<=42)or(hitVel==169 and 9<=hitAng<=38)or(hitVel==170 and 9<=hitAng<=44)or(hitVel==171 and 7<=hitAng<=37)or(hitVel==172 and 12<=hitAng<=32)or(hitVel==173 and 8<=hitAng<=33)or(hitVel==174 and 10<=hitAng<=36)or(hitVel==175 and 12<=hitAng<=38)or(hitVel==176 and 11<=hitAng<=26)or(hitVel==177 and 24<=hitAng<=30)or(hitVel==178 and 10<=hitAng<=36)or(hitVel==179 and 17<=hitAng<=42)or(hitVel==181 and hitAng==14)
    if batterCode in batterDict:
        batterDict[batterCode]['ab']+=1
    else:
        batterDict[batterCode] = {
            'ab': 1,
            'barrel': 0
        }
    if barrel:
        batterDict[batterCode]['barrel']+=1
#[0]GYEAR,[1]PCODE,[2]GAMENUM,[3]PA,[4]AB,[5]BA,[6]HIT,[7]HR,[8]TOTB,[9]SLG,[10]SF,[11]BB,[12]KK,[13]IB,[14]HP,[15]GD
newBatterDict = {}
for eachBatter in batterList[1:]:
    if eachBatter[1] not in newBatterDict:
        newBatterDict[eachBatter[1]] = [eachBatter[k] for k in range(16)]
    else:
        for l in range(2, 16):
            newBatterDict[eachBatter[1]][l]=float(newBatterDict[eachBatter[1]][l])+float(eachBatter[l])

openfilename = 'batterData_w_barrels.csv'
with open(openfilename, 'w', encoding='UTF8') as f:
    f.write('GYEAR,PCODE,GAMENUM,PA,AB,BA,HIT,HR,TOTB,SLG,SF,BB,KK,IB,HP,GD,AB_ME,BRL\n')
    for eachBatter2 in newBatterDict:
        for data2 in newBatterDict[eachBatter2]:
            f.write(str(data2)+',')
        if eachBatter2 in batterDict:
            f.write(str(batterDict[eachBatter2]['ab'])+','+str(batterDict[eachBatter2]['barrel'])+'\n')
        else:
            f.write('.,.\n')
            
#  타격 결과 항목(총 17가지)
#   1> 1루타
#   2> 2루타
#   3> 3루타
#   4> 내야안타(1루타)
#   5> 땅볼아웃
#   6> 번트아웃
#   7> 번트안타
#   8> 병살타
#   9> 삼중살타
#   10> 야수선택
#   11> 인필드플라이
#   12> 직선타
#   13> 파울플라이
#   14> 플라이
#   15> 홈런
#   16> 희생번트
#   17> 희생플라이