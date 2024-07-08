def main():
    options = [1, 2]
    encodeOrDecode = ""
    
    while True:
        encodeOrDecode = input("Do you want to encode(1) a message or decode(2) a message?")
        if encodeOrDecode not in options:
            print("Please enter a valid option")
            continue
        break
    
    if encodeOrDecode == "1":
        encode()
    elif encodeOrDecode == "2":
        decode()
    else:
        print("How did we get here, just incase, this is if an invalid input makes it past the check")
        
def encode():
    msg = input("Please enter the message you want to be encoded")
    repeated = []
    newMsg = []
    
        
    
def decode():
    print("placeholder")
    
main()