## Done by Smit PATEL(jayambe36)


## Importing the required modules and libraries which list down here in this code in your system.
# pip install psutil
# pip install py-cpuinfo
# pip install wmi


import platform
import psutil
import cpuinfo
import wmi

print(f"Achitecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating System: {platform.platform()}")
print(f"Processor: {platform.processor()}")


my_cpuinfo = cpuinfo.get_cpu_info() # Getting the CPU info

#print(my_cpuinfo) # This will print the dictionary of the cpu info.

print(f"Full CPU Name: {my_cpuinfo['brand_raw']}") # This will print the full name of the CPU.
print(f"Full CPU Name: {my_cpuinfo['hz_actual_friendly']}") # This will print the actual clock speed of the CPU.
print(f"Full CPU Name: {my_cpuinfo['hz_advertised_friendly']}") # This will print the advertised clock speed of the CPU.


#print(my_cpuinfo.keys()) # This will print the keys of the dictionary.


print(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB") #showing ram in GB


## GPU Info

pc = wmi.WMI() # This will create a WMI object.
os_info = pc.Win32_OperatingSystem()[0] # This will get the operating system info.


#print(pc) # This will print the dictionary of the system info.
print(os_info) # This will print the dictionary of the system info.
print(pc.Win32_Processor()[0])
print(pc.Win32_VideoController()[0])


print("CPU Name: ",pc.Win32_Processor()[0].name)
print("GPU Name: ",pc.Win32_VideoController()[0].name)

print("ALL IS WELL") #just to make sure it works.