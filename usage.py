import os
import psutil
import pandas as pd

pid=os.getpid()
py=psutil.Process(pid)

cpu_usage = os.popen("ps aux | grep "+str(pid)+"| grep -v grep | awk '{print $3}'").read()
cpu_usage=cpu_usage.replace("\n","")

memory_usage=round(py.memory_info()[0] / 2. **30, 2)

print("cpu usage\t\t:", cpu_usage, "%")
print("memory usage\t\t:", memory_usage, "%")

data=pd.read_csv('/home/nuc/Peract/peract/logs/C2LIN_drawer/C2FARM_LINGUNET_BC/seed0/train_data.csv')
print(data)