from django import template

register = template.library()

def cut_words(value, length=3):
    return value[:length]

register.filter('cut_words', cut_words)