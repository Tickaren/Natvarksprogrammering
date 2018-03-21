import re
f = open("tabla.html", encoding="utf-8")
txt = f.read()
f.close()

regg =re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*<div.*?>\s*.*\s*.*\s*<p.*?>\s*(\w+.*)\s*</p>', txt)
#regg = regg.split("')")
for i in regg:
    print("----------------------------")
    print("Tid:      ", ''.join(re.findall(r'\s*(\d+\.\d+)\s*', str(i))))
    print("Säsong:   ", ''.join(re.findall(r'Säsong\s*(\d+)', str(i))))

    avsnittnr = ''.join(re.findall(r'Del\s*(\d+)', str(i)))
    avsnitttotal = ''.join(re.findall(r'av\s*(\d+)', str(i)))
    print("Avsnitt:  ", avsnittnr, "/", avsnitttotal)

    print("Handling: ",''.join(re.findall(r"av\s*\d+\.\s*(\w+.*)\s*'", str(i))))
