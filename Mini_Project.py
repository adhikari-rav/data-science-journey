import csv
result = 'TBD'
Datas = [
    ["Username", "Attempts" , "Status"],
    ["Ram_88", "8" , "Success" ],
    ["Roger_one", "5" , "Failed" ],
    ["Here_me", "2" , "Failed" ],
    ["User", "20" , "Success" ],
    ["User_01", "20" , "Failed" ],
    ["User_02", "5" , "Success" ]
    ]

with open ("Data_log.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(Datas)

def security_Report(entry):
    print ("==== Security Report =====")
    for entries in entry:
        Status = entries['Status']
        Attempts = int(entries['Attempts'])
        if Status == "Success":
            result = "CLEAR"
        elif Status == "Failed" and Attempts <5:
            result = "MONITOR"
        else:
            result = "SUSPICIOUS"

        print(f"Name: {entries['Username']}")
        print(f"Attempts: {entries['Attempts']}")
        print(f"Status: {entries['Status']}")
        print(f"Flag: {result}")
        print("---")
    print("==== End of Report ====")

with open ("Data_log.csv", "r") as file:
    reader = csv.DictReader(file)
    security_Report(reader)
