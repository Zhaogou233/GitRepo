import re
 
def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:    
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): 
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring
 
def querySimpleProcess(ss):
    s1=strQ2B(ss)
    s2=re.sub(r"(?![\u4e00-\u9fa5]|[0-9a-zA-Z])."," ",s1) 
    s3=re.sub(r"\s+"," ",s2)
    return s3.strip().lower()
 

def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
 

def check_contain_english(check_str):
    for ch in check_str:
        if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':
            return True
    return False
 

def delete_letters(ss):
    rs = re.sub(r"[a-zA-Z]+","",ss)
    return rs
 

def countCharacters(inputStr):
    tmpStr = querySimpleProcess(inputStr)
    str2list = tmpStr.strip().split(" ")
    if len(str2list) > 0:
        charsNum = 0
        for elem in str2list:
            chineseFlag = check_contain_chinese(elem)
            englishFlag = check_contain_english(elem)
            if englishFlag == False:
                charsNum = charsNum + len(elem)
                continue
            else:
                elem = delete_letters(elem)
                charsNum = charsNum + 1 + len(elem)
        return charsNum
    return 0
