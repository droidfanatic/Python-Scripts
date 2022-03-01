hours = 0
minutes = 0
h = 0
m = 0
lTime = []
isDay = False

file = open("mytime.txt", "r")
for line in file:
  split = line.split(" ")
  fSplit = split[1].split(":")
  sSplit = split[4].split(":")
  
  h += int(sSplit[0]) - int(fSplit[0])
  if int(sSplit[1]) < int(fSplit[1]):
    h -= 1
    m += (int(sSplit[1]) + 60) - int(fSplit[1])
  else:
    m += int(sSplit[1]) - int(fSplit[1])

  if isDay:
    while m >= 60:
      h += 1
      m -= 60

    hours += h
    minutes += m
    lTime.append([h,m])

    h = 0
    m = 0
  isDay = not isDay

for day in lTime:
  print(day)

while minutes >= 60:
      hours += 1
      minutes -= 60
print(hours,"hrs ",minutes, "mins")

remHours = 39 - hours
remMinutes = 60 - minutes

print(remHours,"hrs ",remMinutes, "mins")
