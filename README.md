# DesignIpsCloudEnvironment
A really long path...
# VERSION I
This project is aimed to design in IPS in a cloud computing environment. At the primary stage, I will focus on detecting 
XSS(http based traffic, which will soonner be extend with wireshark networks logs, on premices logs, real-time iocs and so on...) based malicious activity. 
The first tests will be perform on vbox and azure vpc.The code is essentially on python. The code editor doesn't matter.
Our goal is to reduce as much as possible, the latency time into detecting and preventing malicious activity in a cloud in order to enhance his
security. Artificial Intelligence will enhance our chances to reach our goals. The Machine learning we are about to deal with is an 'Unsupervised Ml algorithm'.
Using this graph, you should rapidly comprehend why we did that choice...

![image](https://github.com/heerbx/DesignIpsCloudEnvironment/assets/70644385/62891c89-a062-4a68-80c0-0b9a7396979c)

At last, we will use for this this test our own generated dataset thank to burpsuite and acunetix.
##  Requirements
-> Python libs(pyhton 3.11.x): pandas, pycaret, urllib, ET, csv...
-> proxy log collectors: Wireshark, Burpsuite Community edition...
-> Web vunerability scanner: Acunetix(version 8.x) ...
-> Environments: Vbox, Azure...

## Architecture:
In short, That's the starting point... Which unfortunately change in the future..😂
![image](https://github.com/heerbx/DesignIpsCloudEnvironment/assets/70644385/4c00f5d4-8ccb-47ea-b0fd-be0b5de94b92)

## Microsoft vpc
This is how test test environment looks like.
![image](https://github.com/heerbx/DesignIpsCloudEnvironment/assets/70644385/b9ce3238-52fd-43f2-8148-5f2856824688)


