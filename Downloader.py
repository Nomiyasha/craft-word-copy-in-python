import os
import gdown
import zipfile

# See get_valid_words
SYLLABLECOUNT = 1

# A class that is used to download and extract a certain folder of words from google drive as well as
# contain all the words that the folder provides in a list
class AllWords:
    def __init__(self, url="https://drive.google.com/uc?id=0B5eYVI2s0XztOVdaUnNWQWFZOEU", zip="words.zip", out="words"):
        self.__url = url
        self.__zip = zip
        self.__out = out
        self.words = self.__init_files()
        self.valid_words = self.__get_valid_words()

    # Downloads the files from a drive link
    def __download(self):
        try:
            gdown.download(self.__url, self.__zip, quiet=True)
        except Exception as e:
            print(f"Error at __download in Downloader: {e}")

    # Unzips the files and removes some redundant files
    def __extract(self):
        with zipfile.ZipFile(self.__zip, 'r') as zip_ref:
            zip_ref.extractall(self.__out)

        try:
            os.remove(self.__zip)
            os.remove(f"{self.__out}/readme.txt")
        except Exception as e:
            print(f"Could not remove readme.txt. Error {e}")

    # returns a list of all the words in the downloaded files
    def __get_array(self):
        arr = []
        # for readability
        folder = self.__out
        try:
            for subfolder in os.listdir(folder):
                for text in os.listdir(f"{folder}/{subfolder}"):
                    with open(f"{folder}/{subfolder}/{text}", 'r') as file:
                        data = file.read().split("\n")
                        for word in data:
                            arr.append(word.lower())

        except Exception as e:
            print(f"Error at get_array in Downloader: {e}")
        return arr

    # returns a list of X syllable long words from the downloaded files, where x is defined at the top of this document
    # we do this because for example "overgrazing" and "humidifier" are really hard words to play with in this game
    # this function must be run after __init_files, also doesn't work if another url is used.
    def __get_valid_words(self):

        if self.__url != "https://drive.google.com/uc?id=0B5eYVI2s0XztOVdaUnNWQWFZOEU":
            print("Wrong url, cannot use get_valid_words")
            return ["hello", "world"]

        arr = []
        folder = self.__out
        try:
            for subfolder in os.listdir(folder):
                for text in os.listdir(f"{folder}/{subfolder}"):
                    for i in range(1, SYLLABLECOUNT+1):
                        check_text = f"{i}"+"syllable"+f"{subfolder}"+".txt"
                        if text in check_text:
                            with open(f"{folder}/{subfolder}/{text}", 'r') as file:
                                #print(f"read {text}")
                                data = file.read().split("\n")
                                for word in data:
                                    arr.append(word.lower())

        except Exception as e:
            print(f"Error at select_words in Downloader: {e}")
        return arr

    # downloads, extracts, and then returns the downloaded words as an array
    def __init_files(self):
        try:
            self.__download()
            self.__extract()
            return self.__get_array()
        except Exception as e:
            print(f"Error at init_files in Downloader: {e}")




