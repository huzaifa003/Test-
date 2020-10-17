import PySimpleGUI as sg      
import os
import threading
import time
timer=0
def countdown():
                global timer
                while timer > 0:


                    for  x in range (timer):
                        time.sleep(1)
                        timer =timer -1
                        if timer == 0:
                            break
                    del x    
sg.theme('Black')    # Keep things interesting for your users
sg.SetOptions(element_padding=(2,2))

layout = [
                    
          [sg.Text('Set the timer',font=30,text_color='Green')],
          [sg.Text('Enter The Time In Seconds',text_color='Red')],
          [sg.InputText(background_color="Grey",do_not_clear=True)],
          [sg.Button('Start Timer',size =(9,2),font =45)],
          [sg.Output(size=(45,5), key='-OUTPUT-')],        
          [sg.Button('Show Remaining Time',),sg.Button('Clear'),sg.Button('Stop Timer')],
          [sg.Button("Exit")]]  
window = sg.Window('Shut Down Timer', layout,auto_size_text=True,auto_size_buttons=True)      
while True:                             # The Event Loop
    event, values = window.read()
    
    if event == 'Start Timer':
        if timer >0:

            os.system ("shutdown /a")
        else:
            print ("Your Timer Has been Started")
            timer = int(values[0])
            if timer <0:
                timer = -(timer)   
            os.system (f"shutdown /s /t {timer}")
            newtimer=threading.Thread(target= countdown)
            newtimer.start() 
    if event == 'Show Remaining Time':
        if timer >0:
            print(f"The Remaining Time is ={timer}")
        else:
            print ("No ShutDown Is Scheduled")
    if event == 'Clear':
        window['-OUTPUT-'].update('')
    if event == 'Stop Timer':
        if timer >0:
            os.system (f"shutdown /a")
            timer = 0
            window['-OUTPUT-'].update('Your ShutDown Has been Cancelled\n')
        else:
            print ("No ShutDown Is Scheduled") 
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()