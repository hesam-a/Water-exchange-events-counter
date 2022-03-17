import re, sys
from itertools import islice

with open(sys.argv[1], 'r') as f:
    
    g = open("exchange_counter.txt", 'a')
    idx_lines = ''
    nframes = ''
    water_idx_list = []

    g.write("water idx, number of MD frames the water was available in a row"+'\n')
    g.write('\n')

    for line in f:
        if "Number of frames" in line:
            nframes = int(line.split()[-1])
        elif "Index of Oxygen" in line:
            idx_lines= ''.join(islice(f,nframes))

    idx_lines = idx_lines.split("\n")

    for count,line in enumerate(idx_lines):

        # current frame
        #curnt = re.split(r'[: \[ \] , \"\']' ,idx_lines[count].strip())
        curnt = re.split(r' ',idx_lines[count].strip())
        curnt = list(filter(None,curnt))

        # previous frame
        #prev = re.split(r'[: \[ \] , \"\']' ,idx_lines[(count-1)].strip())
        prev = re.split(r' ',idx_lines[(count-1)].strip())
        prev = list(filter(None,prev))

        # next frame
        #nxt = re.split(r'[: \[ \] , \"\']' ,idx_lines[(count+1)].strip())
        nxt = re.split(r' ',idx_lines[(count+1)].strip())
        nxt = list(filter(None,nxt))
#        print("current:  ",curnt)
#        print("previous: ",prev)
#        print("next:     ",nxt)

        for j in curnt:
            if j not in water_idx_list:
                water_idx_list.append(j)

        # for avoiding bug in nxt
        if line == idx_lines[-2]:
            break
        else:
            # loop over water indices 
            for wat in curnt:
                index_counter=0

                # check if the water index is repeating over the next frames 
                for i in idx_lines[count:]:
                    # count in if the water is in the current frame
                    if wat in i:
                        index_counter += 1
                    # break if water was in the previous and next frames 
                    elif wat in prev and nxt:
                        #print(wat, "was in previous and next frame")
                        break
                    # if not in the current frame
                    elif wat not in i:
                        g.write("{:>10}".format(wat)+'   '+str("{:>10}".format(index_counter))+'\n')
                        #print(wat, index_counter)
                        break
    g.write("Number of unique indices: "+str(len(water_idx_list)))
g.close()
f.close()
