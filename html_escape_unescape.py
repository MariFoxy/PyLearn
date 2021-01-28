'''
Программа, меняющая угловые скобки в HTML документе на их экранированные аналоги.
'''

import html

#Экранирование тегов
tag_script = html.escape("This HTML fragment contains a <script> </script> tag.")
print (tag_script)

#Возвращение тегов в виде угловых скобок <>
no_tag_script = html.unescape("I &hearts; Python's &lt;standart library&gt;.")
print(no_tag_script)
