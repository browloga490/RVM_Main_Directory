from numpy import isclose
import numpy as np
from detect_peaks import*
import matplotlib
from scipy.signal import savgol_filter
from ampd import find_peaks_ampd

##def build_list(rpm_value,upper_bound):
##    ''' This function will return a list of tuples that contain a
##        lower and upper bound of each of the rpm's multiples.'''
##
##    temp = [(rpm_value-1,rpm_value+1)] #Creates a list with the first value being a tuple - (the rpm - 1, the rpm + 1). This will
##                                       #act as the first set of ranges
##    
##    multiplier = 2  #The value that the rpm will be multiplied by
##    
##    next_val = rpm_value*multiplier #The value of the next rpm multiple
##
##    while next_val < upper_bound: #This loop will continue to execute as long as the next rpm value is less than the upper bound
##        temp.append((next_val-1,next_val+1)) #Appends a tupple containing
##        multiplier += 1
##        next_val = rpm_value*multiplier
##
##    return temp
##
#peaks = [16.9, 21.53, 22.23, 27.34, 34.06, 36.52, 42.32, 43.86, 45.02, 46.31] #List of recorded peaks

fft = np.loadtxt(r'/home/udoo/Documents/FFT_grab.txt')

#rpm_range = [0.742971,3.9434,1.07768,3.10719,8.17209,6.15402]

#rpm_range = [16.9, 21.53, 22.23, 27.34, 34.06] #List of recorded peaks that fall within the set rpm range
##
##def test_1():
##    n_peaks = []
##
##    for i in range(0,len(rpm_range)):
##        n_peaks.append([])
##        for j in range(0,len(peaks)):
##            if peaks[j]/rpm_range[i] < 1:
##                n_peaks[i].append(0)
##            else:
##                n_peaks[i].append(round(peaks[j]/rpm_range[i],1))
##
##    print('<TEST 1>')
##    for i in n_peaks:
##        print(i)
##
##
##
##def test_2():
##    n_peaks = []
##    count_list = [] #Will store the list of count values for each rpm value test
##    
##    for i in range(0,len(rpm_range)):
##        n_peaks.append([])
##        max_mult = int(upper_bound/rpm_range[i])
##        count = 0
##        
##        for j in range(0,len(peaks)):
##            
##            if peaks[j]/rpm_range[i] <= 1:
##                n_peaks[i].append(0)
##                
##            elif peaks[j]/rpm_range[i] <= max_mult:
##                n_peaks[i].append(round(peaks[j]/rpm_range[i],5))
##                count += 1
##                
##        count_list.append(count)
##
##    print('\n<TEST 2>')
##    for i in n_peaks:
##        print(i)
##
##    print(count_list)

def test_3(fft,min_rpm,max_rpm,mph,rms):
  
    filtered_fft = savgol_filter(fft,3,1)
    
    check = filtered_fft[min_rpm:max_rpm+1]
    
    #return filtered_fft
    
    peaks = detect_peaks(filtered_fft, mph=mph, mpd=3, show=False)
    rpm_peaks = detect_peaks(check, mph=mph, mpd=3, show=False)#find_peaks_ampd(filtered_fft, 200)[0]
    
    n_peaks = []
    count_list = [] #Will store the list of RPM, amplitude, count, and scale values for each rpm value test
    scale_sort_list = [] #Will store the list of RPM, amplitude, count, and scale values that will be sorted by the scale value
    output = []
    upper_bound = 50
    rpm_range = []
    
    AF = 20
    WF = 10
    
    for i in rpm_peaks:
        rpm_range.append(i+min_rpm)
    
    
    if len(peaks) == 0:
        return [30]
    
    if len(rpm_range) == 1:
        return [rpm_range[0]]
    
    for i in range(0,len(rpm_range)):
        n_peaks.append([])
        max_mult = int(upper_bound/rpm_range[i])
        count = 0
        for j in range(0,len(peaks)):
            
            if peaks[j]/rpm_range[i] <= 1:
                n_peaks[i].append(0)
                
            elif peaks[j]/rpm_range[i] <= max_mult:
                if isclose(round(peaks[j]/rpm_range[i],0), peaks[j]/rpm_range[i], 1):
                    n_peaks[i].append(round(peaks[j]/rpm_range[i],5))
                    count += 1

        count_list.append((rpm_range[i],filtered_fft[rpm_range[i]],count, AF*filtered_fft[rpm_range[i]]/rms + WF/rpm_range[i]))

    count_list.sort(key=lambda tup: tup[2], reverse=True)
    
    if len(count_list) < 5:
        scale_sort_list = count_list
        #return scale_sort_list

    else:
        scale_sort_list = count_list[0:5]

    scale_sort_list.sort(key=lambda tup: tup[3], reverse=True)

    print(count_list)
    
    if len(scale_sort_list) > 1:
        if scale_sort_list[0][3] == scale_sort_list[1][3]:
            scale_sort_list.sort(key=lambda tup: tup[2], reverse=True)
    
    for i in scale_sort_list:
        output.append(i[0])
        

    return output

    #return top 5 rpm values


 #The highest frequency value that we will be looking at in terms of our peaks

#data = [] #List of desired information (display data that may be interesting)




#test_1()
#test_2()
#print(test_3(fft))
#y = savgol_filter(fft,3,1)
#detect_peaks(y, mph=0, mpd=3, show=True)




##for i in rpm_range: #Iterates through the list of possible rpm values
##
##    count = 0 #Sets the number of peaks that were matched to one of the rpm's multiple to 0
##
##    temp = build_list(i,upper_bound) #
##    
##    for j in temp:
##        for k in peaks:
##            if j[0] <= k and j[1] >= k:
##                count += 1
##                data.append((i,(j[0]+1)/i,k))
##                break
##
##    count_list.append(count)
##
##print(count_list)



