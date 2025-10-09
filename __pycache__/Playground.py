from deep_translator import GoogleTranslator
while True:
    text = input("Enter text in English: ")
    translation = GoogleTranslator(source="en", target="es").translate(text)
    print(f"Spanish translation: {translation}")

