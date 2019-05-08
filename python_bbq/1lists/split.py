email = "max.mustermann@yahoo.de"
name = [i for i in email.split(".")]
second_name_list = name[1].split("@")
print("First name:", name[0].capitalize())
print("Second name:", second_name_list[0].capitalize())
print("Domain name:", second_name_list[1].capitalize())
