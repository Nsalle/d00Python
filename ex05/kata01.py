languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

# for lang,name in languages.items():
#    kata01 = ""
#    kata01 += lang
#    kata01 += " was created by "
#    kata01 += name
#    print(kata01)

for lang, name in languages.items():
    print("{} was created by {}".format(lang, name))
