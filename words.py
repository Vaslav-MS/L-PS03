import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='en', target='ru')

def get_word():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        word_en = soup.find('div', id='random_word').text.strip()
        def_en = soup.find('div', id='random_word_definition').text.strip()

        # Перевод
        word_ru = translator.translate(word_en)
        def_ru = translator.translate(def_en)

        return {
            'word': word_ru,
            'definition': def_ru
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def game():
    print('Начинаем игру')
    while True:
        words_dict = get_word()
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