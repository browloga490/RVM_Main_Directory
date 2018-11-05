##import matplotlib as mpl
##mpl.use('TkAgg')
##
##import scipy.fftpack
##import matplotlib.dates as dates
##import ast
##import datetime
import os 
##import csv
##import shutil
##import numpy as np
##import matplotlib.pyplot as plt
##from matplotlib.colors import LinearSegmentedColormap
##from matplotlib.colors import Colormap
##from mpl_toolkits.axes_grid1 import make_axes_locatable
##from mpl_toolkits.mplot3d import axes3d
##from matplotlib.pyplot import figure
#import graph_class
from graph_class import Graph_Frame
from graph_class import Graph

os.chdir(r"/usr/local/RVMD/Python_Scripts/Graph_Gen/GenCh0/")

# CONSTANTS
FILE_PREFIX = "data_store/"
LAST_FILE_NUM = 80 #This is set to 80 for now. Change to None when fully opertaional (it should work regardles though)
NEW_FILE = False

good = [['darkgreen','green'],['green','yellowgreen']]
satisfactory = [['yellowgreen','yellow'],['yellow','#FFD12A']]
unsatisfactory = [['#FFD12A','orange'],['orange','orangered']]
unacceptable = [['orangered','red'],['red']]
cbar = ['green','yellow','orange','red']


def colormap_builder(steps_each,colors,multiplier):
    seg = 1/len(colors)
    steps = seg/steps_each
    temp = [(0, colors[0])]

    for i in range(0,len(colors)):
        for j in range(0,steps_each):
            temp.append((round(j*steps,12), colors[i]))

    temp[-1] = (1, colors[-1])

    return LinearSegmentedColormap.from_list("", temp,N=256)


def graph_grad(ISO,g_cmap,s_cmap,uns_cmap,una_cmap,axis,x_lim,y_lim):

    g_extent = [[0,x_lim,0,0.04],[0,x_lim,0.04,0.07]]
    s_extent = [[0,x_lim,0.07,0.13],[0,x_lim,0.13,0.18]]
    uns_extent = [[0,x_lim,0.18,0.315],[0,x_lim,0.315,0.44]]
    una_extent = [[0,x_lim,0.44,0.45],[0,x_lim,0.45,y_lim]]

    xv, yv = np.meshgrid(np.linspace(0,0.4,x_lim+1), np.linspace(0,0.4,x_lim+1))
    zv = yv

    axis.imshow(zv, cmap=g_cmap[0], interpolation='nearest', origin='lower', extent=g_extent[0], aspect='auto')
    axis.imshow(zv, cmap=g_cmap[1], interpolation='nearest', origin='lower', extent=g_extent[1], aspect='auto')

    axis.imshow(zv, cmap=s_cmap[0], interpolation='nearest', origin='lower', extent=s_extent[0], aspect='auto')
    axis.imshow(zv, cmap=s_cmap[1], interpolation='nearest', origin='lower', extent=s_extent[1], aspect='auto')

    axis.imshow(zv, cmap=uns_cmap[0], interpolation='nearest', origin='lower', extent=uns_extent[0], aspect='auto')
    axis.imshow(zv, cmap=uns_cmap[1], interpolation='nearest', origin='lower', extent=uns_extent[1], aspect='auto')

    axis.imshow(zv, cmap=una_cmap[0], interpolation='nearest', origin='lower', extent=una_extent[0], aspect='auto')
    axis.imshow(zv, cmap=una_cmap[1], interpolation='nearest', origin='lower', extent=una_extent[1], aspect='auto')

    

def prepend(filename, line):
    
    with open(filename, 'r+') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        next(csv_reader)
        content = file.read()
        file.seek(67, 0)
        file.write('\n' + line.rstrip('\r\n') + '\n' + content)
        file.close()


def file_search(): 
    
    file = open("storage.txt", 'r+') #Open file to grab list of filenames and next number
    filenames = ast.literal_eval(file.readline()) #Temporary storage of filenames
    
    new_filenames = os.listdir('new_data/')
    filenames.extend(new_filenames)

    #Store filenames 

    if len(new_filenames) > 0:
        
        for name in new_filenames:
            shutil.move('new_data/'+name, 'data_store/')
        
        file.truncate(0) 
        file.seek(0)
        file.write(str(filenames)+'\n')
        file.close()

    temp = filenames[-1]
    temp = temp.strip('measure')
    LAST_FILE_NUM = int(temp.strip('.txt'))

    return new_filenames


