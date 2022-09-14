acronyms = {
    'LOL': 'laugh out loud',
    'IDK': 'i dont know',
    'TBH': 'to be honest'
}

# to print the value in a dictionary, we pass in the key
print(acronyms['LOL'])

# output: laugh out loud

# add items to the dictionary
acronyms['IKR'] = "i know right?"
print(acronyms)

# delete value
del acronyms['LOL']
print(acronyms)

# get a key that might not be there (and avoid an error)

definition = acronyms.get('BTW')
print(definition)

# ^ output: None