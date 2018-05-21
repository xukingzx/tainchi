pred =  [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
truePositive = falsePositive = trueNegative = falseNegative = 0
for i in range(len(pred)):
    if(pred[i] == 1 and labels[i] == 1):
        truePositive = truePositive + 1
    elif(pred[i] == 1 and labels[i] == 0):
        falsePositive = falsePositive + 1
    elif(pred[i] == 0 and labels[i] == 1):
        falseNegative = falseNegative + 1
    else:
        trueNegative = trueNegative + 1

print('truePositive is:' + str(truePositive))
print('falsePositive is:' + str(falsePositive))
print('trueNegative is:' + str(trueNegative))
print('falseNegative is:' + str(falseNegative))

print(truePositive / (truePositive + falsePositive))
print(truePositive / (truePositive + falseNegative))