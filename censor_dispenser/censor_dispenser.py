# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#censor functions
def censor_phrase(phrase, source):
    censored_email = source.replace(phrase, "**")
    censored_email = censored_email.replace(phrase.title(), "**")
    return censored_email

def censor_from_list(phrases, source):
    censored_email = source
    phrases.sort(key=len, reverse=True)
    for phrase in phrases:
        censored_email = censored_email.replace(phrase, "**")
        censored_email = censored_email.replace(phrase.title(), "**")
    return censored_email

#censor email one to remove learning algorithms
email_one_censored = censor_phrase("learning algorithms", email_one)
#censor email two to remove proprietary terms
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_two_censored = censor_from_list(proprietary_terms, email_two)

print(email_two_censored)
