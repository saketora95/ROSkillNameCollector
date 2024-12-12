import json
import requests
import os
import time

reqUrl = 'https://www.divine-pride.net/api/database/Skill/'

result_file_dict = {}

def fetch_data(data_id, api_key, target_language):
    url = f'{reqUrl}{data_id}?apiKey={api_key}'

    if target_language == 'ko-KR':
        url += '&server=kROM'

    header = {'Accept-Language': target_language}

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        if response.status_code == 403:
            return 'STOP'

        if response.status_code == 404:
            return None


        print(f'HTTP 請求錯誤: {e}')
        return None
    except ValueError:
        print('回傳的資料無法解析為 JSON')
        return None

if os.path.exists('config.json'):
    config = open('config.json', 'r')
    config = json.load(config)
    print('Read API key: {} ...'.format(config['apiKey'][:5]))
    print('Read target language: {}'.format(config['targetLanguage']))

    result_file_dict['ko-KR'] = open('result/ko-KR-result.txt', 'a', encoding='utf-8')
    for lang in config['targetLanguage']:
        result_file_dict[lang] = open('result/{}-result.txt'.format(lang), 'a', encoding='utf-8')

    for i in range(6050, 6600):
        print(f'- Process to skill ID: {i}')

        skill_info = fetch_data(i, config['apiKey'], 'ko-KR')
        if skill_info == 'STOP':
            print('- Get [ STOP ] signal.')
            break

        if skill_info is None or 'name' not in skill_info or skill_info['name'] is None:
            continue

        print('    - Get [ ko-KR ] skill name: {}'.format(skill_info['name']))
        if len(skill_info['name']) > 3 and skill_info['name'][:3] == 'NPC':
            print('    - Skip NPC skill.')
            continue
        
        result_file_dict['ko-KR'].write('{}　{}\n'.format(i, skill_info['name']))

        for lang in config['targetLanguage']:
            skill_info = fetch_data(i, config['apiKey'], lang)

            if skill_info is None or 'name' not in skill_info:
                print('    - Get [ {} ] skill name: None'.format(lang))
                result_file_dict[lang].write('{}　{}\n'.format(i, 'none'))
                continue

            print('    - Get [ {} ] skill name: {}'.format(lang, skill_info['name']))
            result_file_dict[lang].write('{}　{}\n'.format(i, skill_info['name']))
        time.sleep(0.5)
else:
    print('Config file not exist, stop process.')
    os.system('pause')
