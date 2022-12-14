def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

def binaryDiv(genlen, msg, gen):
    pick = genlen
    tmp = msg[0:pick]

    while pick < len(msg):
        if tmp[0] == "1":
            tmp = xor(gen, tmp) + msg[pick]
        else:
            tmp = xor('0'*pick, tmp) + msg[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(gen, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

# Main
message = input("Enter polynomial:")

crcGenerator = "10001000000100001"
# crcGenerator = "1011"
print("CRC Generator:", crcGenerator)

crcGenLength = len(crcGenerator)
# zero=["0" for i in range(0,crcGenLength)]
# zero=''.join(zero)
# modMessage = message+zero
modMessage = str(int(message) * (10**(crcGenLength-1)))
print("Modified polynomial:", modMessage)

# rem = int(modMessage) / int(crcGenerator)
rem = binaryDiv(crcGenLength, modMessage, crcGenerator)
print("Remainder:", rem)

# generate codeword using remainder
codeword = str(int(modMessage) + int(rem))
print("Code Word:", codeword)

ch = int(input("Test error detection? 1:yes, 0:no :"))
if ch == 1:
    pos = int(input("Enter position to insert error:"))

    codeword = list(codeword)
    if codeword[pos+1] == '1':
        codeword[pos+1] = '0'
    else:
        codeword[pos+1] = '1'

    codeword = ''.join(codeword)

    print("Errorneous codeword:", codeword)

    # test = codeword / crcgenerator
    test = binaryDiv(crcGenLength, codeword, crcGenerator)
    print("CodeWord / CRCGenerator:", test)

    # if test = 0 => no error
    if int(test) == 0:
        print("No Error")
    else:
        print("Error Detected")

else:
    print("Skipping error insertion")
