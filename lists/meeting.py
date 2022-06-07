attendees = ["Ken","Ayah","Oraby","Hammad"]
attendees.append("Karim")
attendees.extend(["Amr","Basmallah"])
optional_invitees = ["Gamal","Hoda"]
potentional_attendees = attendees + optional_invitees
print("There are ", len(potentional_attendees), "potentional attendees currenty")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)