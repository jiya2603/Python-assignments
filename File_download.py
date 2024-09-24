import requests


def download_file(url,file_name):
    response = requests.get(url)
    if response.status_code == 200:
      with open(file_name, 'wb') as file:
        file.write(response.content)
        print(f"File'{file_name}' downloaded succesfully.")
    else:
         print(f"Failed to download file. Status code: {response.status_code}") #Example usage
    
if __name__ == "__main__":
    url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
    file_name = 'dummy.pdf'
    download_file(url, file_name)