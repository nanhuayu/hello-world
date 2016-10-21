test = []
def getline(money):
    try:
        money.append(float(raw_input()))
        return True
    except EOFError:
        return False

for i in range(12):
    getline(test)
    #print test

print "$%.2f" % round((sum(test) + 0.001) / 12 ,2)