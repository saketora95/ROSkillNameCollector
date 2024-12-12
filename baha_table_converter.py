import os
import json

config_file = open('config.json', 'r')
config = json.load(config_file)
config_file.close()

lang_list = config['targetLanguage']
lang_list.insert(0, 'ko-KR')
lang_list.insert(0, 'id')
print('Read target language: {}'.format(lang_list))

data_dict = {}
for lang in lang_list:
    if lang == 'id':
        continue

    read_file = open('result/{}-result.txt'.format(lang), 'r', encoding='utf-8')

    if lang == 'ko-KR':
        for line in read_file.readlines():
            if len(line) < 2:
                continue

            raw_skill = line.strip('\n').split('　')
            data_dict[raw_skill[0]] = { 'id': raw_skill[0], lang: raw_skill[1] }

    else:
        for line in read_file.readlines():
            if len(line) < 2:
                continue

            raw_skill = line.strip('\n').split('　')
            if raw_skill[0] in data_dict:
                data_dict[raw_skill[0]][lang] = raw_skill[1]

    read_file.close()

center_col = [0, 1]
bigger_col = [0, 1]
bold_col = [0, 1]

write_file = open('result/table_result.txt', 'w', encoding='utf-8')

write_file.write('[table cellspacing=1 cellpadding=1 border=1 align=center width=100%]\n')
for skill_id in data_dict:
    write_file.write('[tr]\n')
    
    for col_num in range(len(lang_list)):
        temp_text = data_dict[skill_id][lang_list[col_num]]

        if col_num in bold_col:
            temp_text = '[b]{}[/b]'.format(temp_text)

        if col_num in bigger_col:
            temp_text = '[size=3]{}[/size]'.format(temp_text)

        if col_num in center_col:
            temp_text = '[td align=center]{}[/td]'.format(temp_text)
        else:
            temp_text = '[td]{}[/td]'.format(temp_text)
        
        write_file.write(temp_text + '\n')

    write_file.write('[/tr]\n')

write_file.write('[/table]\n')

write_file.close()
