import psutil
import datetime
import pandas as pd

pids = []
name = [] 
cpu_usage= []
memory_usage = []
memory_usage_percentage =[]
status =[]
create_time =[]
threads =[]

for process in psutil.process_iter():
    pids.append(process.pid)
    name.append(process.name())

    cpu_usage.append(process.cpu_percent(interval=1)/psutil.cpu_count())

    memory_usage.append(round(process.memory_info().rss/(1024*1024),2))

    memory_usage_percentage.append(round(process.memory_percent(),2))

    create_time.append(datetime.datetime.fromtimestamp(process.create_time()).strftime("%Y%m%d - %H:%M:%S"))

    status.append(process.status())

    threads.append(process.num_threads())

data = {"PIds":pids,
        "Name": name,
        "CPU":cpu_usage,
        "Memory Usages(MB)":memory_usage,
        "Memory Percentage(%)": memory_usage_percentage,
        "Status": status,
        "Created Time": create_time,
        "Threads": threads,
        }

process_df = pd.DataFrame(data)
#set index to pids
process_df =process_df.set_index("PIds")

#sort the process 
process_df =process_df.sort_values(by='Memory Usages(MB)', ascending=False)

#add MB at the end of memory
process_df["Memory Usages(MB)"] = process_df["Memory Usages(MB)"].astype(str) + " MB"

print(process_df)