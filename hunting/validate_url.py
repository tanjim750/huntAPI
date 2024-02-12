import requests,os
from colorama import Fore

class Request:
    def __init__(self,url,headers=None):
        self.url = url
        if headers is not None:
            self.headers = headers
        else:
            self.headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-length': '0',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
            }

    def Get(self):
        try:
            response = requests.get(self.url, headers = self.headers)
            return "success" if response.status_code == 200 else False
        
        except Exception as e:
            print(Fore.RED+"\nPlease check your connection and try again")
            return "error"
        
    def Post(self):
        try:
            response = requests.post(self.url, headers = self.headers)
            return "success" if response.status_code == 200 else "failed"
        
        except Exception as e:
            print(Fore.RED+"\nPlease check your connection and try again")
            return "error"
        
    def Patch(self):
        try:
            response = requests.patch(self.url, headers = self.headers)
            return "success" if response.status_code == 200 else "failed"
        
        except Exception as e:
            print(Fore.RED+"\nPlease check your connection and try again")
            return "error"
    
    def Put(self):
        try:
            response = requests.put(self.url, headers = self.headers)
            return "success" if response.status_code == 200 else "failed"
        
        except Exception as e:
            print(Fore.RED+"\nPlease check your connection and try again")
            return "error"
    
    def Delete(self):
        try:
            response = requests.delete(self.url, headers = self.headers)
            return "success" if response.status_code == 200 else "failed"
        
        except Exception as e:
            print(Fore.RED+"\nPlease check your connection and try again")
            return "error"
