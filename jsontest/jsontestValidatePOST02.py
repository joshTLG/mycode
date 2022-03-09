import requests


# PART A - pull timestamps
TIMEURL = "http://date.jsontest.com"

# PART B - Pull IP address
IPURL = "http://ip.jsontest.com"

# PART C - Read in a list of servers from myservers.txt

# PART D - Format the data in {"json": "time: <<PART A>>, ip: <<PART B>>, mysvers: [ <<PART C>> ]"}

# PART E - Validate
VALIDURL = "http://validate.jsontest.com"

def main():
    resp = requests.get(TIMEURL)
    mytime = resp.json()
    mytime = mytime["time"].replace(" ", "").replace(":","-")

    resp = requests.get(IPURL)
    myip = resp.json()
    print(myip)
    myip = myip["ip"]

    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()


    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    resp = requests.post(VALIDURL, data=mydata)

    respjson = resp.json()

    print(respjson)

    print(f"JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
