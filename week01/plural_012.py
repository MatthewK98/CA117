import sys
line = sys.stdin
for a in line:
  a = a.strip()
  if a[-2:] in ("ch","sh"):
    print(a + "es")
  elif a[-1] in ("x", "s","z"):
    print(a + "es")
  elif a[-2] not in ("a","e","i","o","u") and a[-1] in "y":
    print(a.replace("y","ies"))
  elif a[-1] in "f":
    print(a.replace("f","ves"))
  elif a[-2] in "fe":
    print(a.replace("fe","ves"))
  elif a[-1] in "o":
    print(a + "es")
  else:
    print(a + "s")