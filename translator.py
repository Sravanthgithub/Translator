from translate import Translator
'''
I am gonna translate into Japanese. If u want to translate
into any other languages then pls kindly use pyhton documentation
for knowing the code of other languages. (Like how we represent 
japanese as 'ja' )
'''
translator = Translator(to_lang='ja')

try:
    with open(r'''C:\Users\Sravanth\OneDrive\Desktop\Python\Udemy Course\some.txt''') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Please kindly check your file path!')
