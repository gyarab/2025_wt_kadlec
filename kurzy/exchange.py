import httpx

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

print("server odpovedel:", res.status_code)
lines = res.text.split('\n')
print("Kruzy pro den:", lines[0].split(" ")[0])

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

rate_str = line_euro.split('|')[-1].replace(',' , '.')
rate = float(rate_str)

print("Kurz eura je", rate)
druh_prevodu = input("Chces prevadet z eur na koruny (1) nebo z korun na eura (2)?")
if druh_prevodu == "1":
    try:
        value_in = float(input("Kolik mas eur? ").replace(',', '.'))
        value_out = value_in * rate
        print(f"Tak to je {value_out:.2f} korun.")
    except ValueError:
        print("Mel jsi napsat cislo")

elif druh_prevodu == "2":
    try:
        value_in = float(input("Kolik mas korun? "))
        value_out = value_in / rate
        print(f"Tak to je {value_out:.2f} eur.")
    except ValueError:
        print("Mel jsi napsat cislo")
else:
    print("mel jsi napsat 1 nebo 2!")
