import re
import requests

def get_script_tag(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    return response.text

    
def getLinks(fullStr):
    pattern = r'onclick="location\.href=\'(.*?)\''
    links = re.findall(pattern, fullStr)
    return links
    

# ----------------------------
# Main script
# ----------------------------
if __name__ == "__main__":
    
    url = "https://nonagon.pt/"
    
    text = get_script_tag(url)
    
    out = getLinks(text)
    count = 1
    
    for str in out:
        if str != "#":
            if count < 10:
                countStr = f"0{count}"
            else: 
                countStr = count    
            print(f"{countStr}: {str}")
            count = count + 1
