def read_contact():
    '''
    Reads contact information of user needed to send notifications

    Returns
    --------
    number (str) : phone number that will receive text notification
    provider (str) : service provider for user phone number
    email (str) : email address through which notification will be sent
    '''
    
    with open('contact_info.txt', 'r') as contact:
        number = ""
        provider = ""
        email = ""
        current_contact = contact.readlines()
        if len(current_contact) > 0:
            number = current_contact[0]
            provider = current_contact[1]
            email = current_contact[2]
        contact.close()
    
    number = number[:-1]
    provider = provider[:-1]
    contactInfo = [number, provider, email]
    return contactInfo