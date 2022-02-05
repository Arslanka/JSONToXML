import string
import time
import re


def show_variant() -> string:
    print("Мой вариант -", 335089 % 36)


def insert_tabs(tabs) -> string:
    return '\t' * tabs


def beg_tag(s) -> string:
    return '<' + s + '>'


def end_tag(s) -> string:
    return "</" + s + ">\n"


def JSON_to_XML(f, res) -> string:
    ans = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<root>\n"
    stack_for_brackets = []  # пара (скобка, тег)
    strings = re.split('\n', f)
    convert = []
    for _ in strings:
        _ = re.sub("\"", '', _)
        _ = _.lstrip()
        if _[-1] == ':':
            _ = _[:-1]
        convert.append(_.split(": ", 1))
    last = ""
    tab = 0
    for i in range(1, len(convert) - 1):
        if len(convert[i]) == 1:
            if len(convert[i][0]) != 1 and len(stack_for_brackets) == 0:
                last = convert[i][0]
            else:
                if convert[i][0] == '[':
                    stack_for_brackets.append(('[', last))
                    tab += 1
                if convert[i][0] == '{':
                    stack_for_brackets.append(('{', last))
                    ans += insert_tabs(tab) + beg_tag(last) + '\n'
                    tab += 1
                if convert[i][0] == '}':
                    tab -= 1
                    top = stack_for_brackets[-1][1]
                    stack_for_brackets.pop()
                    ans += insert_tabs(tab) + end_tag(top)
            if convert[i][0] == "},":
                tab -= 1
                top = stack_for_brackets[-1][1]
                stack_for_brackets.pop()
                ans += insert_tabs(tab) + end_tag(top)
        else:
            ans += insert_tabs(tab) + beg_tag(convert[i][0]) + convert[i][1][:-1] + end_tag(convert[i][0])
    ans += "</root>\n"
    return ans
    # print(stack_for_brackets)


start_time = time.time()
f = open("Json.json", "r")
r = open("XML2.xml", "w")
file = f.read()
show_variant()
ans = ""
for i in range(0, 10):
    ans = JSON_to_XML(file, r)
r.write(ans)
print(f'time:  { 1000 * (time.time() - start_time)}')# добавить табы + стэк для тэгов
# ('[', ']') - обозначают массив, '{', '}' -объект
# Если встретилась квадратная скобка, то дальше будут объекты массива. Пока скобка не закроется, теги объектов = название масива