def get_data(filenames):
    
    rmsgs = []
    pkpks = []
    datetrack = []

    #iterate files and harvest data
    #'filenames' is the list of files being analyzed
    output_send = []

    if len(filenames) != 0:
        for filename in filenames:
            file = open(FILE_PREFIX + filename, 'r')

            file.readline()
            file.readline()
            gs =[]
            date_list = []
            x_axis = []

            rows = file.readlines()

            for row in rows:
                cols = row.split(",")
                count = 0

                for col in cols:
                    if count == 1:
                        gs.append(float(col)) #(word.strip()) is an alternative
                    elif count == 2:
                        date_list.append(col)
                    count += 1

            total = 0.0

            for g in gs:
                total += abs(g)

                max_gs = max(gs)
                min_gs = min(gs)
                pk = (max_gs - min_gs)

            pkpks.append(pk)
            rmsgs.append(total/len(rows))

            if date_list[0] != date_list[len(date_list)-1]: #checking if date is same throuhgout
                print('We have a problem')
            else:
                date = date_list[0] #make variable "date" the first entry in the date column
                datetrack.append(date[:6]+'20'+date[6:])
                #x_axis.extend(dates.datestr2num(date))
                # where date is '01/02/1991'
                
            file.close()

        for i in range(len(rmsgs)):
            prepend('master_mem.txt',"{}, {}, {}".format(rmsgs[i], pkpks[i], datetrack[i]))

    return datetrack


def build_average_graph(scope, m_class):
    
    now = datetime.date.today()
    
    last_date = now - datetime.timedelta(days=scope)
    
    file = open('master_mem.txt', 'r')
    csv_reader = csv.reader(file)
    next(csv_reader)
    next(csv_reader)
    temp = next(csv_reader)
    
    dayrmsn = []    
    daypkpkn = []
    dates = []
    plotr = []
    plotp = []

    fig = plt.figure(facecolor='#151515',figsize=(10,5))
    ax1 = fig.add_subplot(111)

    dayrmsn.append(temp[0])
    daypkpkn.append(temp[1])
    dates.append(temp[2].strip()) #will append temp[7] on CentOS machines

    for row in csv_reader:

        if row[2].strip() == "END":
            r = np.mean([float(i) for i in dayrmsn])
            p = np.mean([float(i) for i in daypkpkn])

            plotr.append(r)
            plotp.append(p)
            
            final = datetime.datetime.strptime(dates[-1], '%m-%d-%Y').date()
            
            for i in range(0, scope - len(dates)):
                plotr.append(0.0)
                plotp.append(0.0)
                
                date = final - datetime.timedelta(days=i) #Change final to first value found (maybe dates[0]?)

                dates.append('{:02d}'.format(date.month) + '-' + '{:02d}'.format(date.day) + '-' + str(date.year))
        else:
            
            date = datetime.datetime.strptime(row[2].strip(), '%m-%d-%Y').date()

            if date >= last_date:
            
                if date == datetime.datetime.strptime(dates[-1], '%m-%d-%Y').date():
                    
                    dayrmsn.append(row[0])  #Adding contents of row[0] to a list of Strings
                    daypkpkn.append(row[1])
                    
                else:
                    r = np.mean([float(i) for i in dayrmsn]) 
                    p = np.mean([float(i) for i in daypkpkn])

                    plotr.append(r)
                    plotp.append(p)

                    dayrmsn = [row[0]]    
                    daypkpkn = [row[1]]

                    #print(date)

                    dates.append('{:02d}'.format(date.month) + '-' + '{:02d}'.format(date.day) + '-' + str(date.year))

            else:
                r = np.mean([float(i) for i in dayrmsn]) 
                p = np.mean([float(i) for i in daypkpkn])

                plotr.append(r)
                plotp.append(p)

                dayrmsn = [row[0]]    
                daypkpkn = [row[1]]
                
                break
                
                
                


    file.close()
    plotr = list(reversed(plotr))
    plotp = list(reversed(plotp))
    dates = list(reversed(dates))
    
    plotr = np.array(list(reversed(plotr)))
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)

    ax1.grid(True, color='w', linestyle=':', linewidth=0.5)

    print(len(dates)-scope)

    if scope == 7:
        graph_grad(10816,g_cmap,s_cmap,uns_cmap,una_cmap,ax1,len(dates)-1,max(plotp))
    else:
        graph_grad(10816,g_cmap,s_cmap,uns_cmap,una_cmap,ax1,len(dates)-2,max(plotp))
    
    ax1.fill_between(dates, plotp, 5, color='#151515')

    
    #ax1.plot(dates, plotr, linewidth=2.2, color='k')#, label='Average Vibration Level')      # '#8B0000'
    ax1.plot(dates, plotp, linewidth=2.5, color='k')#, label='Pk to Pk Vibration')               #'#259ae1'

    ax1.xaxis.label.set_color('w')
    ax1.yaxis.label.set_color('w')
    ax1.spines['bottom'].set_color('grey')
    ax1.spines['top'].set_color('grey')
    ax1.spines['left'].set_color('#151515')
    ax1.spines['right'].set_color('#151515')

    ax1.tick_params(axis='y', colors='w')
    ax1.tick_params(axis='x', colors='w')

    ax = plt.gca()
    ax.set_ylim([0, 1.2*max(plotp)])
    ax.set_facecolor('#151515')
    ax.tick_params(direction='out', length=6, width=2, colors='w', grid_alpha=0.9,labelsize='large')
    plt.tight_layout()

    if scope == 31:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/2))
    elif scope == 93:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/7))
    elif scope ==186:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/7))
    
    #x_ticks = np.append(ax.get_xticks(), dates[-1])
    #ax.set_xticks(x_ticks)

    ##WORK ON GETTING THE LAST TICK TO SHOW##

    plt.subplots_adjust(left=0.09, bottom=0.14, right=0.94, top=0.94, wspace=2.0, hspace=0)

    plt.xlabel('Date',size='xx-large',weight='bold',labelpad=10)
    plt.ylabel('Velocity (in/s)',size='xx-large',weight='bold',labelpad=10)
    plt.title('Machine Health Monitor', color='w',size='xx-large',weight='bold')

    ###COLORBAR START###

    divider = make_axes_locatable(ax1)
    cax = divider.append_axes("right", size="5%", pad=0.5)
    cax.set_ylim([0, 1.2*max(plotp)])

    cbar_cmap = LinearSegmentedColormap.from_list("", cbar,N=256)

    cb1 = mpl.colorbar.ColorbarBase(cax, ticks=[0.01,0.33,0.66,0.99], cmap=cbar_cmap, orientation='vertical')
    cb1.ax.set_yticklabels(['Good','Satisfactory','Unsatisfactory','Unacceptable'],size='large')
    cb1.ax.yaxis.set_tick_params(color='white')

    plt.setp(plt.getp(cb1.ax.axes, 'yticklabels'), color='white', weight='bold')

    ###COLORBAR END###

    plt.setp(ax1.get_xticklabels(),weight='bold')
    plt.setp(ax1.get_yticklabels(),weight='bold')
    
    plt.tight_layout()
    plt.savefig('C1_PKPK_'+str(scope)+'.png',facecolor='k',dpi=200)#'#151515')
    #plt.show()

