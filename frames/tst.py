
kd = {"ALFA":"a",
      "BETA":"b",
      "GAMMA":"g"
        }


string = input("Inserte texto a formatear:  ")

lst = string.split("{")


words, tokens = [],[]

formatted = ""

for i in lst:
    if "}" in i:
        key = i.split("}")[0]
        if key in kd.keys(): 
            formatted += f"{kd[key]}"
        else:
            formatted += f"{{{i}"
    else:
        formatted += i

print(f"\n\n\t{formatted}")

