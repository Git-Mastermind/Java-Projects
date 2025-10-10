from deep_translator import GoogleTranslator, LingueeTranslator
while True:
    text = input("Enter text in English: ")
    google_translation = GoogleTranslator(source="en", target="fr").translate(text)
    print(f"Spanish translation: {google_translation}")

    linguee_translator = LingueeTranslator(source="en", target="fr").translate(text)
    print(f"Spanish translation: {linguee_translator}")
    

