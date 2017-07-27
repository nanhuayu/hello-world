# coding:utf8

link_0 = "https://translate.google.cn/translate_a/single?"
link_1 = "client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&kc=9&tk=791417.673923&q=ship"

link_tts = "https://translate.google.cn/translate_tts?ie=UTF-8&q=%C3%A7a%20va%20bien&tl=fr&total=1&idx=0&textlen=10&tk=390962.240840&client=t&prev=input"

def TL(a):
    b = 406644;
    b1 = 3293161072;
    sb = "+-a^+6";
    zb = "+-3^+b+-f";
    e = []
    for i in range(len(a)):
        m = ord(a[i])
        if m < 128 :
            e.append(m)
        else:
            if (m < 2048):
                e.append( m >> 6 | 192)
            else:
                if 55296 == (m & 64512) and i + 1 < len(a) and 56320 == (ord(a[g + 1]) & 64512):
                    i += 1
                    m = 65536 + ((m & 1023) << 10) + (ord(a[i]) & 1023)
                    e.append(m >> 18 | 240)
                    e.append(m >> 12 & 63 | 128)
                else:
                    e.append(m >> 12 | 224)
                e.append(m >> 6 & 63 | 128)
            e.append(m & 63 | 128)
    print(e)
    tmp = b
    for i in e:
        tmp += i
        tmp = RL(tmp, sb)
    print(tmp)
    tmp = RL(tmp, zb)
    tmp ^= b1 or 0;
    if tmp < 0:
        tmp = (tmp & 2147483647) + 2147483648
    tmp %= 1000000
    return str(tmp) + "." + str(tmp ^ b)

def RL(a, b):
    t = "a"
    Yb = "+"
    for i in range(0,(len(b)-2), 3):
        d = b[i+2]
        if (d>=t): d = ord(d)-87
        else:d = int(d)
        if (b[i+1]) == Yb: d = a >> d
        else: d = a<<d
        if b[i] == Yb: a = a + d & 4294967295
        else: a = a ^ d
    return a

