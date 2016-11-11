
import matplotlib.pyplot as plt


def plotData(crimes, categories):

    hist = []
    for cat in categories:
        for day in range(0,7):
            hist.append(0)
            x = []
            y = []
            h = 0            
            for c in crimes:
                if( cat == c.call_group and c.occ_weekday == day):
                    x.append( c.x_coordinate )
                    y.append( c.y_coordinate )
                    h = h+1
            print day, h
            hist.append(h)
            print cat, day, len(x)
            plt.plot(x,y,'r.', alpha = 0.05)
            plt.axis([7610000, 7700000, 650000, 730000])
            plt.show(block = True)
        plt.hist(hist)
        plt.show( block=True )
        raw_input()
        