def build_2_graph(scope, m_class):    #Find a way to incorporate the scope into the name of the graph image
    
    now = datetime.date.today()
    
    last_date = now - datetime.timedelta(days=scope)
    
    file = open('master_mem.txt', 'r')
    csv_reader = csv.reader(file)
    next(csv_reader)
    next(csv_reader)
    temp = next(csv_reader)
    
    some_value_2 = []    
    dates = []
    plot = []

    fig = plt.figure(facecolor='#151515',figsize=(10,5))
    ax1 = fig.add_subplot(111)

    some_value_2.append(temp[2])
    dates.append(temp[7].strip())

    for row in csv_reader:

        if row[2].strip() == "END":
            r = np.mean([float(i) for i in some_value_2])

            plot.append(r)
            
            final = datetime.datetime.strptime(dates[-1], '%m-%d-%Y').date()
            
            for i in range(0, scope - len(dates)):
                plot.append(0.0)
                
                date = final - datetime.timedelta(days=i) #Change final to first value found (maybe dates[0]?)

                #Find a way to prepend new dates to the 'dates' list
                dates.append('{:02d}'.format(date.month) + '-' + '{:02d}'.format(date.day) + '-' + str(date.year))
        else:
            
            date = datetime.datetime.strptime(row[2].strip(), '%m-%d-%Y').date()

            if date >= last_date:
            
                if date == datetime.datetime.strptime(dates[-1], '%m-%d-%Y').date():
                    
                    some_value_2.append(row[2])  #Adding contents of row[2] to a list of Strings
                    
                else:
                    r = np.mean([float(i) for i in some_value_2]) 

                    plot.append(r)

                    some_value_2 = [row[2]]    
                    
                    dates.append('{:02d}'.format(date.month) + '-' + '{:02d}'.format(date.day) + '-' + str(date.year))

            else:
                r = np.mean([float(i) for i in some_value_2])

                plot.append(r)

                some_value_2 = [row[2]]    
                daypkpkn = [row[1]]
                
                break
                
                
                


    file.close()
    plotr = list(reversed(plotr))
    plotp = list(reversed(plotp))
    dates = list(reversed(dates))
                
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)

    ax1.grid(True, color='w', linestyle=':', linewidth=0.5)
    
    ax1.fill_between(dates, plotp, 0, facecolor='b', edgecolor='w')

    ax1.plot(dates, plotp, linewidth=1, color='w')#, label='Pk to Pk Vibration')               #'#259ae1'

    ax1.xaxis.label.set_color('w')
    ax1.yaxis.label.set_color('w')
    ax1.spines['bottom'].set_color('grey')
    ax1.spines['top'].set_color('grey')
    ax1.spines['left'].set_color('#151515')
    ax1.spines['right'].set_color('#151515')

    ax1.tick_params(axis='y', colors='w')
    ax1.tick_params(axis='x', colors='w')

    ax = plt.gca()
    ax.set_ylim([0, 1.2*max(plotp)])
    ax.set_facecolor('#151515')
    ax.tick_params(direction='out', length=6, width=2, colors='w', grid_alpha=0.9,labelsize='large')
    plt.tight_layout()

    if scope == 31:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/2))
    elif scope == 93:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/7))
    elif scope ==186:
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(dates)/7))

    plt.subplots_adjust(left=0.09, bottom=0.14, right=0.94, top=0.94, wspace=2.0, hspace=0)

    plt.xlabel('Date',size='xx-large',weight='bold',labelpad=10)
    plt.ylabel('Velocity (in/s)',size='xx-large',weight='bold',labelpad=10)
    plt.title('Bearing Health Monitor', color='w',size='xx-large',weight='bold')

    plt.setp(ax1.get_xticklabels(),weight='bold')
    plt.setp(ax1.get_yticklabels(),weight='bold')
    
    plt.tight_layout()
    plt.savefig('C1_BEAR_'+str(scope)+'.jpg',facecolor='k',dpi=200)#'#151515')
    #plt.show()

