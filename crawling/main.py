from colorama import Fore, Style

def input_text(text=None):
    if text is None:
        text_ = Fore.RED+"╔═══"+Fore.CYAN+"["+Fore.GREEN+"Tanjim"+Fore.CYAN+"]"+Fore.RED+"══════"+Fore.CYAN+"["+Fore.GREEN+"HuntApi"+Fore.CYAN+"]"+"\n"+Fore.RED+"║"+"\n"+Fore.RED+"╚═══➣➣ "+Fore.GREEN
    else:
        text_ = Fore.RED+"╔═══"+Fore.CYAN+"["+Fore.GREEN+text+Fore.CYAN+"]"+"\n"+Fore.RED+"║"+"\n"+Fore.RED+"╚═══➣➣ "+Fore.GREEN
    return text_

web_url = input(input_text("Enter your target Web URL(with 'http or https')"))

while len(web_url) < 1:
    web_url = input(input_text(Fore.RED+f'Enter a valid Web URL(with "http or https")'))
