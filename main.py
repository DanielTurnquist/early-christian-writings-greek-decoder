from greek_accentuation.characters import *

if __name__ == '__main__':
    file_name = input("enter an encoded greek text from early christian writings: ")
    #file_name = "apokaluyis iakwb.txt"
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    greekCharsLower = "αβγδεζηθικλμνξοπρσςτυφχψω"
    greekCharsUpper = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩ"
    latinCharslower = "abgdezhqiklmnxoprsvtufcyw"
    latinCharsUpper = latinCharslower.upper()
    for i in range(len(latinCharsUpper)):
        text = text.replace(latinCharsUpper[i], greekCharsUpper[i])
        text = text.replace(latinCharslower[i], greekCharsLower[i])
    new_text = ""
    try:
        i = 0
        while i < len(text):
            if text[i] in "jJ<>=+[]|~":
                i += 1
                continue
            if text[i].isalpha() or text[i] == " ":
                new_char = text[i]

                for j in range(1, 3):
                    if text[i+j] not in "jJ<>=+[]|~":
                        break
                    if text[i + j] == 'j':
                        new_char = add_breathing(new_char, SMOOTH)
                        continue
                    if text[i + j] == 'J':
                        new_char = add_breathing(new_char, ROUGH)
                        continue
                    if text[i + j] == '~':
                        new_char = add_diacritic(new_char, CIRCUMFLEX)
                        continue
                    if text[i + j] == ']':
                        new_char = add_breathing(add_diacritic(new_char, ACUTE), SMOOTH)
                        continue
                    if text[i + j] == '[':
                        new_char = add_breathing(add_diacritic(new_char, ACUTE), ROUGH)
                        continue
                    if text[i + j] == '+':
                        new_char = add_breathing(add_diacritic(new_char, CIRCUMFLEX), SMOOTH)
                        continue
                    if text[i + j] == '>':
                        new_char = add_diacritic(new_char, ACUTE)
                        continue
                    if text[i + j] == '<':
                        new_char = add_diacritic(new_char, GRAVE)
                        continue
                    if text[i + j] == '|':
                        new_char = add_diacritic(new_char, IOTA_SUBSCRIPT)
                        continue
                new_text += new_char
            else:
                new_text += text[i]
            i += 1
        new_text += text[-1]
    except IndexError:
        pass
    new_file_name = file_name.split('.')[0]
    new_file_name += "_decoded.txt"
    with open(new_file_name, 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_text)
        new_file.close()