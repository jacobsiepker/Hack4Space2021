#HACK4SPACE2021
#DePaulUniversity
#Jacob Siepker
#NASA File Parser

import os

def main():
    print("Working on it!")
    td = [None, None]
    #as [Date, TimeUTC]

    Foutput = open("Data_parsed.csv","w+")

    path = os.path.abspath('NASAParser.py')[:-13] + 'data'


    for subdirectories, directories, files in os.walk(path):
        for file in files:

            #for each .TAB file
            Fdata = open(path+'\\'+file, "r")
            print("Working On " + path+'\\'+file)
            FdataLines = Fdata.readlines()
            for line in FdataLines:
                Foutput.write(parse(line, td))


    Foutput.close()
    print("All Done!")

##################################

def parse(line, td):
    line = line.replace(' ','')
    line = line.replace('\t','')
    #print(line)
    
    #IF Time/Date line
    if line[:3] == "0,\"":
        line = line.replace("\"", "")
        TdAry = line.split(',')
        td[0] = TdAry[1]
        td[1] = TdAry[2]
        
        return ''

    #IF Data Line
    elif line[:2] == "0,":
        lineOut = ''
        line = line.replace("\"", "")
        DataAry = line.split(',')

        if (td[0] == None or td[1] == None or DataAry[13]=='-9999' or DataAry[14]=='-9999' or DataAry[4]=='-9999' or DataAry[5]=='-9999'):
            return ''

        lineOut+= (td[0].replace(",","") + ",")
        lineOut+= (td[1].replace(",","") + ",")
        lineOut+= (DataAry[13].replace(",","") + ",")
        lineOut+= (DataAry[14].replace("\n","") + ",")
        lineOut+= (DataAry[4].replace(",","") + ",")
        lineOut+= (DataAry[5].replace(",","") + ",")
        lineOut+= (DataAry[8].replace(",","") + ",")
        lineOut+= (DataAry[9].replace(",",""))
        lineOut+= "\n"
        
        return lineOut
        

    else:
        return ''
        


#1,          Date,            UTC,           SCLK,       L_s,    Solar_dist, Orb_num, Gqual, Solar_lat, Solar_lon,  Solar_zen,     LTST, Profile_lat, Profile_lon, Profile_rad, Profile_alt,   Limb_ang,  Are_rad,  Surf_lat,   Surf_lon,  Surf_rad,   T_surf, T_surf_err, T_near_surf, T_near_surf_err, Dust_column, Dust_column_err,  H2Ovap_column,  H2Ovap_column_err,  H2Oice_column,  H2Oice_column_err,  CO2ice_column,  CO2ice_column_err,   p_surf,   p_surf_err, p_ret_alt,      p_ret, p_ret_err, Rqual, P_qual, T_qual, Dust_qual,  H2Ovap_qual,  H2Oice_qual,  CO2ice_qual, surf_qual,  Obs_qual,    Ref_SCLK_0,    Ref_SCLK_1,    Ref_SCLK_2,    Ref_SCLK_3,    Ref_SCLK_4,    Ref_SCLK_5,    Ref_SCLK_6,    Ref_SCLK_7,    Ref_SCLK_8,    Ref_SCLK_9,    Ref_Date_0,      Ref_UTC_0,    Ref_Date_1,      Ref_UTC_1,    Ref_Date_2,      Ref_UTC_2,    Ref_Date_3,      Ref_UTC_3,    Ref_Date_4,      Ref_UTC_4,    Ref_Date_5,      Ref_UTC_5,    Ref_Date_6,      Ref_UTC_6,    Ref_Date_7,      Ref_UTC_7,    Ref_Date_8,      Ref_UTC_8,    Ref_Date_9,      Ref_UTC_9
#0             1                2              3           4        5            6        7       8           9          10          11       12           13              14        15            16       17        ...

#1,         Pres,       T,   T_err,       Dust,   Dust_err,     H2Ovap, H2Ovap_err,     H2Oice, H2Oice_err,     CO2ice, CO2ice_err,     Alt,       Lat,       Lon
#0            1         2      3            4        5            6           7            8          9            10         11          12        13        14

#Output Lines contain
#Date, Time, Lat, Long, Dust, Dust_Err, H20ice, H20_iceErr


main()
