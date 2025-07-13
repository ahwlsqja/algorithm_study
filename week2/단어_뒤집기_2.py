s = input()
stack = []
s_list = []
reversing_s = ''

pairs = {"<": ">"}

for char in s:
    if len(stack) == 0:
        if "<" in char:
            if reversing_s != '':
                s_list.append(reversing_s[::-1])
                reversing_s =''
            stack.append(char)
            s_list.append(char)

        
        elif char == ' ':
            s_list.append(reversing_s[::-1] + ' ')
            reversing_s = ''
        
        else: 
            reversing_s += char

        
    elif ">" in char:
        stack.pop()
        s_list.append(char)
    else:
        s_list.append(char)

if reversing_s != '':
    s_list.append(reversing_s[::-1])
            
print(''.join(s_list))