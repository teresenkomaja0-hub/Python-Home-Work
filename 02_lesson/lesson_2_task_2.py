def is_year_leap(year):
    return "True" if year%4==0 else "Fals"
x=int(input("Год:"))
y=is_year_leap(x)
print(f"ГОД:{x}<{y}>")


