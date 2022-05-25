fstring_from_file = open('a.txt', 'r').read().split(' - ')[0]
compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
formatted_output = eval(compiled_fstring)
print(formatted_output)