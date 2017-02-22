#字符的定义04 ord(字符的整数表示) chr(编码转化为字符) len(测长度) encode(str→bytes) decode(bytes→str)
ord('A')
#65
ord('中')
#20013
chr(66)
#'B'
print (chr(25991))
#'文'
print ('\u4e2d\u6587')
#'中文'Python对bytes类型的数据用带b前缀的单引号或双引号表示：
#纯英文的str可以用ASCII编码为bytes，内容是一样的，
#含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#在bytes中，无法显示为ASCII字符的字节，用\x##显示
#x = b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
print("'ABC'.encode('ascii')")#[这个要在交互式环境下直接运行、print("")去掉]
#b'ABC'
print("'中文'.encode('utf-8')")
#b'\xe4\xb8\xad\xe6\x96\x87'#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print("'中文'.encode('ascii')")
print("b'ABC'.decode('ascii')")#要把bytes变为str，就需要用decode().要计算str包含多少个字符，可以用len()函数
input()