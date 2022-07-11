import pywhatkit

def reminder(message, hour, minute):
    pywhatkit.sendwhatmsg('+905322807393', str(message), int(hour), int(minute))

reminder(input('Type the note you want to be reminded'), input('Type the hour you want to be reminded'), input('Type the minute you want to be reminded'))



