import string


def check_password(password):
    score = 0

    if len(password)>=8:
        sccore+=1

    if any(c.isupper() for c in password):
        score+=1

    if any(c.islower() for c in password):
        acore +=1

    if any(c.isdigit() for c in password):
        score +=1

    if any(c in string.punctuation for c in password):
        score +=1
    return score
