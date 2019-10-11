#%%
import visa
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import os
def AUTO(Equip,chan1,chan2):
    Equip[OSC].write("AUToscale")	
    time.sleep(2)
    #Equip[OSC].write(":ACQuire:TYPE AVERage")
    VPP1=float(Equip[OSC].ask("MEASure:VPP? CHANnel" + str(chan1))) 
    VPP2=float(Equip[OSC].ask("MEASure:VPP? CHANnel" + str(chan2))) 
    CHRange1=1.25*(VPP1)
    CHRange2=1.25*(VPP2)
    if CHRange2<.160:
        CHRange2=.160
    if CHRange1<.160:
        CHRange1=.160
    return   CHRange1, CHRange2      
    

def set_up_equipment(rm,devices):
    # This function should allow the program to automatically find and set up the function generator (FG) and the oscilloscope (OSC).
    # It returns two integers that are used to program which is the scope and which is the function generator.
    # You can add other devices
    n=0
    Address=[0]*len(devices)
    Equip=[0]*len(devices)
    if len(devices) > 0:
        for device in devices:
            Address[n]=device
            Equip[n]=rm.open_resource(Address[n])
            Type=str(Equip[n].ask("*IDN?"))
            if "DSO" in Type:
                OSC=n
            if "33" in Type:
                FG=n
            n=n+1
    else:
        print('... didn\'t find anything!')
    return Equip, OSC, FG
def set_equipment(Equip,OSC,FG):
    #Set the test equipment to a known state
    Equip[OSC].clear()
    Equip[FG].clear()
    Equip[OSC].write("*RST")
    Equip[FG].write("*RST")
    Equip[FG].write("OUTPut:LOAD INFinity") 
def start_visa():    
    resourceManager = visa.ResourceManager()
    devices = resourceManager.list_resources('USB?*INSTR')
    rm = visa.ResourceManager()
    return devices,rm
def Gain():
    V1= float(Equip[OSC].ask("MEASure:VPP? CHANnel" + str(1)))
    V2=  float(Equip[OSC].ask("MEASure:VPP? CHANnel" + str(2)))
    return 20*np.log10(V2/V1) 
devices, rm =start_visa()
Equip, OSC,FG=set_up_equipment(rm,devices)
print(Equip, OSC,FG)
set_equipment(Equip,OSC,FG)

#Set start Frequency (Will not work below 50Hz)
FreqStart =50.
FreqStart=np.log10(FreqStart)
#Set end Frequency. No guarantee a circuti will work at 10MHz
FreqEnd =10e6
FreqEnd=np.log10(FreqEnd)
# Number of points on the Bode plot.  Use a small number for debugging
NumSteps = 5
# Input voltage Set as large as you can to that it can measure filters.
# Slew rate, Gain and supply rails will limit how large you can make the amplitude.
Amplitude =1
#Create the log progression. 
FreqArray = np.logspace(FreqStart,FreqEnd,NumSteps)
NumSteps = len(FreqArray)
#Create a panda Dataframe to store data
df = pd.DataFrame(columns=['Frequency', 'Magnitude', 'Phase'])
## Data Acquisition
InChan = 1		# Measurement channels.
OutChan = 2
for iter in range(0, NumSteps):
    Freq = FreqArray[iter]

  
    Equip[FG].write("APPLy:SIN " + str(Freq) + ", " + str(Amplitude) + ", 0")
    time.sleep(1) 
    Equip[OSC].write("AUToscale")
    CR1, CR2= AUTO(Equip,1,2)
   
    Equip[OSC].write(":CHANnel1:OFFSet "+str(0))
    Equip[OSC].write(":CHANnel2:OFFSet "+str(0))
    Equip[OSC].write(":CHANnel1:RANGe "+str(CR1))
    Equip[OSC].write(":CHANnel2:RANGe "+str(CR2))
    Equip[OSC].write(":TRIGger:EDGE:SOURce CHANnel1")
    #Equip[OSC].write(":ACQuire:TYPE AVERage")
    #Equip[OSC].write(":ACQuire:COUNt 8")
    #time.sleep(1)   
    T_FreqArray=0.0
    T_PhaseArray=0
    T_GainArray=0
    xxx=0
    #How many samples to average.  
    A=1
    while xxx<A:
     
        T_FreqArray=float(Equip[OSC].ask("MEASure:FREQuency? CHANnel" + str(1)))+T_FreqArray          
        T_PhaseArray=float(Equip[OSC].ask(":MEASure:PHASe?  CHANnel2 , CHANnel1"))+T_PhaseArray
        T_GainArray=Gain()+T_GainArray
        xxx=xxx+1
     
    F = T_FreqArray/A
    P=T_PhaseArray/A   
    G=T_GainArray/A
    print (F, G, P)
    #Sometimes the phase measurment does not work and gives a vaue near 10^18
    #This will only allow valid data to be plotted/saved
    if (P<300):
        df=df.append({'Frequency':F,'Magnitude':G,'Phase':P}, ignore_index=True )
    
# Save data to csv
path= os.getcwd()
# Change to your path!
path_out=path+'/Dropbox/Public/EE110L/python/Bode.csv'
df.to_csv(path_out, encoding='utf-8', index=True)  


#Plot Data
fig, ax = plt.subplots(figsize=(8,6))
ax=df.plot(kind='line',    x='Frequency', y='Magnitude', style='b',  ax=ax,  fontsize=15,logx=True, label='Magnitude')
ax.set_xlabel('Frequency ( Hz)', fontsize=15)
ax.set_ylabel('Magnitude (dB)', color='b', fontsize=15)
ax.tick_params('y', colors='b')
ax.get_legend().remove()
ax1 = ax.twinx()
df.plot(kind='line',    x='Frequency', y='Phase', style='ro',  ax=ax1,  fontsize=15,logx=True,label='Phase')
ax1.set_ylabel('Phase($^o$)', color='r', fontsize=15)
ax1.tick_params('y', colors='r')
ax1.get_legend().remove()
plt.title('Change title')
plt.tight_layout(pad=2, w_pad=2, h_pad=2.0)
 
## show the plot on the screen
plt.show()


#%%
