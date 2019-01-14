import operator

wordfreq = {
"a" : 0.0730,
"b" : 0.0168,
"c" : 0.0187,
"d" : 0.0381,
"e" : 0.1261,
"f" : 0.0226,
"g" : 0.0155,
"h" : 0.0459,
"i" : 0.0640,
"j" : 0.0039,
"k" : 0.0110,
"l" : 0.0381,
"m" : 0.0259,
"n" : 0.0743,
"o" : 0.0911,
"p" : 0.0207,
"q" : 0.0006,
"r" : 0.0621,
"s" : 0.0633,
"t" : 0.0827,
"u" : 0.0336,
"v" : 0.0116,
"w" : 0.0297,
"x" : 0.0006,
"y" : 0.0284,
"z" : 0.0013
}

cipher = open('q3cipher.txt','r')
ctxt = cipher.read()
#print ctxt
cipher.close()

temp1 = ctxt.replace(" ", "")
temp2 = temp1.replace(".", "")
combtxt  = temp2.replace(",", "")

ctxtlist = []
cl = []
for i in range(len(combtxt)):
    ctxtlist.append(combtxt[i])

for i in range(len(ctxtlist)):
    if (ctxtlist[i] == '\n' or ctxtlist[i] == '\r'):
        continue
    else:
        cl.append(ctxtlist[i])
#print (sorted(cl))
cl = sorted(cl)

num = len(cl)
alpha = wordfreq.keys()

cipfreq = {}

for i in range(len(alpha)):
    sum = 0
    for j in range(len(cl)):
        if cl[j] == alpha [i]:
            sum+=1.0
    cipfreq[alpha[i]] = round(sum/num, 4)

#print cipfreq
sorted_cip = sorted(cipfreq.items(), key=operator.itemgetter(1))
sorted_alpha = sorted(wordfreq.items(), key=operator.itemgetter(1))

#print sorted_cip
#print sorted_alpha

match = {}
replace = {}
for i in range(len(sorted_cip)):
    match[sorted_alpha[i][0]] = sorted_cip[i][0]
    replace[sorted_cip[i][0]] = sorted_alpha[i][0]

sorted_match = sorted(match.items(), key=operator.itemgetter(0))
sorted_replace = sorted(replace.items(), key=operator.itemgetter(0))

#print sorted_match

plntxt = ""
for i in ctxt:
    if i.isalpha() == True:
        plntxt = plntxt + replace[i]
    else:
        plntxt = plntxt + i

print plntxt
