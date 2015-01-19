#!/usr/bin/python3
import re, sys
class ProcessSrt:
    dictTxt = {}
    fileName = ''

    def __init__(self, fileName):  
        self.fileName = fileName
        dictHandler = open('dict.txt')
        dictline = dictHandler.readline()
        while dictline:
            word = dictline.lower().split(maxsplit=1)
            self.dictTxt.update({word[0]:word[1][:-1]})
            dictline = dictHandler.readline() 
        
    def englishWord(self, word):
        for uchar in word:
            if (uchar >= 'a' and uchar<='z') or (uchar >= 'A' and uchar<='Z'):
                pass
            else:
                return False
        return True
    
    def getTranslate(self, word):
        newWord = None
        if word.lower() in self.dictTxt:
            newWord = word + '['+self.dictTxt[word.lower()]+']'
        return newWord
    
    def processSrt(self):
        fileHandler = open(self.fileName, 'r+')
        line = fileHandler.readline()
        filetxt = []
        while line:
            words = [w.strip(',.?') for w in line.split() if w.strip(',.?')]
            for word in words:
                if self.englishWord(word) and self.getTranslate(word) != None:
                    p = re.compile(word + '[\s|\?|,|.]')
                    line = p.sub(self.getTranslate(word) + ' ', line)
            filetxt.append(line)
            line = fileHandler.readline()
    
        fileHandler = open(self.fileName, 'w')
        for txt in filetxt:
            fileHandler.write(txt)
        fileHandler.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Arguments Error! ' + str(len(sys.argv)))
        exit(0)
    p = ProcessSrt(sys.argv[1])
    p.processSrt()
