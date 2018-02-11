import re

string = 'h' + 'e' + 'l' + 'l' + 'o' + ',' + 'w' + 'o' + 'r' + 'l' + 'd'
print(string)

string = 'h232e3dsl423lfs2oeqw,234wffwo432r432l43fd555'[::4]
print(string)

string = 'h232e3dsl423lfs2oeqw,234wffwo432r432l43fd555'
string = re.sub(r'^(helo,wrd)',r'',string)
print(string)
