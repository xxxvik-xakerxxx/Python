#-*-coding: utf-8-*
import sys
from bitarray import bitarray

class lz77:
    #Реализациа алгоритма LZ77
    searchBufferSize = 250
    lookABufferSize = 250
    def __init__(self):
        pass
    def sch(self,lookABuffer, searchBuffer):
        offset = 0
        length = 0
        for i in xrange(1, self.searchBufferSize+1):
            l = 0
            o = 0
            if searchBuffer[self.searchBufferSize - i ] is None:
                if l >= length:
                    length = l
                    offset = i
                break
            for j in xrange(i):
                if j  >= len(lookABuffer)-1:
                    if l >= length:
                        length = l
                        offset = i
                    break
                if searchBuffer[self.searchBufferSize - i + j] == lookABuffer[j]:
                    l += 1
                else:
                    if l >= length:
                        length = l
                        offset = i
                    break
                if l == i:
                    if l >= length:
                        length = l
                        offset = i
                    break
        return length,offset
    def compress(self,file,DEBUG=False):
        #DEBUG=True для отладки
        try:
            with open(file,'rb') as f:
                s = list(f.read())
        except IOError:
            print 'Unable to open file'
            exit(1)
        # print s
        outFile = file.split('.')
        ext = outFile[-1]
        outFile = ''.join(outFile[:-1] + ['.lz77'])
        l = len(ext)
        out = bitarray(endian='big')
        out.frombytes(chr(l))
        for i in ext:
            out.frombytes(i)
        searchBuffer = [None]*self.searchBufferSize
        lookABuffer = s[:self.lookABufferSize]
        s = s[self.lookABufferSize:]
        while len(lookABuffer) != 0:
            length,offset = self.sch(lookABuffer, searchBuffer)
            try:
                symbol = lookABuffer[length]
            except IndexError:
                symbol = '$'
            if length > 0:
                if symbol == '$' and len(s) > 0:
                    symbol = s[0]
                    searchBuffer.extend(lookABuffer + [symbol])
                    searchBuffer = searchBuffer[length + 1:]
                    lookABuffer.extend(s[:length+1])
                    s = s[length+1:]
                    lookABuffer = lookABuffer[length+1:]
                else:
                    searchBuffer.extend(lookABuffer[:length+1])
                    searchBuffer = searchBuffer[length + 1:]
                    lookABuffer.extend(s[:length+1])
                    s = s[length+1:]
                    lookABuffer = lookABuffer[length+1:]
                    if DEBUG:
                        print offset,length,symbol
            else:
                if DEBUG:
                    print 0,symbol
                searchBuffer.pop(0)
                e = lookABuffer.pop(0)
                searchBuffer.append(e)
                try:
                    e = s.pop(0)
                    lookABuffer.append(e)
                except:
                    pass
            if offset != 0:
                out.append(True)
                out.frombytes(chr(offset))
                out.frombytes(chr(length))
                out.frombytes(symbol)
            else:
                out.append(False)
                out.frombytes(symbol)
        out.fill()
        try:
            with open(outFile,'wb') as f:
                f.write(out.tobytes())
        except IOError:
            print 'Unable to write compressed file'
            exit(1)
    def decompress(self,file,DEBUG = False):
        #DEBUG=True для отладки
        data = bitarray(endian='big')
        res = []
        try:
            with open(file,'rb') as f:
                data.fromfile(f)
        except IOError:
            print 'Не могу прочитать файл, возможно его не существует,или вы просите невозможногою'
            exit(1)

        ext = '.'
        l = ord(data[:8].tobytes())
        del(data[:8])
        while l >0:
            ext += data[:8].tobytes()
            del(data[:8])
            l -= 1
        while len(data) >= 9:
            flag = data.pop(0)
            if not flag:
                symbol = data[0:8].tobytes()
                offset = 0
                length = 0
                del(data[0:8])
                if DEBUG:
                    print 0,0,symbol
            else:
                offset = ord(data[0:8].tobytes())
                length = ord(data[8:16].tobytes())
                symbol = data[16:24].tobytes()
                if DEBUG:
                    print offset,length,symbol
                del(data[:24])
            x = []
            if -offset + length >= 0:
                x = res[-offset:] + res[:-offset + length] + [symbol]
            else:
                x = res[-offset:-offset + length] + [symbol]
            res.extend(x)
            # print res
        if res[-1] == '$':
            res.pop()
        v = ''.join(res)
        # print v
        outFile = ''.join(file.split('.')[:-1] + [ext])
        try:
            with open(outFile,'wb') as f:
                f.write(v)
        except IOError:
            print 'Не могу найти файл, возможно его не существует, либо вы просите невозможного.'
            exit()
if __name__ == '__main__':
    arg = sys.argv[1:]
    if arg[0] == '-h' or arg[0] == '--h' or arg[0] == '-help':
        print "используйте lz77.py [-c | -d ] имя файла"
        print "опции:"
        print "-c\t\t\t:Сжатие."
        print "-d\t\t\t:Расшифровка."
        exit(0)
    elif arg[0] == '-c':
        l = lz77()
        try:
            print 'Сжатие...'
            l.compress(arg[1])
        except:
            print 'Ошибка сжатия.'
            exit(1)
        print 'Завершено.'
    elif arg[0] == '-d':
        l = lz77()
        try:
            print 'Расшифровка...'
            l.decompress(arg[1])
        except:
            print 'Ошибка расшифровки.'
            exit(1)
        print 'Завершено.'
    else:
        print "Ошибка ввода"
        print "используйте script.py [-c | -d ] Имя файла"
        print "опции:"
        print "-c\t\t\t:Сжатие."
        print "-d\t\t\t:Расшифровка."
        exit(0)
