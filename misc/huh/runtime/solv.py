# Define the NATO phonetic alphabet mapping
natoToAlpha = {
    'Alfa': 'A', 'Bravo': 'B', 'Charlie': 'C', 'Delta': 'D',
    'Echo': 'E', 'Foxtrot': 'F', 'Golf': 'G', 'Hotel': 'H',
    'India': 'I', 'Juliett': 'J', 'Kilo': 'K', 'Lima': 'L',
    'Mike': 'M', 'November': 'N', 'Oscar': 'O', 'Papa': 'P',
    'Quebec': 'Q', 'Romeo': 'R', 'Sierra': 'S', 'Tango': 'T',
    'Uniform': 'U', 'Victor': 'V', 'Whiskey': 'W', 'X-ray': 'X',
    'Yankee': 'Y', 'Zulu': 'Z'
}

decodeToStr = {' ':'',
    '(space)':' '}


def readData(filename: str):
    try:
        with open(filename, 'r') as t:
            fileData = t.read()

            return fileData

    except Exception as e:
        print(f"[!] fail to read {filename}")


def decodeNato(fileData: str):

    # nato 먼저
    for nato, value in natoToAlpha.items():
        fileData = fileData.replace(nato, value)

    # 보기 좋게
    for key, value in decodeToStr.items():
        fileData = fileData.replace(key, value)

    return fileData


if __name__=="__main__":
    fileData = readData('WoosukUniv.txt')
    result = decodeNato(fileData)

    print(result.lower())