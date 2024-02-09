from colorama import Fore, Style

input_text = Fore.RED+"╔═══"+Fore.CYAN+"["+Fore.GREEN+"Tanjim"+Fore.CYAN+"]"+Fore.RED+"══════"+Fore.CYAN+"["+Fore.GREEN+"HuntApi"+Fore.CYAN+"]"+"\n"+Fore.RED+"║"+"\n"+Fore.RED+"╚═══➣➣ "+Fore.GREEN

web_url = input(Fore.GREEN+f'\n\nEnter your target Web URL(with "http or https"):\n{input_text}')

while len(web_url) < 1:
    web_url = input(Fore.RED+f'\nEnter a valid Web URL(with "http or https"):\n{input_text}')



