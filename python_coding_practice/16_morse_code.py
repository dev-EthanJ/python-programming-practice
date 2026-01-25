morse_code = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
dict_items = morse_code.items()
morse_list = list(map(lambda a: list(a), dict_items))


def CodeToChar(code):
    for item in morse_list:
        if item[1] == code:
            return str(item[0]) 
    return "ERROR"

def DecodingMorse(morse):
    result = ""
    word = ""
    for index in range(0, len(morse)):
        if morse[index] != " ":
            word += morse[index]
        else: # char == " "
            if morse[index - 1] != " ":
                # 코드를 문자로 변환하여 문자열에 추가
                result += CodeToChar(word)
                word = ""
                # print(result)
            if morse[index - 1] == " ":
                result += " "
                # print(result)

        if index == len(morse) - 1:
            # 코드를 문자로 변환하여 문자열에 추가
            result += CodeToChar(word)

    return result

morse_str = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
print(DecodingMorse(morse_str))