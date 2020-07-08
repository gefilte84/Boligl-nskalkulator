#Boliglån Kalkulator med GUI
#Obligatorisk oppgave 1 Vår

from tkinter import *
def beregn_lan():
    if status.get()=='enslig':
     if int(bruttoinntekt.get())<=300000:
         lonn_faktor=int(bruttoinntekt.get())*0
     elif int(bruttoinntekt.get())<=450000:
         lonn_faktor=int(bruttoinntekt.get())*3
     elif int(bruttoinntekt.get())<=650000:
         lonn_faktor=int(bruttoinntekt.get())*4
     elif int(bruttoinntekt.get())<=900000:
         lonn_faktor=int(bruttoinntekt.get())*4.5
     elif int(bruttoinntekt.get())<=1000000:
         lonn_faktor=int(bruttoinntekt.get())*5
     elif int(bruttoinntekt.get())<=1200000:
         lonn_faktor=int(bruttoinntekt.get())*5.25
     else:
         lonn_faktor=int(bruttoinntekt.get())*5.25

        #Lånefaktor gift
    if status.get()=='par':
     if int(bruttoinntekt.get())<=450000:
         lonn_faktor=int(bruttoinntekt.get())*0
     elif int(bruttoinntekt.get())<=650000:
         lonn_faktor=int(bruttoinntekt.get())*3
     elif int(bruttoinntekt.get())<=900000:
         lonn_faktor=int(bruttoinntekt.get())*4.25
     elif int(bruttoinntekt.get())<=1000000:
         lonn_faktor=int(bruttoinntekt.get())*5
     elif int(bruttoinntekt.get())<=1200000:
         lonn_faktor=int(bruttoinntekt.get())*5.5
     else:
         lonn_faktor=int(bruttoinntekt.get())*5.75

    #Barne trekk
    if status.get()=='par':
        barne_trekk=int(antall_barn.get())*365000
    else:
        if status.get()=='enslig':
            barne_trekk=int(antall_barn.get())*780000


    maks_lanet=(int(bruttoinntekt.get())*lonn_faktor)-barne_trekk
    eklanet=(int(egenkapital.get())/0.15)-int(egenkapital.get())

    if eklanet<maks_lanet:
        maks_lan.set(eklanet)
        maks_kjopesum.set(eklanet+int(egenkapital.get()))
    else:
        if eklanet>=maks_lanet:
            maks_lan.set(maks_lanet)
            maks_kjopesum.set(maks_lanet+(int(egenkapital.get())))
    

window=Tk()

# Vi gir vinduet et navn
window.title('Lånekalkulator')

# Vi lager ledetekster for kjøpesum, egenkapital og lånetilsagn
lbl_bruttoinntekt=Label(window, text='Bruttoinntekt:')
lbl_bruttoinntekt.grid(row=0, column=0, padx=100, pady=15)

lbl_egenkapital=Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=1, column=0, padx=100, pady=15)

lbl_status=Label(window, text='Status(Enslig/Par):')
lbl_status.grid(row=2, column=0, padx=100, pady=15)

lbl_antall_barn=Label(window, text='Antall barn:')
lbl_antall_barn.grid(row=3, column=0, padx=100, pady=15)

lbl_maks_kjopesum=Label(window, text='Maksimal kjøpesum:')
lbl_maks_kjopesum.grid(row=5, column=0, padx=100, pady=15)

lbl_maks_lan=Label(window, text='Maksimal lån:')
lbl_maks_lan.grid(row=6, column=0, padx=100, pady=15)

# Vi lager inndatafelt for kjøpesum og egenkapital
bruttoinntekt=StringVar()
ent_bruttoinntekt=Entry(window, width=9, textvariable=bruttoinntekt)
ent_bruttoinntekt.grid(row=0, column=1, padx=100, pady=15)

egenkapital=StringVar()
ent_egenkapital=Entry(window, width=9, textvariable=egenkapital)
ent_egenkapital.grid(row=1, column=1, padx=100, pady=15)

status=StringVar()
ent_status=Entry(window, width=9, textvariable=status)
ent_status.grid(row=2, column=1, padx=100, pady=15)

antall_barn=StringVar()
ent_antall_barn=Entry(window, width=9, textvariable=antall_barn)
ent_antall_barn.grid(row=3, column=1, padx=100, pady=15)

maks_kjopesum=StringVar()
ent_maks_kjopesum=Entry(window, width=20, textvariable=maks_kjopesum)
ent_maks_kjopesum.grid(row=5, column=1, padx=100, pady=15)

maks_lan=StringVar()
ent_maks_lan=Entry(window, width=20, textvariable=maks_lan)
ent_maks_lan.grid(row=6, column=1, padx=100, pady=15)


# Vi lager en knapp for å beregne lånetilsagnet
btn_beregn=Button(window, text='Beregn kjøpesum/maks lån', command=beregn_lan)
btn_beregn.grid(row=4, column=0, columnspan=2, pady=15)

# Og vi lager et utdatafelt/visningsfelt for konklusjonen på lånnetilsagnet
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window, width=20, state='readonly', textvariable=lanetilsagn)


# Knapp for å avslutte
btn_avslutt=Button(window, text='Avslutte', command=window.destroy)
btn_avslutt.grid(row=7, column=0, columnspan=2, pady=15)


window.mainloop()
