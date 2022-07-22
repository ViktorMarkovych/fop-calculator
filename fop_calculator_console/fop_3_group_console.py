quarter = int(input('What quarter '))
rate = int(input('What rate '))
suma = int(input('What is the amount per quarter '))
if quarter == 4:
    esv = 4422.0
else:
    esv = 4290.0
ep = (suma / 100 * rate)
print("EP =",ep, "UAN")
print("ESV =",esv, "UAN")
