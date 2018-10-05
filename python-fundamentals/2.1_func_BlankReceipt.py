def PrintHeader():
    print("CASH RECEIPT")
    print("------------------------------")

def PrintBody():
    print("Charged to____________________")
    print("Received by___________________")

def PrintFooter():
    print("------------------------------")
    print("\u00A9" + " SoftUni")

def PrintAll():
    PrintHeader()
    PrintBody()
    PrintFooter()

PrintAll()
