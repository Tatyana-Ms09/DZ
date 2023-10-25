text = input("Введите текст: ")

sentences = text.split('.')
sentences += text.split('!')
sentences += text.split('?')

num_sentences = len(sentences)

print("Количество предложений в тексте:", num_sentences)

