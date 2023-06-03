# ![https://nwp.dmi.govcloud.dk/dmi-hirlam/plots/](https://nwp.dmi.govcloud.dk/dmi-hirlam/plots/)

stations = {
'QAS_L':  '04401', 'QAS_U':  '04402',
'NUK_L':  '04403', 'TAS_L':  '04404',
'CEN':    '04407', 'TAS_A':  '04408',
'KAN_U':  '04409', 'KAN_M':  '04411',
'KAN_L':  '04412', 'SCO_L':  '04413',
'NAE':    '04420', 'SCO_U':  '04421',
'UPE_U':  '04422', 'UPE_L':  '04423',
'THU_L':  '04424', 'TUN':    '04425',
'KPC_U':  '04427', 'KPC_L':  '04428',
'LYN_T':  '04429', 'MIT':    '04430',
'HUM':    '04432', 'NEM':    '04436',
'NUK_K':  '04437', 'NUK_U':  '04439',
'QAS_M':  '04441', 'CP1':    '04442',
'NAU':    '04443', 'LYN_L':  '04450',
'EGP':    '04451', 'JAR':    '04452',
'THU_L2': '04453', 'THU_U':  '04454',
'SWC':    '04458', 'ZAK_L':  '04461',
'ZAK_U':  '04462', 'DY2':    '04464',
'SDL':    '04485', 'NSE':    '04488',
'SDM':    '04492'}
import tocgen
import os
filename="./plot_compilations/DMI_meteograms.md"
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
for k in stations.keys():
    Msg('# %s'%k)
    Msg('![%s](https://nwp.dmi.govcloud.dk/dmi-hirlam/plots/met%s00e.png)'%(k,stations[k][1:]))
tocgen.processFile(filename, filename[:-3]+'_toc.md')