import requests
from bs4 import BeautifulSoup

# url page with links

url = 'https://docs.juniper.bot/misc/radio-stations/'

response = requests.get(url)
print(response)

with open(file = 'links-radio.M3U', mode = 'w') as file:
    text_for_file = f"""#EXTM3U\n""" 
    file.write(text_for_file)

try: 
    if response.status_code == 200: # check site response
        soup =  BeautifulSoup(requests.get(url).content, "html.parser")
        # print(soup)
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            a = str(a_tag)
            if a.find('.aacp') > 0: 
                # print(a_tag.text) 
                with open(file = 'links-radio.M3U', mode = 'a') as file:
                    text_for_file = f"""{a_tag.text}\n""" 
                    file.write(text_for_file)
    else: 
        print("Error connection")
except:
    print("Error program")
