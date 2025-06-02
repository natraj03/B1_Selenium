from stringfunction import outputstr

#

inpVar="news1234"
outputstr=""
for index in range (0,len(inpVar)):
    temp =inpVar[index]
    outputstr=temp+outputstr
    print("limit",outputstr)
