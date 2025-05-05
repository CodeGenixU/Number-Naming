def name(n):
    n = int(n)
    naam = '' 
    d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if len(str(n))<=2:
        if n in d:
            naam = d[n]
        elif n == 0 :
            naam = 'zero'
        else :
            naam = d[int(str(n)[-2])*10] + ' ' + d[int(str(n)[-1])]

    if len(str(n)) == 3:
        naam = d[int(str(n)[0])] + " hundred "
        if int(str(n)[1:4]) != 0 :
               naam += name(int(str(n)[1:4]))
        
    return naam.title()
#-------------------------------------------------------------------------------------------------------------------------
def Namer(n,s = "n"):
    d = {"i":({0:" thousand ",1:" million "},3),
         "n":({0:" thousand ",1:" lakh ",2:" crore "},2)}
    sys,o = d[s]
    num = str(n)
    naam = ''
    st,sp = -1,-(o+1)
    if len(num) >= 4:
        if (len(num)-3)%o != 0:
            num = "0"*(o-((len(num)-3)%o)) + num[0:len(num)-3]
        else :
            num = num[0:len(num)-3]
        for i in range(len(num)//o) :
            im = int((num[st:sp:-1])[::-1])
            if im != 0:
                naam = name(im) + sys[i] + naam
            st,sp = sp,sp-o
        if int((str(n)[-1:-4:-1])[::-1]) != 0 :
            naam += name(int((str(n)[-1:-4:-1])[::-1]))
    else :
        naam = name(n)
    return naam.title()

print("Welcome to number namer")
print("Before proceding further I want to inform you that this can only name numbers upto 999999999")
while True:
    print("For International system, enter 1.")
    print("For Indian system, enter 2.")
    print("Enter any other character to close the program.")
    try :
        x = int(input("Enter system : "))
        while True:
            n = input("Enter Number : ")
            if n.isdigit() :
                if x == 2: print(Namer(n))
                elif x == 1: print(Namer(n, s = "i"))
            else:
                if n.lower() == "exit":
                    break
                else:
                    print("Not a valid input.")
    except Exception :
        break