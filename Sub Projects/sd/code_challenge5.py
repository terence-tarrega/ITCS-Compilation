#ph_denomination_TARREGA.py
name = input("Enter your name here ---> ")
deposit = eval(input("Enter amount to deposit:"))

thousand = deposit // 1000
fiveh = deposit - (thousand * 1000)
fh = fiveh // 500
twoh = fiveh - (fh * 500)
th = twoh // 200
oneh = twoh - (th * 200)
oh = oneh // 100
fifty = oneh - (oh * 100)
ff = fifty // 50
twenty = fifty - (ff * 50)
tw = twenty // 20
ten = twenty - (tw * 20)
t = ten // 10
five = ten - (t * 10)
f = five // 5
one = five - (f * 5)
o = one // 1 
print ("The denomination of your deposit is:")
print (thousand,"- 1000")
print (fh,"- 500")
print (th,"- 200")
print (oh,"- 100")
print (ff,"- 50")
print (tw,"- 20")
print (t,"- 10")
print (f,"- 5")
print (o,"- 1")
