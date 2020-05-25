t = (19,42,21)


#kata00 = "The " + str(len(t)) + " numbers are: "
#for i in t:
#   kata00 += str(i)
#   kata00 += ", "
#print(kata00[:-2])

print("The {} numbers are: {}".format(len(t), str(t)[1:][:-1]))