##def build_fft_graph(filenames,N,T):
##
##    sec = []
##    gs = []
##    file_list = []
##    
##    file = open('storage.txt', 'r+')
##    csv_reader = csv.reader(file)
##    next(csv_reader)
##    file.close()
##
##    if len(filenames) >= 10:
##        file_list = filenames[-10:]
##
##    else:
##        file_list = filenames
##
##    ##START FOR LOOP##
##
##    file = open(FILE_PREFIX + 'measure80.txt')#'50HzTXT.txt')
##    file.readline()
##    file.readline()
##
##    rows = file.readlines()
##
##    for row in rows:
##        cols = row.split(",")
##        count = 0
##
##        for col in cols:
##            if count == 0:
##                sec.append(float(col)) #(word.strip()) is an alternative
##            elif count == 1:
##                gs.append(float(col))
##                break
##            count += 1
##
##    
##
##    XYZ_list = [] #Consider storing a copy of this list in the storage.txt folder (oh and you've got this :-)
##    
##    x = sec
##    y = gs
##    yf = scipy.fftpack.fft(y)
##    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
##
##    temp = [4]*24
##
##    yn = np.array(temp) 
##    zn = 2.0/N * np.abs(yf[:N//2])
##
##    fig = plt.figure()
##    ax = fig.add_subplot(111, projection='3d')
##    
##    ax.plot(xf,yn,zn)
##
##    ##END FOR LOOP##
##
##    ax.set_xlabel('x axis')
##    ax.set_ylabel('y axis')
##    ax.set_zlabel('z axis')
##
##    plt.tight_layout()
##    plt.show(fig)




#START OF PROGRAM#

#filenames = file_search()

#filedates = list(set(get_data(filenames)))

