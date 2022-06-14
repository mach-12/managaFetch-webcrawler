import os
import requests # pip install requests ## Install Dependency

def main():
    print("\nWelcome to AOT downloader")
    
    CHAPTER = int(input("Enter Chapter: (1 to 139)\n"))
    if CHAPTER > 139 or CHAPTER < 1:
        print(f"\nERROR: chapter {CHAPTER} does not exist, try again\n")
        main()
    
    wantsToDownload = input("Do you wish to download this chapter? (y/n) \n")
    if wantsToDownload in ['y', 'Y', 'YES', 'yes']:
        pass
    else:
        main()
    
    download_file('attack-on-titan', CHAPTER)
    
def download_file(manga, chapter):
    page = 1
    while True:
        file_url = f'https://read.mangadad.com/Mangadad/{manga}/chapter-{chapter}/{page}.jpg'
        output_path = rf'.\AOT-CHAPTER-{chapter}'

        # Checks if path directory exists, Makes new if not
        isExist = os.path.exists(output_path)
        if not isExist:
            os.makedirs(output_path)

        response = requests.get(file_url)

        # 200 is 'healthy' return code
        if response.status_code == 200:
            file_path = os.path.join(output_path, os.path.basename(file_url))
            with open(file_path, 'wb') as f:
                f.write(response.content)

        else:
            # Opens the directory in Windows Explorer
            os.startfile(os.path.realpath(output_path))
            return response.status_code
        page += 1
main()
