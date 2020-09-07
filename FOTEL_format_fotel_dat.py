import numpy as np
import os

# # exists = os.path.isfile('FOTEL/nugem.dat')
# # if exists:
# #     os.remove('FOTEL/nugem.dat')

#------------------------------------------------------------------------------------------------
# KOREL RVs
# mjd, RV1, RV2 = np.loadtxt('KOREL/4713+6678/korel.rv', skiprows=1, usecols=(1, 2, 4)  , unpack=True)

# with open('FOTEL/nugem_korel_RVs_HeI6678.dat', 'w') as file:
#     file.write('\n')
#     for i in range(len(mjd)):
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    1\n'.format(mjd[i], RV1[i], 1.0, 1))
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    2\n'.format(mjd[i], RV2[i], 1.0, 2))

        # file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    1\n'.format(jd[i]-2400000.5, rvHe[i], 1.0, 1))
        # file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    1\n'.format(jd[i]-2400000.5, rvSi[i], 1.0, 1))


#-------------------------------------------------------------------------------------------------
# RVs from rivi
# mjd, RV = np.loadtxt('FOTEL/RVs_rivi_email.dat', skiprows=2, unpack=True)
# mjd, rvHe, rvSi = np.loadtxt('FOTEL/RVs_rivi2006_He_Si.dat', skiprows=1, unpack=True)

# jd, rvHa, rvHe, rvSi = np.loadtxt('FOTEL/table2.dat', usecols=(0,6,7,8), unpack=True)

# with open('FOTEL/nugem_table2_Ha.dat', 'w') as file:
#     file.write('\n')
#     for i in range(len(jd)):
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    2\n'.format(jd[i]-2400000.5, rvHa[i], 1.0, 1))
# #         # file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    1\n'.format(jd[i]-2400000.5, rvHe[i], 1.0, 1))
# #         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}    1\n'.format(jd[i]-2400000.5, rvSi[i], 1.0, 1))


#------------------------------------------------------------------------------------------------
# # WDS astrometry
mjd, sep, PA, err_maj = np.loadtxt('astrometry/HD45542_WDS_tyler.txt', usecols=(1,2,3,4), unpack=True, skiprows=1)

with open('FOTEL/nugem.dat_astrometry_WDS', 'w') as file:
    for i in range(len(mjd)):

        file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   14\n'.format(mjd[i], sep[i]/1000, 1, 3))
        file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   15\n'.format(mjd[i], PA[i], 1, 4))

#-------------------------------------------------------------------------
# # MIRC INNER ORBIT
# mjd, sep, PA, err_maj = np.loadtxt('astrometry/HD45542_WDS_tyler.txt', usecols=(1,2,3,4), unpack=True, skiprows=1)

# with open('FOTEL/nugem_WDS_astrometry.dat', 'w') as file:
    # for i in range(len(mjd)):

    #     file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   14\n'.format(mjd[i], sep[i]/1000, 5/err_maj[i], 3))
    #     file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   15\n'.format(mjd[i], PA[i], 5/err_maj[i], 4))

#---------------------------------------------------------------------------------------------------------------
# # MIRC-X OUTER ORBIT

# mjd, sep, PA, sig_major, sig_minor, sig_PA = np.loadtxt('astrometry/HD_45542_inner.txt', skiprows=1, usecols=(1,2,3,4,5,6), unpack=True)

# with open('FOTEL/nugem_MIRC_inner_astrometry.dat', 'w') as file:
#     for i in range(len(mjd)):

#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   14\n'.format(mjd[i], sep[i], 1, 3))
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   15\n'.format(mjd[i], PA[i], 1, 4))

#---------------------------------------------------------------------------------------------------------------
# # MIRC-X OUTER ORBIT

mjd, rv = np.loadtxt('RVs/BeSS.fits.dat', skiprows=0, usecols=(0,1), unpack=True)

with open('FOTEL/nugem.dat_Ha_RVs_BeSS.dat', 'w') as file:

    file.write('\n')

    for i in range(len(mjd)):

        file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   {}\n'.format(mjd[i], rv[i], 0.5, 1, 2))


#---------------------------------------------------------------------------------------------------------------
# # WOBBLE orbit
# mjd, ra, dec, err_maj = np.loadtxt('astrometry/HD45542_wobble.txt', usecols=(0,1,2,3), unpack=True, skiprows=1)

# sep = np.sqrt(ra**2 + dec**2)
# #PA = np.arctan2(dec, ra) * 180 / np.pi
# PA = np.degrees(np.arctan2(ra, dec)) % 360.


# with open('FOTEL/nugem.dat_wobble_astrometry', 'w') as file:
#     file.write('\n')
#     for i in range(len(mjd)):
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   14\n'.format(mjd[i], sep[i]/1000, 1.0, 5)) # np.amin(err_maj)/err_maj[i]
#         file.write('{:10.4f} {:9.5f}     {:3.1f}      {}   15\n'.format(mjd[i], PA[i], 1.0, 6))


