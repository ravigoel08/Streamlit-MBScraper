#creating CSV

def exportCsv(data: list):

     #external File
    outfile_name = 'data.csv'
    #CSV headers
    headers = 'Price, Area'
    f = open(outfile_name,'w')
    f.write(headers)
    
    for area, price in data:
        f.write("\n" + str(price) + ", " + str(area) )
    f.close()
