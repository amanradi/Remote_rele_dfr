from os import path
from pywinauto.application import Application
import time
#import pywhatkit

#kirim_wa.start_server()

x = 1

if x==1:
    print ("Program dijalankan sebentar ya")
    plc = Application(backend='uia').start(r'"C:\Program Files (x86)\ABB\HMI600\HMI600.exe"').connect(title='HMI600',timeout=100)

    #plc.Hmi600.print_control_identifiers()

    hubung_1 = plc.Hmi600.child_window(title="Logon, equipment address:", auto_id="20502", control_type="RadioButton")
    hubung_1.click_input()

    hubung_2 = plc.Hmi600.child_window(title="User name", auto_id="22102", control_type="Edit")
    hubung_2.click_input()
    hubung_2.type_keys("Administrator")

    hubung_3 = plc.Hmi600.child_window(title="Password", auto_id="20514", control_type="Edit")
    hubung_3.click_input()
    hubung_3.type_keys("welcome")

    hubung_4 = plc.Hmi600.child_window(title="Upload status", auto_id="20773", control_type="CheckBox")
    hubung_4.click_input()

    #hubung = plc.Hmi600.child_window(title="Connect", control_type="Window").wrapper_object()
    #hubung.click_input()
      

    hubung_5 = plc.Hmi600.child_window(title="OK", auto_id="1", control_type="Button")
    hubung_5.click_input()

    time.sleep(10)

    hubung_6 = plc.Hmi600.child_window(title="Accept temporarily", auto_id="22100", control_type="Button")
    hubung_6.click_input() 

    print ("tunggu sebentar...............")
    time.sleep(30)

    
    hubung_8 = plc.Hmi600etl600_1.child_window(title="HMI600 - ETL600_1", control_type
    ="Window")
    hubung_8 = plc.Hmi600etl600_1.maximize()

    hubung_7 = plc.Hmi600etl600_1.menu_select("View->Display events")

   # plc.Hmi600etl600_1.print_control_identifiers()

    
    hubung_8.set_focus()
    gambar = plc.Hmi600etl600_1.capture_as_image()
    gambar.save('gambarnya.png')
    print("selesai")

    hubung_9 = plc.Hmi600etl600_1.child_window(auto_id="1", control_type="Edit")
    hubung_9 = plc.Hmi600etl600_1.WindowText()
    #print(hubung_9)
'''
while True:
    #pywhatkit.sendwhats_image("+6281215546238", "gambarnya.png")
    pywhatkit.sendwhatmsg_instantly("+6281215546238", "mantullll")
    time.sleep(10)
    x =+ 1
    if x == 10:
        break

#kirim_wa.sendwhats_image("EWSgroup", "gambarnya.png")
#pywhatkit.sendwhatmsg_to_group_instantly("EWSgroup", "Hey") 

'''