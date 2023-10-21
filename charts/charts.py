import matplotlib.pyplot as pylot

def generate_pie_chart ():
    labels = ['A','B','C']
    values = [100, 100, 300]

    fig, ax = pylot.subplots()
    ax.pie(values, labels = labels)

    pylot.savefig('pie.png')
    pylot.close()
