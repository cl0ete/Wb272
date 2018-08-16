a = []

def read(name):
    file = open(name,'r')

    for line in file:
        a.append(line.strip().split('\t'))
    file.close()

def run(name):
    read(name)
    convert(a)
    return a

def convert(a):
    index = 0
    for line in a:
        a[index]=(float(line[0]),float(line[1]))
        index += 1

if __name__ == '__main__':
    read('points.txt')
    convert()
    print a
