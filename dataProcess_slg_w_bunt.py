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
hitList = [[] for _ in range(120746)]
count = 0
i = 0
with open(filename,'r', encoding='UTF8') as data:
   for line in csv.reader(data):
       hitList[i]=line
       i+=1

def roundUp(num):
    if num>=0:
        return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)
    else:
        return int(num) if (num-int(num)) >= -0.5 else int(num)-1

hit_by_vel_vs_ang = [[[] for _ in range(NUM_VEL)] for _ in range(NUM_ANG)]

for eachHit in hitList[1:]:
    hitVel = roundUp(float(eachHit[6]))
    hitAng = roundUp(float(eachHit[7]))
    pitId = eachHit[2]
    pCode = eachHit[3]
    hitResult = eachHit[8]
    hit_by_vel_vs_ang[hitAng+69][hitVel-10].append((pitId, pCode, hitResult))

for hitListByAng in hit_by_vel_vs_ang:
    for hitListByVel_inCertainAng in hitListByAng:
        # 해당 각도와 속도에 해당하는 타구 기록이 없는 경우 스킵해주어야함.
        if not hitListByVel_inCertainAng:
            continue
        ab=b1=b2=b3=hr=0
        for eachHit2 in hitListByVel_inCertainAng:
            hitResult2 = eachHit2[2]
            if hitResult2 not in ('희생번트', '희생플라이'):
                ab+=1
            if hitResult2 in ('1루타', '내야안타(1루타)', '번트안타'):
                b1+=1
            elif hitResult2=='2루타':
                b2+=1
            elif hitResult2=='3루타':
                b3+=1
            elif hitResult2=='홈런':
                hr+=1
        # 모든 타구 기록이 타수로 인정되지 않는 경우 (즉 희생번트/희생플라이만 있는 경우)
        if ab==0:
            hitListByVel_inCertainAng.append('.')
            continue
        slg = (b1+2*b2+3*b3+4*hr)/ab
        hitListByVel_inCertainAng.append(slg)

# hitResult 번트안타를 1루타에 포함시켜야 하나?
# slg = (b1+2*b2+3*b3+4*hr)/ab

#save as csv
openfilename = 'slg_by_vel_vs_ang.csv'
with open(openfilename, 'w', encoding='UTF8') as f:
    f.write('.,')
    for k in range(NUM_VEL):
        f.write(str(k+10)+',')
    f.write('\n')
    for i in range(NUM_ANG):
        angY = i-69
        f.write(str(angY)+',')
        for j in range(NUM_VEL):
            if hit_by_vel_vs_ang[i][j]:
                f.write(str(hit_by_vel_vs_ang[i][j][-1])+',')
            else:
                f.write('.,')
        f.write('\n')

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