yoil = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

m, d = map(int,input().split())

splitday = sum(day[:m])+d
print(yoil[splitday%7])
