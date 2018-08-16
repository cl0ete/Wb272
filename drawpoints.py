import matplotlib.pyplot as plt
import read

def draw_tpl(name):
    a = read.run(name)
    x_val = [x[0] for x in a]
    y_val = [y[1] for y in a]
    plt.plot(x_val, y_val, )
    plt.plot(x_val, y_val, "rs")
    plt.show()
    
def draw(name):
    a = read.run(name)
    plt.plot(x_val, y_val, )
    plt.plot(x_val, y_val, "rs")
    plt.show()

if __name__ == '__main__':
    draw_tpl('points.txt')
