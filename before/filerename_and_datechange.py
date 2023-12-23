import os
dir=''
def func(oStr,nStr,oStr2,nStr2):
    path = os.getcwd() + dir
    files = os.listdir(path)
    for file in files:
        if oStr in file:
            file_path = path +'\\'+ file
            new_file_path = path +'\\'+ file.replace(oStr,nStr)
            with open(file_path, 'r', encoding='utf-8') as f1,open(new_file_path, 'w', encoding='utf-8') as f2:
                for line in f1:
                    if oStr in line:
                        line = line.replace(oStr,nStr)
                    if oStr2 in line:
                        line = line.replace(oStr2,nStr2)
                    f2.write(line)
            os.remove(file_path)

def func2(oStr,nStr):
    path = os.getcwd() + dir
    files = os.listdir(path)
    for file in files:
        file_path = path + '\\' + file
        if file not in __file__:
            with open(file_path, 'r', encoding='utf-8') as f1,open('%s.bak'% file_path, 'w', encoding='utf-8') as f2:
                for line in f1:
                    if oStr in line:
                        line = line.replace(oStr,nStr)
                    f2.write(line)
            os.remove(file_path)
            os.rename('%s.bak'% file_path,file_path)
if __name__ == '__main__':
    # func('H_','','AresHiAudioTestCase','AresSharkTestCase')
    # func2('timeout(500)','timeout(2000)')
    print(__file__)