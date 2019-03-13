import os
import time
from datetime import datetime, timedelta
from dateutil.parser import parse
import numpy as np

nemoinput = '/results2/SalishSea/nowcast-green.201806/'

def salishseacast_paths(timestart, timeend, path = nemoinput):
    """Generate paths for Salish Seacast forcing 

    :arg timestart: date from when to start concatenating
    :type string: :py:class:'str'

    :arg timeend: date at which to stop concatenating
    :type string: :py:class:'str'

    :arg path: path of input files
    :type string: :py:class:'str'

    :arg outpath: path for output files
    :type string: :py:class:'str'

    :arg compression_level: compression level for output file (Integer[1,9])
    :type integer: :py:class:'int'

    :returns tuple: two tuples containing the arguments to pass to hdf5 file generator functions
    :rtype: :py:class:`tuple'
    """
    
    # generate list of dates from daterange given
    daterange = [parse(t) for t in [timestart, timeend]]

    # append all filename strings within daterange to lists
    U_files = []
    for day in range(np.diff(daterange)[0].days):
        datestamp = daterange[0] + timedelta(days = day)
        datestr1 = datestamp.strftime('%d%b%y').lower()
        datestr2 = datestamp.strftime('%Y%m%d')
        
        # check if file exists. exit if it does not. add path to list if it does.

        # U files
        U_path = f'{path}{datestr1}/SalishSea_1h_{datestr2}_{datestr2}_carp_T.nc'
        if not os.path.exists(U_path):
            print(f'File {U_path} not found. Check Directory and/or Date Range.')
            return False
        U_files.append(U_path)

    print('\nAll source files found')
    print(U_files)
    return U_files

timestart = input('enter begin date:\n')
timeend = input('enter day after end date:\n')
salishseacast_paths(timestart, timeend, path = nemoinput)
