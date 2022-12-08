contacts = {
    "TEJESH":8317652279,"SOMA SEKHAR": 7981184515,"Yeshwanth":7995939179,"Chanukya":7569669189,"Venky":9063559343,"Darshan":7569827366,"Tharun":9948338123,
    "Shubham":9693964520,"Pradeep ":9177455989,"Prem ":6206407406,"Sumit ":9310083947,"Mohan ":8919889419,"Aabid Khan":7319661231,
    "Vinayak ":9177411877,"Lokeshwaran ":9345148191,"Piyush ":9997725596,"ABHI":6301190340,"SAHIL KHAN":6002634110,"SAAWAN":6207802116,
    "VIKRAM JHA":7742130488,"NISHANTH":7970922655,"HARSHA VARDHAN CHAUHAN":8791681219,"SHUBHAM AGRAWAL":8932951318,"ARYEN DEY":9365272613,
    "AJAY":9494818978,"VED":9798741907
}


# Searches the dictionary and prints the key value pair incase the key isn't present,it gives contact not found''

def single_search():
    name = input(">>>Enter the name of the contact you wish to search for: ").upper()
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        print("contact not found")


# Searches the dictionary and prints multiple key value pair and incase any key isn't present,it gives contact not found.

def multiple_search():
    result = {}
    name1 = input(">>>Enter the names of the contacts seperated by commas : ").split(",")
    for i in name1:
        i = i.upper()
        if i in contacts:
            result[i] = contacts[i]
            print(result)
        else:
            print("contact not found")




choice = int(input(
    "Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \n>>>Enter your choice: "))

if choice == 1:
    single_search()
elif choice == 2:
    for key, value in contacts.items():
        print(key,':',value)

elif choice == 3:
    multiple_search()

else:
    print("Choose from the given options!")
