str="Some RanDomTExt so eeeee"
print(str)
print(str.center(0,"*"))
print(str.format())
print(str.encode())
print(str.expandtabs(2))
gmail="sam@gmail.com"
a=gmail.find('@')
d=str.find('.')
print(gmail[0:a])
print(gmail[a+1:d])
print(ord('A'))
for ch in range(ord('A'),ord('Z')+1):
    print(chr(ch))

inp=input("enter your name")
mail=inp.strip()
mail=mail+"@gmail.com"
print(mail.lower())