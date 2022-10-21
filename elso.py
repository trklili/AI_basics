
import pandas as pd
import numpy as np
df = pd.read_csv('ip.txt', header = None,dtype="string")

ipcimek=df.squeeze()

print("Sorok száma :",ipcimek.shape[0])


nodevice=np.sum(ipcimek.str.startswith("2001:0db8", na=False))
print("Dokumentációs címek száma,amik eszközöknek nincsenek kiosztva:", nodevice)

globalip=np.sum(ipcimek.str.startswith("2001:0e", na=False))
print("Informatikai eszközöknek kiosztott globális egyedi címek száma", globalip)

localuniqueip=np.sum(ipcimek.str.startswith("fc", na=False))+np.sum(ipcimek.str.startswith("fd", na=False))
print("Az eszközöknek kiosztott helyi egyedi címek száma", localuniqueip)