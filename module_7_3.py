import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    words = []
                    for line in f:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation + '—'))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:


                print(f"Файл не найден.")
                all_words[file_name] = []

        return all_words


    def find(self, word):
        results = {}
        word = word.lower()
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                position = words.index(word)
                results[name] = position

        return results


    def count(self, word):
        results = {}
        word = word.lower()
        all_words = self.get_all_words()

        for name, words in all_words.items():
            count = words.count(word)
            results[name] = count

        return results


# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT')) 
