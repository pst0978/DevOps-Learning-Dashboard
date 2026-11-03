import os 
def check_company_lock():
    print("Checking if tradding compNY is controlling this mac")
    print("----------------")

    command = "profiles status -type enrollment"
    result = os.popen(command).read().strip()

    print("System Report")
    print("result")
    print("------------")
    if "Enrolled: Yes" in result or "MDM: Yes" in result:
        print("Alert: This Mac is managed by the company's remote server!")
    else:
        print("success: this mac is yours. No company lock found.")    

check_company_lock()        
              