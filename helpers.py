def rotate_character(char,rot):
    if char.isalpha():
        if char.isupper():
            x = 65
        if char.islower():
            x = 97
    else:
        return char
    position =  ord(char)- x
    if type(rot)==int:
        rot = rot
    else:
        rot = rot.lower()
        rot =  ord(rot)-97
    rotate = (position + rot)% 26
    rotated = chr(rotate + x)
    return rotated

def alphabet_position(text):
    return True
