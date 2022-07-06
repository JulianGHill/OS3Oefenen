# De opdracht geeft jou een textfile met dhcp log
# jij moet elke line in de log aggrafreren en het aantal specifieke soorten dhcp acties bijhouden en in een overzicht uitprinten
# de input is een mac adress en deze mac address moet in de regel staan
# File wordt geopend
file1 = open('note.txt', 'r')
count = 0

CountDHCPDISCOVER = 0
CountDHCPOFFER = 0
CountDHCPREQUEST = 0
CountDHCPACK = 0
CountDHCPNACK = 0

#inputMac = input("Put in the mac address : ")
inputMac = "00:11:22:33:44:55"

# for loop waarin wordt gekeken hoeveel x een specifieke DHCP form in de regel komt
# als dit in de line zit wordt het aan de counter toegevoegd
for line in file1:
    if inputMac in line and "DHCPOFFER" in line:
        CountDHCPOFFER += 1
    if inputMac in line and "DHCPDISCOVER" in line:
        CountDHCPDISCOVER += 1
    if inputMac in line and "DHCPREQUEST" in line:
        CountDHCPREQUEST += 1
    if inputMac in line and "DHCPNACK" in line:
        CountDHCPNACK += 1
    if inputMac in line and "DHCPACK" in line:
        CountDHCPACK += 1

file1.close()

# ik open opniuew de text file om de eerste en de laaste regel in 2 vars te zetten
with open("note.txt", "r") as fp:
    lines = fp.readlines()
    first = lines[0].split('/n')[0]
    end = lines[-1].split('/n')[0]
# ik split de vars en verwijder alles na de datum
sep = '    '
first = first.split(sep, 1)[0]
end = end.split(sep, 1)[0]

fp.close()
print("------------------------")
print("Start:   ", first)
print("End:     ", end)
print("------------------------")
print("MAC:", inputMac)
print("------------------------")
print("DHCPDISCOVER : ", CountDHCPDISCOVER, 'x')
print("DHCPOFFER : ", CountDHCPOFFER, 'x')
print("DHCPREQUEST : ", CountDHCPREQUEST, 'x')
print("DHCPACK : ", CountDHCPACK, 'x')
print("DHCPNACK : ", CountDHCPNACK, 'x')
print("------------------------")
