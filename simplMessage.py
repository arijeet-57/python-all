text = "how are you?"
text = "I am fine"
print(text)

#name = "brad pitt"
#print(name.title())

#below is the example of string concatenation
first_name = "brad"
last_name = "pitt"
full_name = first_name + " " + last_name

print(full_name.title())

#personal message
name = "henry"
print("How are you shittin today " + name.title() + " ?")

print(name.upper())
print(name.lower())
print(name.title())

famous_person = "richard feynman"
quote = ( famous_person.title() + ' once said, "Learn in the most \nundisciplined manner possible"')
print(quote)



stripper_payload = '" \t\nuser name "'
print(stripper_payload)
print(stripper_payload.lstrip())
print(stripper_payload.rstrip())
print(stripper_payload.strip())