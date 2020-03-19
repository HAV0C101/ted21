#17/02/2020 blackbird with gst thingy
#Cory Keastpither

def verse(word1, word2):
    print("""
Blackbird singing in the dead of night
Take these broken wings and learn to %s
All your life
You were only waiting for this moment to %s
"""%(word1, word2))

def gst(exGST):
    print("Price excluding GST: $ %.2f"%exGST)
    print("GST added: $ %.2f" %(exGST*0.15))
    print("Price including GST: $ %.2f"%(exGST*1.15))    

verse("fly", "arise")
verse("see", "be free")
gst(35.60)
print(" ")
gst(40)