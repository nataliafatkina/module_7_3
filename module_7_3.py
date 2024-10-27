class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []

        for file in file_names:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']

        for doc in self.file_names:
            all_words[doc] = []
            with open(doc, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in punctuations:
                        if char in line:
                            line = line.replace(char, '')
                    for words in line.split():
                        all_words[doc].append(words)
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        number_word = 0
        for key, value in all_words.items():
            for word_value in value:
                number_word += 1
                if word.lower() == word_value:
                    return {key: number_word}

    def count(self, word):
        all_words = self.get_all_words()
        number_word = 0
        for key, value in all_words.items():
            for word_value in value:
                if word.lower() == word_value:
                    number_word += 1
            return {key: number_word}



finder1 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())

print(finder1.find('teXt'))
print(finder1.count('teXT'))
