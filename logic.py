def atbash(tt):
    al = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
          'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    answer = ""
    for x in tt:
        if x in (".", ",", ";", ":", "_", "-", ")", "(", "!", "?", "=", "+", " "):
            answer += x
            continue
        flag = True
        if x.isupper():
            x = x.lower()
            flag = False
        ind = al.index(x)
        newind = len(al) - ind - 1
        x1 = al[newind]
        if flag == False:
            x1 = x1.upper()
        answer += x1
    return answer


def cezar(input_data):
    al = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
          'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    ss = 5  # шаг сдвига
    tt = input_data
    answer = ""
    for x in tt:
        if x in (".", ",", ";", ":", "_", "-", ")", "(", "!", "?", "=", "+", " "):
            answer += x
            continue
        flag = True
        if x.isupper():
            x = x.lower()
            flag = False
        ind = al.index(x)
        newind = (ind + ss) % len(al)
        x1 = al[newind]
        if flag == False:
            x1 = x1.upper()
        answer += x1
    return answer



def morza(ar):
    morz= { 'А': '.-',
        'Б': '-...',
        'В': '.--',
        'Г': '--.',
        'Д': '-..',
        'Е': '.',
        'Ё': '.',
        'Ж': '...-',
        'З': '--..',
        'И': '..',
        'Й': '.---',
        'К': '-.-',
        'Л': '.-..',
        'М': '--',
        'Н': '-.',
        'О': '---',
        'П': '.--.',
        'Р': '.-.',
        'С': '...',
        'Т': '-',
        'У': '..-',
        'Ф': '..-.',
        'Х': '....',
        'Ц': '-.-.',
        'Ч': '---.',
        'Ш': '----',
        'Щ': '--.-',
        'Ъ': '--.--',
        'Ы': '-.--',
        'Ь': '-..-',
        'Э': '..-..',
        'Ю': '..--',
        'Я': '.-.-',
        '1': '.----',
        '2': '..---',
        '3':  '... --',
        '4':  '....-',
        '5':  '.....',
        '6':  '-....',
        '7':  '--...',
        '8':  '---..',
        '9':  '----.',
        '0':  '-----',
        '.': '.-.-.-',
        '(': '-.--.',
        ':': '---...',
        '+': '.-.-.',
        ',': '--..--',
        '!': '-.-.--',
        ')': '-.--.-',
        ';': '-.-.-.',
        '-': '-',
        '?': '..--..',
        '=': '-...-',
        '_': '..--.-'
    }
    s = ''
    for i in range(len(ar)):
        s = s + morz[ar[i].upper()] + ' '
    return s
