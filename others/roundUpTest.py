def roundUp(num):
    if num>=0:
        return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)
    else:
        return int(num) if (num-int(num)) >= -0.5 else int(num)-1

print(roundUp(float(-68.9)))
print(roundUp(float(89.8)))
print(roundUp(float(-7.4)))
print(roundUp(float(-7.6)))


# neg = -2
# print(-22-neg)