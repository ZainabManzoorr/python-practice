sentence = "Hello, welcome to Python programming!"

reversed_sentence = " ".join([word[::-1] for word in sentence.split()])
print(reversed_sentence)