import requests
from bs4 import BeautifulSoup

def get_word_en():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        words_en = soup.find('div', id='random_word')
        words_definition = soup.find('div', id='random_word_definition')

        return {
            'word': words_en.text.strip(),
            'definition': words_definition.text.strip()
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def game():
    print('Начинаем игру')
    while True:
        words_dict = get_word_en()
        word = words_dict.get('word')
        definition = words_dict.get('definition')
        print(f'Значение слова - {definition}')
        user = input('Что это за слово? ')
        if user == word:
            print('Всё верно!')
        else:
            print(f'Не правильно! Это слово - {word}')

        play_again = input('Хотите сыграть ещё? y/n ')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

game()