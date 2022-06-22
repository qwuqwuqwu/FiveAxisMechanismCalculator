# This is a sample Python script.
from Calculator import Calculator
from tkinter import *
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyCalculator = Calculator()
    MyCalculator.LoadDll()
    MyCalculator.InitKinematic( 3 )
    MyCalculator.ConfigParameter()
    MyCalculator.ForwardKinematic()
    MyCalculator.InverseKinematic()

    window = Tk()
    # add widgets here

    window.title('Hello Python')
    window.geometry("300x200+10+20")
    window.mainloop()

    a = np.array([1, 2, 3, 4])
    print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
