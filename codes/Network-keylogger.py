import os,sys
leftover = os.popen(f"tshark -r {sys.argv[1]} -Y \"usb.capdata\" -T fields -e \"usb.capdata\"").readlines()

usb_codes = {
    "04":['a','A'],"05":['b','B'], "06":['c','C'], "07":['d','D'], "08":['e','E'], "09":['f','F'],"0A":['g','G'],"0B":['h','H'], "0C":['i','I'], "0D":['j','J'], "0E":['k','K'], "0F":['l','L'],"10":['m','M'], "11":['n','N'], "12":['o','O'], "13":['p','P'], "14":['q','Q'], "15":['r','R'],"16":['s','S'], "17":['t','T'], "18":['u','U'], "19":['v','V'], "1A":['w','W'], "1B":['x','X'],"1C":['y','Y'], "1D":['z','Z'], "1E":['1','!'], "1F":['2','@'], "20":['3','#'], "21":['4','$'],"22":['5','%'], "23":['6','^'], "24":['7','&'], "25":['8','*'], "26":['9','('], "27":['0',')'],"28":['\n','\n'], "29":['[Esc]','[Esc]'], "2A":['{backspace}','{backspace}'], "2B":['\t','\t'],"2C":[' ',' '], "2D":['-','_'], "2E":['=','+'], "2F":['[','{'], "30":[']','}'], "31":['\',"|'],"32":['#','~'], "33":";:", "34":"'\"", "36":",<",  "37":".>", "38":"/?","39":['[CAPSLOCK]','[CAPSLOCK]'], "3A":['F1'], "3B":['F2'], "3C":['F3'], "3D":['F4'], "3E":['F5'], "3F":['F6'], "41":['F7'], "42":['F8'], "43":['F9'], "44":['F10'], "45":['F11'],"46":['F12'], "4F":[u'→',u'→'], "50":[u'←',u'←'], "51":[u'↓',u'↓'], "52":[u'↑',u'↑']
   }

for index in range(len(leftover)):
    try:
        if leftover[index][:2].upper() == '20' or leftover[index][:2].upper() == '02':
            print(usb_codes.get(leftover[index][4:6].upper())[1],end='')
        else:
            print(usb_codes.get(leftover[index][4:6].upper())[0],end='')
    except:
        continue

#Usage :: python3 Network-keylogger.py <pcapfile>
