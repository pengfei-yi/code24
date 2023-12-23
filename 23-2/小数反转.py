def func():
    s = input()
    if "." in s:
        a,b = s.split(".")
    else:
        a = s
        b = "0"
    print(float(f"{a[::-1]}.{int(b[::-1])}"))
func()