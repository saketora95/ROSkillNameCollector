import os
import json

lang_list = ['zh-TW', 'ko-KR', 'ja-JP', 'en-US', 'pt-BR']
main_lang_index = 0

input_dict = {}
for lang in lang_list:
    input_dict[lang] = {}
    read_file = open('result/{}-result.txt'.format(lang), 'r', encoding='utf-8')

    for line in read_file.readlines():
        if len(line) < 3:
            continue

        raw_text = line.strip('\n').split('　')
        input_dict[lang][raw_text[0]] = raw_text[1]
    
    read_file.close()

result_dict = {}
for id in input_dict['ko-KR']:
    for lang in lang_list:
        if lang == 'zh-TW':
            continue

        result_dict[input_dict[lang][id]] = input_dict['zh-TW'][id]

write_file_json = open('result/translate_table.json', 'w', encoding='utf-8')
write_file_json.write(
    json.dumps(
        result_dict,
        indent=4,
        ensure_ascii=False
    )
)
write_file_json.close()
