import pandas as pd
'''
This File takes NOAA GLOBAL HOURLY data in the form of CSV and cleans
certain columns of data. The Data is often represented with compound
formats like data_we_care_about,QualityCodes,OtherJunk,Data_WeCareAbout.
The data is also scaled so that decimals are avoided, so isolation
and manipulation are required. This will work with any data that can be
downloaded from the HOURLY GLOBAL from here

https://gis.ncdc.noaa.gov/maps/ncei/cdo/hourly

'''

file_names = [
    'Ashville Airport NC.csv',
    'Bogor ID.csv',
    'BURLINGTON CARSON AIRPORT CO US.csv',
    'Cairo INTL.csv',
    'Darwin INTL AS.csv',
    'Fedorova RS.csv',
    'Grasslands ZI.csv',
    'NAgasaki JA.csv',
    'NikosKazantzakis GR.csv',
    'Odessa INTNL UP.csv',
    'Robert Gabriel Mugabe International Harare ZI.csv',
    'Talagi RS.csv',
    'Unzendaka JA.csv',
]


def clean_wind_speed(filename):
    """
    This Method Takes in a CSV file from the GLOBAL HOURLY Dataset from NOAA.
    It then converts it into a Pandas Dataframe, to make manipulation of
    row.column data easier.

    :param filename:
    """
    av = pd.read_csv(filename)
    newData = []
    if av['WND'].dtypes == 'object':
        if 'WND' in av:
            print("Cleaning WND", filename)
            for row in av['WND']:
                data = row[8:12]
                if data == '0000':
                    newData.append('NaN')
                else:
                    newData.append(float(data) / 10.0)

            x = newData
            av.WND = x
            av.to_csv(filename)
    else:
        pass


def clean_temp(filename):
    """
        This Method Takes in a CSV file from the GLOBAL HOURLY Dataset from NOAA.
        It then converts it into a Pandas Dataframe, to make manipulation of
        row.column data easier.

        Temperature is in Celsius

        :param filename:
        """
    print("Cleaning Temperature", filename)
    av = pd.read_csv(filename)
    newData = []
    if av['TMP'].dtypes == 'object':
        for row in av['TMP']:
            data = row[1:5]
            sign = row[0]
            if data == '9999':
                newData.append('NaN')
            elif sign == '+':
                newData.append(float(data) / 10.0)
            elif sign == '-':
                newData.append(-1 * (float(data) / 10.0))
        x = newData
        av.TMP = x
        av.to_csv(filename)
    else:
        pass


def clean_dew(filename):
    """
        This Method Takes in a CSV file from the GLOBAL HOURLY Dataset from NOAA.
        It then converts it into a Pandas Dataframe, to make manipulation of
        row.column data easier.

        The temperature to which a given parcel of air must be cooled at constant pressure and water vapor
        content in order for saturation to occur.
         MIN: -0982 MAX: +0368 UNITS: Degrees Celsius

        :param filename:
        """
    print("Cleaning Dew", filename)
    av = pd.read_csv(filename)
    newData = []
    if av['DEW'].dtypes == 'object':
        for row in av['DEW']:
            data = row[1:5]
            sign = row[0]
            if data == '9999':
                newData.append('NaN')
            elif sign == '+':
                newData.append(float(data) / 10.0)
            elif sign == '-':
                newData.append(-1 * (float(data) / 10.0))
        x = newData
        av.DEW = x
        av.to_csv(filename)
    else:
        pass


def clean_slp(filename):
    """
        This Method Takes in a CSV file from the GLOBAL HOURLY Dataset from NOAA.
        It then converts it into a Pandas Dataframe, to make manipulation of
        row.column data easier.

        The average pressure at the observed point for the day derived computationally from other QC’ed elements
        MIN: 04500 MAX: 10900 UNITS: hectopascals

        :param filename:
        """
    av = pd.read_csv(filename)
    newData = []
    if av['SLP'].dtypes == 'object':
        if 'SLP' in av:
            print("Cleaning SLP", filename)
            for row in av['SLP']:
                data = row[0:5]
                if data == '9999':
                    newData.append('NaN')
                else:
                    newData.append(float(data) / 10.0)

            x = newData
            av.SLP = x
            av.to_csv(filename)
    else:
        pass


def clean_precip(filename):
    """
        This Method Takes in a CSV file from the GLOBAL HOURLY Dataset from NOAA.
        It then converts it into a Pandas Dataframe, to make manipulation of
        row.column data easier.

        The depth of LIQUID-PRECIPITATION that is measured at the time of an observation.
        MIN: 0000 MAX: 9998 UNITS: millimeters

        :param filename:
        """
    print("Cleaning Precipitation", filename)
    av = pd.read_csv(filename)
    location = av.columns.get_loc('AA1')
    twentyFour_precip = []
    eighteen_precip = []
    fifteen_precip = []
    twelve_precip = []
    nine_precip = []
    seven_precip = []
    six_precip = []
    three_precip = []
    one_precip = []
    for row in av['AA1']:
        if pd.isna(row):
            twentyFour_precip.append(float('nan'))
            eighteen_precip.append(float('nan'))
            fifteen_precip.append(float('nan'))
            twelve_precip.append(float('nan'))
            nine_precip.append(float('nan'))
            seven_precip.append(float('nan'))
            six_precip.append(float('nan'))
            three_precip.append(float('nan'))
            one_precip.append(float('nan'))
        else:
            hour = row[:2]
            precip = row[3:7]
            if hour == '24':
                twentyFour_precip.append(float(float(precip) / 10.0))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '18':
                eighteen_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))


            elif hour == '15':
                fifteen_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '12':
                twelve_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '09':
                nine_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '07':
                seven_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '06':
                six_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                three_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '03':
                three_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                one_precip.append(float('nan'))

            elif hour == '01':
                one_precip.append(float(float(precip) / 10.0))
                twentyFour_precip.append(float('nan'))
                eighteen_precip.append(float('nan'))
                fifteen_precip.append(float('nan'))
                twelve_precip.append(float('nan'))
                nine_precip.append(float('nan'))
                seven_precip.append(float('nan'))
                six_precip.append(float('nan'))
                three_precip.append(float('nan'))

    if '24_PCP' in av:
        av['24_PCP'] = twentyFour_precip
    else:
        av.insert(location, '24_PCP', twentyFour_precip)

    if '18_PCP' in av:
        av['18_PCP'] = eighteen_precip
    else:
        av.insert(location, '18_PCP', eighteen_precip)

    if '15_PCP' in av:
        av['15_PCP'] = fifteen_precip
    else:
        av.insert(location, '15_PCP', fifteen_precip)

    if '12_PCP' in av:
        av['12_PCP'] = twelve_precip
    else:
        av.insert(location, '12_PCP', twelve_precip)

    if '09_PCP' in av:
        av['09_PCP'] = nine_precip
    else:
        av.insert(location, '09_PCP', nine_precip)

    if '07_PCP' in av:
        av['07_PCP'] = seven_precip
    else:
        av.insert(location, '07_PCP', seven_precip)

    if '06_PCP' in av:
        av['06_PCP'] = six_precip
    else:
        av.insert(location, '06_PCP', six_precip)

    if '03_PCP' in av:
        av['03_PCP'] = three_precip
    else:
        av.insert(location, '03_PCP', three_precip)

    if '01_PCP' in av:
        av['01_PCP'] = one_precip
    else:
        av.insert(location, '01_PCP', one_precip)
    av.to_csv(filename)


for file in file_names:
    clean_temp(file)
    clean_dew(file)
    clean_slp(file)
    clean_precip(file)
    clean_wind_speed(file)
