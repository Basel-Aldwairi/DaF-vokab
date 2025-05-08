from time import process_time_ns

from reportlab.pdfgen import canvas as ca


def fromTxt(input: str) -> dict[str, list[tuple]]:
    germanEnglish = dict()
    thema = str()
    with open(input, 'r', encoding='utf-8') as file:
        for line in file:

            if '(' in line and '*' not in line and line[0] != ' ' and not '→' in line:

                index = line.index('(')
                thema = ''.join([line[:index - 1]])
                germanEnglish[thema] = []
                print(f'thema {thema}')

            elif '**' in line:
                thema = ''.join([line[2:- 3]])
                germanEnglish[thema] = []
                print(f'thema {thema}')
            elif '→' in line:
                startIndex = line.index('→')
                start = 4
                if '*' in line:
                    start = 2
                german = line[start:startIndex - 1]
                english = line[startIndex + 2:-1]
                germanEnglish[thema].append((german, english))
                print(f'{german} | {english}')
    return germanEnglish


def toTxt(output: str, dictionary: dict[str, list[set]]):
    i = 1
    with open(output, 'w', encoding='utf-8') as file:
        for thema, translation in dictionary.items():
            file.write(f'{thema} : \n')
            file.write('\n')
            for german, english in translation:
                file.write(f'  {i:3} : {german:26} | {english}\n')
                i += 1
                print(i)
                if (i - 1)% 5== 0:
                    file.write('\n')
            file.write('\n\n')


vebs = fromTxt('verbsinput.txt')
toTxt('verbs.txt',vebs)
dictionary = fromTxt('input.txt')
dictionary2 = fromTxt('input2.txt')
dic = {**dictionary, **dictionary2}
toTxt('output.txt', dic)
