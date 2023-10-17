# DesignIpsCloudEnvironment
This project is aimed to design in IPS in a cloud computing environment. At the primary stage, I will focus on detecting 
XSS(http based traffic, which will soonner be extend with wireshark networks logs, on premices logs, real-time iocs and so on...) based malicious activity. 
The first tests will be perform on vbox and azure vpc.The code is essentially on python. The code editor doesn't matter. 
Our goal is to reduce as much as possible, the latency time into detecting and preventing malicious activity in a cloud in order to enhance his
security.

# VERSION I
##  Requirements
-> Python libs(pyhton 3.11.x): pandas, pycaret, urllib, ET, csv...
-> proxy log collectors: Wireshark, Burpsuite Community edition...
-> Web vunerability scanner: Acunetix(version 8.x) ...
-> Environments: Vbox, Azure...

## Architecture:
In short, That's the starting point... Which unfortunately change in the future..😂
![Capture d'écran 2023-10-09 123604](https://github.com/heerbx/DesignIpsCloudEnvironment/assets/70644385/d008868b-bfe1-4194-9cf8-2371632cd04e)
