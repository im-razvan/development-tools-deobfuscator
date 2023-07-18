from random import randint,choice
from datetime import date
import secrets
import string
import codecs  
import zlib
import marshal
import base64

watermark = f'''"""
  --  Guardian Protector
       {date.today().strftime("%d/%m/%Y")}                                                                                                                                           
"""
'''

def string_enc(string):
    f = ""
    m = randint(3,12)

    for letter in string:
        f+=str(ord(letter)*m)+","

    f=f[:-1]

    return f"''.join(chr(int(i/{m})) for i in [{f}])"

def split_string(input_string):
    variables = {}
    reconstruction = []
    
    for char in input_string:
        if char not in variables:
            var_name = choice(string.ascii_lowercase) + choice(string.ascii_uppercase)
            while var_name in variables.values():
                var_name = choice(string.ascii_lowercase) + choice(string.ascii_uppercase) + choice(string.ascii_lowercase)
            variables[char] = var_name
        
        reconstruction.append(variables[char])
    
    variables_string = ';'.join([f'{var}="{chr(char)}"' for char, var in variables.items()])
    reconstruction_string = '+'.join([var for var in reconstruction])
    
    return variables_string, reconstruction_string

print("\n\n\n")
ptt = '4637192805'
code_to_obfuscate = """a = 5
print(f'a = {a}')"""

randxor = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30))

memestrings = [ 
    randxor,''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30))
]

for i in range(len(memestrings)):
    memestrings[i] = string_enc(memestrings[i])


def random_math(_sum):
    try:
        f = randint(-_sum,randint(-_sum,999))
        f1 = randint(-_sum,randint(-_sum,999))
        f2 = randint(-_sum,randint(-_sum,999))
        return f'{_sum-f-f1+f2}+{f}+{f1}-{f2}'
    except Exception as e:
        print(e)
        return str(_sum)

xor = lambda message,key: ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, __import__("itertools").cycle(key)))

def enc(x, use_xor=True):
    final = ""
    if use_xor==True:
        x = xor(x,randxor)
    for letter in x:
        fl = "{}".format(ord(letter))
        for character in fl:
            final+=ptt[int(character)]
        final+='​'
        
    return final[:-1]

#print(enc("exec",False))


def obfuscate(code):
    b = compile(code, '', 'exec')

    code_bytes = marshal.dumps(b) 
    encoded_code = base64.b64encode(code_bytes)

    vars_str, recon_str = split_string(encoded_code)
    code2 = f"""__builtins__.eval("".join(chr(i) for i in [101,120,101,99]))(__import__({string_enc("marshal")}).loads(__import__({string_enc("base64")}).b64decode({recon_str})))"""

    return watermark+r"o,g={},[];"+f"""{vars_str};g.append({choice(memestrings)});eval({string_enc('setattr(__builtins__,"______",compile)')});o["ꀀ"]="0";g.append({choice(memestrings)});o["ꀁ"]="1";g.append({choice(memestrings)});o["ꀂ"]="2";g.append({choice(memestrings)});o["ꀃ"]="3";g.append({choice(memestrings)});o["ꀄ"]="4";g.append({choice(memestrings)});o["ꀅ"]="5";g.append({choice(memestrings)});o["ꀆ"]="6";g.append({choice(memestrings)});o["ꀇ"]="7";g.append({choice(memestrings)});o["ꀈ"]="8";o["ꀉ"]="9";o["ꀊ"]="A";o["ꀋ"]="B";o["ꀌ"]="C";o["ꀍ"]="D";g.append({string_enc(randxor)});o["ꀎ"]="E";o["ꀏ"]="F";o["ꀐ"]="G";o["ꀑ"]="H";o["ꀒ"]="I";o["ꀓ"]="J";o["ꀔ"]="K";o["ꀕ"]="L";o["ꀖ"]="M";o["ꀗ"]="N";o["ꀘ"]="O";o["ꀙ"]="P";o["ꀚ"]="Q";o["ꀛ"]="R";g.append({choice(memestrings)});o["ꀜ"]="S";o["ꀝ"]="T";o["ꀞ"]="U";g.append({choice(memestrings)});o["ꀟ"]="V";__=lambda _:''.join(chr(int(''.join(str('{ptt}'.index(j))for j in i)))for i in _.split('​'));o["ꀠ"]="W";o["ꀡ"]="X";o["ꀢ"]="Y";g.append({choice(memestrings)});o["ꀣ"]="Z";o["ꀤ"]="a";g.append({choice(memestrings)});o["ꀥ"]="b";o["ꀦ"]="c";g.append({choice(memestrings)});o["ꀧ"]="d";o["ꀨ"]="e";o["ꀩ"]="f";g.append({choice(memestrings)});o["ꀪ"]="g";o["ꀫ"]="h";o["ꀬ"]="i";o["ꀭ"]="j";o["ꀮ"]="k";o["ꀯ"]="l";g.append({choice(memestrings)});o["ꀰ"]="m";o["ꀱ"]="n";o["ꀲ"]="o";o["ꀳ"]="p";o["ꀴ"]="q";o["ꀵ"]="r";o["ꀶ"]="s";o["ꀷ"]="t";g.append({choice(memestrings)});o["ꀸ"]="u";o["ꀹ"]="v";o["ꀺ"]="w";o["ꀻ"]="x";o["ꀼ"]="y";o["ꀽ"]="z";g.append({choice(memestrings)});eval({string_enc('setattr(__builtins__,"____",eval)')});g.append({choice(memestrings)});eval({string_enc('setattr(__builtins__,"_____",exec)')});g.append({choice(memestrings)});g.append({choice(memestrings)});____({string_enc("__builtins__")}).__dict__[__('{enc("_____",False)}')](____({string_enc('''____(____(o["ꀦ"]+o["ꀲ"]+o["ꀰ"]+o["ꀳ"]+o["ꀬ"]+o["ꀯ"]+o["ꀨ"])('compile','','eval'))''')})(____((lambda x,y: ''.join(chr(ord(c)^ord(k)) for c,k in zip(x, __import__({string_enc("itertools")}).cycle(y))))(__({string_enc(enc(f"(lambda x,y: ''.join(chr(ord(c)^ord(k)) for c,k in zip(x, __import__({string_enc('itertools')}).cycle(y))))"))}),g[{random_math(9)}]))(__(____(__import__({string_enc("codecs")}).decode(__import__({string_enc("zlib")}).decompress({ str(zlib.compress(codecs.encode(string_enc(enc(code2))), 9))})))),g[{random_math(9)}]),'',{string_enc("exec")}));g[1],g[3],g[4],g[5],g[6],g[9]=1,2,3,4,5,6;_____({string_enc('obfuscated_with_guardian = g[5]')}); g[9] = 32 if obfuscated_with_guardian == g[5] else 0;____({string_enc('print(chr(g[9]))')}) ##end"""

with open("obf.py", "w", encoding="utf-8") as f:
    f.write(obfuscate(code_to_obfuscate))

print("Obfuscated")

print("\n\n\n")