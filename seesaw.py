#180220 see saw
#Cory Keastpither

#define functions
def  getDistances(userWeight):
    return (46*200)/userWeight
#main routine
print("For a 75kg person: %f cm" %getDistances(75))
print("For a 60kg person: %f cm" %getDistances(60))
print("For a 100kg person: %d cm" %getDistances(100))