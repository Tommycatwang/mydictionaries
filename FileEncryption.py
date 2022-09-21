write1=open('encrypted.txt','w')
read=open('info_security.txt','r')
codes={'A':'%','a':'9','B':'@','b':'#','C':'!','c':'$','D':'^','d':'6'}
codes = {'E':'1','e':'&','F':'2','f':'8', 'G':'*','g':'7','H':';','h':'0','I':'3'}
codes={'i':'4','J':':','j':'[','K':'5','k':'-','L':'_','l':'|','M':'`','m':'~'}
codes={'O':'=','o':'+','P':'<','p':',', 'Q':'.','q':'>','R':'?','r':'/','S':']'}
codes={'T':'{','t':'}','U':'=-','u':')(','V':'!@!','v':'$%%$','W':'**&*','w':'}{'}
codes={'X':'+:>','x':'0235','Y':'2352','y':'?:?','Z':'::>','z':'"})9'}

sentence=''
read=read.readline()
for w in read:
    if w in codes.keys():
        sentence+=codes[w]
    else:
        sentence+=w

write1.write("Encrypted text: "+sentence)