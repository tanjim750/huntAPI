from colorama import Fore, Style
import os
import re
import time
import csv

from validate_url import Request

DEFAULT_WORDLIST = './default_wordlist'
CUSTOM_WORDLIST = './custom_wordlist'
RESULT_PATH = './results'

def extract_domain(url):
    match = re.search(r'https?://(?:www\.)?([a-zA-Z0-9.-]+)', url)
    return match.group(1) if match else None

def get_wordlists(folder_path):
    files = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(foldername, filename))
    return files

def input_text(text=None,color=None):
    if text is None:
        text_ = Fore.RED+"\n╔═══"+Fore.CYAN+"["+Fore.GREEN+"Tanjim"+Fore.CYAN+"]"+Fore.RED+"══════"+Fore.CYAN+"["+Fore.GREEN+"HuntApi"+Fore.CYAN+"]"+"\n"+Fore.RED+"║"+"\n"+Fore.RED+"╚═══➣➣ "+Fore.GREEN
    else:
        text_ = Fore.RED+"\n╔═══"+Fore.CYAN+"["+color+text+Fore.CYAN+"]"+"\n"+Fore.RED+"║"+"\n"+Fore.RED+"╚═══➣➣ "+Fore.GREEN
    return text_

def validate(url,file_path):
    listOfWords = []
    url = url if url.endswith('/') else url+'/'
    
    with open(file_path, 'rb') as f:
        try:
            words = f.read().decode('utf-8')
            words = words.split()
            listOfWords.extend(word for word in words if word not in listOfWords)
        except UnicodeDecodeError:
            print(Fore.RED+f"\nError decoding file: {file_path}. Try with another wordlist")

    print( Fore.LIGHTBLUE_EX+
           "\n\n       ======================================================================\n"+
           Fore.GREEN+"       URL           Response           End-Point           Accepted-Requests\n"+
           Fore.LIGHTBLUE_EX+"       ======================================================================\n" )
    
    success_urls = []

    start_time = time.time()

    for word in listOfWords:
        acceptedRequests = []
        url_=url+word
        request = Request(url=url_)

        # requests and responses
        get = request.Get()
        post = request.Post()
        patch = request.Patch()
        put = request.Put()
        delete = request.Delete()

        if get == "error" or post == "error" or patch == "error" or delete == "error" or put == "error":
            break

        if get == "success": acceptedRequests.append("GET")
        if post == "success": acceptedRequests.append("POST")
        if patch == "success": acceptedRequests.append("PATCH")
        if put == "success": acceptedRequests.append("PUT")
        if delete == "success": acceptedRequests.append("DELETE")

        if acceptedRequests:
            print( Fore.GREEN+"      "+
                  url_+"                      Success"+Fore.CYAN+"                      "+word+Fore.MAGENTA+"           "+
                  ", ".join(acceptedRequests))
            
            response_dict = {}
            response_dict["URL"] = url_
            response_dict["Response"] = "Success"
            response_dict["end-point"] = word
            response_dict["AcceptedRequests"] = ", ".join(acceptedRequests)
            success_urls.append(response_dict)
        else:
            print( Fore.GREEN+"      "+
                  url_+Fore.RED+"                      Failed"+Fore.CYAN+"                      "+word+Fore.MAGENTA+"           --")

    end_time = time.time()
    execution_time = int(end_time - start_time)/60
    total_requests = len(listOfWords)
    success_requests = len(success_urls)
    failed_requests = total_requests - success_requests
    
    print()
    print(Fore.WHITE+"Execution time: "+str(execution_time)+" min")
    print(Fore.WHITE+"Total requests: "+str(total_requests))
    print(Fore.WHITE+"Success requests: "+Fore.GREEN+str(success_requests))
    print(Fore.WHITE+"Failed requests: "+Fore.RED+str(failed_requests))

    if success_requests > 0:
        csv_path = RESULT_PATH+"/"+extract_domain(url)+".csv"
        header = ["URL","Response","End-Point","Accepted-Requests"]
        data = [list(success_url.values()) for success_url in success_urls]

        with open(csv_path, "w",newline="") as f:
            writer = csv.writer(f)
            dict_writer = csv.DictWriter(f, fieldnames=header)
            dict_writer.writeheader()
            writer.writerows(data)
        
        print(Fore.RED+"\n[Note]: "+Fore.GREEN+" Please check results folder to see your results")
    else:
        print(Fore.RED+"\n [Note]: "+Fore.CYAN+" No Working URL found")

    
def display_wordlist(files):
    current_folder = None

    for index,file in enumerate(files):
        split_file = file.split('/')
        folder_name = split_file[-2]
        file_name = split_file[-1]
        
        if folder_name != "default_wordlist" and folder_name != current_folder:
            print(Fore.MAGENTA+"\n\n       "+folder_name+":\n")
            current_folder = folder_name

        print(Fore.CYAN+"          |"+Fore.RED+str(index)+Fore.CYAN+"| "+Fore.LIGHTYELLOW_EX+file_name)

web_url = input(input_text("Enter your target Web URL(with 'http or https')",Fore.GREEN))
if not extract_domain(web_url): # if domain can be extracted then the url is valid
    web_url = ""

while len(web_url) < 1:
    web_url = input(input_text('Enter a valid Web URL(with "http or https")',Fore.RED))
    if not extract_domain(web_url): # if domain can be extracted then the url is valid
        web_url = ""


# wordlist choices (default and custom)
print(Fore.CYAN+"\n\n   |"+Fore.RED+"1"+Fore.CYAN+"| "+Fore.MAGENTA+"Using default wordlist")
print(Fore.CYAN+"   |"+Fore.RED+"2"+Fore.CYAN+"| "+Fore.MAGENTA+"Using custom wordlist")
print(Fore.RED+"\n  [Note]: "+Fore.CYAN+" If you want to use custom wordlist you should add or create a new txt file in custom_wordlist folder")
wordlist_choice = input(input_text("How You want to hunt URLs",Fore.GREEN))

while (len(wordlist_choice) < 1 or int(wordlist_choice) > 2):
    wordlist_choice = input(input_text("Choose a valid option",Fore.RED))
    if wordlist_choice == "1" or wordlist_choice == "2":
        break

if wordlist_choice == "1":
    file_list = get_wordlists(DEFAULT_WORDLIST)
elif wordlist_choice == "2":
    file_list = get_wordlists(CUSTOM_WORDLIST)

# display available wordlists
if len(file_list) > 0:
    print(Fore.GREEN+"\nAvailable wordlist files:\n")
    display_wordlist(file_list)
    selected_wordlist = wordlist_choice = input(input_text("Select a wordlist",Fore.GREEN))

    while (len(selected_wordlist) < 1 or int(selected_wordlist) >= len(file_list)):
        selected_wordlist = input(input_text("Choose a valid Wordlist",Fore.RED))
        if len(selected_wordlist) > 0 and int(selected_wordlist) < len(file_list):
            break

    if selected_wordlist:
        file_path = file_list[int(selected_wordlist)]
        validate(web_url,file_path)

else:
    print(Fore.RED+"\nSorry!!! No wordlist available\n")