##g_cmap = [colormap_builder(1,good[0],0),colormap_builder(1,good[1],1)]
##s_cmap = [colormap_builder(1,satisfactory[0],2),colormap_builder(1,satisfactory[1],3)]
##uns_cmap = [colormap_builder(1,unsatisfactory[0],4),colormap_builder(1,unsatisfactory[1],5)]
##una_cmap = [colormap_builder(1,unacceptable[0],6),colormap_builder(1,unacceptable[1],7)]
##
##build_average_graph(7, 1)
##build_average_graph(31, 1)
##build_average_graph(93, 1)
##build_average_graph(186, 1)
##build_bearing_graph(7, 1)


#build_fft_graph(filenames,48,1/500)
#print(cbar)

frame = Graph_Frame(r'/usr/local/RVMD/GUI/Ch3_Graphs/')

#graph_X = Graph(ID, *kwargs)

graph_1 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_2 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_3 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_4 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)

graph_5 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_6 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_7 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_8 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')

graph_9 = Graph('Ch3_MISA',fill_color='honeydew')
graph_10 = Graph('Ch3_MISA',fill_color='honeydew')
graph_11 = Graph('Ch3_MISA',fill_color='honeydew')
graph_12 = Graph('Ch3_MISA',fill_color='honeydew')

graph_13 = Graph('Ch3_BEAR',fill_color='limegreen')
graph_14 = Graph('Ch3_BEAR',fill_color='limegreen')
graph_15 = Graph('Ch3_BEAR',fill_color='limegreen')
graph_16 = Graph('Ch3_BEAR',fill_color='limegreen')

graph_17 = Graph('Ch3_GEARS',fill_color='plum')
graph_18 = Graph('Ch3_GEARS',fill_color='plum')
graph_19 = Graph('Ch3_GEARS',fill_color='plum')
graph_20 = Graph('Ch3_GEARS',fill_color='plum')

graph_21 = Graph('Ch3_OTHER',fill_color='thistle')
graph_22 = Graph('Ch3_OTHER',fill_color='thistle')
graph_23 = Graph('Ch3_OTHER',fill_color='thistle')
graph_24 = Graph('Ch3_OTHER',fill_color='thistle')

graph_1.read_file('master_mem.txt',1,7,7)
graph_2.read_file('master_mem.txt',1,7,31)
graph_3.read_file('master_mem.txt',1,7,93)
graph_4.read_file('master_mem.txt',1,7,186)

graph_5.read_file('master_mem.txt',2,7,7)
graph_6.read_file('master_mem.txt',2,7,31)
graph_7.read_file('master_mem.txt',2,7,93)
graph_8.read_file('master_mem.txt',2,7,186)

graph_9.read_file('master_mem.txt',3,7,7)
graph_10.read_file('master_mem.txt',3,7,31)
graph_11.read_file('master_mem.txt',3,7,93)
graph_12.read_file('master_mem.txt',3,7,186)

graph_13.read_file('master_mem.txt',4,7,7)
graph_14.read_file('master_mem.txt',4,7,31)
graph_15.read_file('master_mem.txt',4,7,93)
graph_16.read_file('master_mem.txt',4,7,186)

graph_17.read_file('master_mem.txt',5,7,7)
graph_18.read_file('master_mem.txt',5,7,31)
graph_19.read_file('master_mem.txt',5,7,93)
graph_20.read_file('master_mem.txt',5,7,186)

graph_21.read_file('master_mem.txt',6,7,7)
graph_22.read_file('master_mem.txt',6,7,31)
graph_23.read_file('master_mem.txt',6,7,93)
graph_24.read_file('master_mem.txt',6,7,186)

#print(graph_1.x_axis)
#print(graph_1.y_axis)

frame.add_graph(graph_1)
frame.add_graph(graph_2)
frame.add_graph(graph_3)
frame.add_graph(graph_4)
frame.add_graph(graph_5)
frame.add_graph(graph_6)
frame.add_graph(graph_7)
frame.add_graph(graph_8)
frame.add_graph(graph_9)
frame.add_graph(graph_10)
frame.add_graph(graph_11)
frame.add_graph(graph_12)
frame.add_graph(graph_13)
frame.add_graph(graph_14)
frame.add_graph(graph_15)
frame.add_graph(graph_16)
frame.add_graph(graph_17)
frame.add_graph(graph_18)
frame.add_graph(graph_19)
frame.add_graph(graph_20)
frame.add_graph(graph_21)
frame.add_graph(graph_22)
frame.add_graph(graph_23)
frame.add_graph(graph_24)

frame.build_colormaps()
frame.build_graphs()

#END OF PROGRAM#









