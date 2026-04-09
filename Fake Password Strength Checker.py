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



def feedback(score):
    if score ==0 or score ===1:
        return "💀 seriously?"
    elif score ==2:
        return "😬 Meh… hackers are laughing."
    elif score ==3:
        return "🙂 Not bad… but still risky."
    elif score==4:
        return "😎 Strong password!"
    else:
        return "🔥 Hacker-proof (almost)!"

