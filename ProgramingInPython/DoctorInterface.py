
# import libs and files
from datetime import datetime
import patient_data as pa

# patient dictionary keys
pat_id = list(pa.patients.keys())

# check the blood pressure historic of patients
def blood_pressure_check(blood_pressure):
    syst = [i[0] for i in blood_pressure]
    diast = [i[1] for i in blood_pressure]
    mean_syst = sum(syst)/len(syst)
    mean_diast = sum(diast)/len(diast)
    
    status = ''
    if (mean_syst > 125) and (mean_diast > 85):
        status = 'High'
    elif (mean_syst <= 125) and (mean_syst > 115) and (mean_diast <= 85) and (mean_diast > 75):
        status = 'Normal'
    elif (mean_syst < 115) and (mean_diast < 75):
        status = 'Low'
    else:
        status = 'Abnormal'
    return print('pressure: {:.2f}/{:.2f}'.format(mean_syst,mean_diast)), print(status + ' pressure')

# check the distance between appointments 
def check_appointments(last_checkup, next_appointment):
    if next_appointment == "No-Date":
        return print('No appointment scheduled') 
    else:
        date1 = last_checkup
        date2 = next_appointment
        time_difference = (date2-date1).days
        return print('{} days between appointments'.format(time_difference))
# main loop
while True:
    print('\n')
    print('list of patient IDs: ', pat_id ) # to make it easier to find IDs
    input_id = input('Enter patient ID: ').upper() 

    if input_id == 'EXIT': # break main loop
        print('\n')
        print('Finishing program! Goodbye!')
        print('\n')
        break
    else:
        if input_id in pat_id:
            # date inputs used for checking appointments
            date1 = datetime.strptime(pa.patients[input_id]['last_checkup_date'], '%Y-%m-%d')
            if pa.patients[input_id]['next_appointment_date'] == "No-Date": #checking if there's an appointment
                date2 = "No-Date"
            else:
                date2 = datetime.strptime(pa.patients[input_id]['next_appointment_date'], '%Y-%m-%d')
            
            # Outputs
            print('\n')
            print('Patient: ',pa.patients[input_id]['name'])
            print(pa.patients[input_id]['age'], ' years old')
            print('Gender: ',pa.patients[input_id]['gender'])
            print('\n')
            blood_pressure_check(pa.patients[input_id]['blood_pressure_checks'])
            print('\n')
            check_appointments(date1,date2)
            print('\n')

            while True: # Run until there's no more medication to add

                # add new medication, also print medication e allergies list to make it easier to visualize
                print('medication list: ', pa.patients[input_id]['medications'])
                print('Alergies: ', pa.patients[input_id]['allergies'])
                new_med = input('Add new medication(Digit None to finish): ')
                print('\n')

                if new_med == 'None':
                    break
                elif new_med in pa.patients[input_id]['allergies']:
                    print('Patient allergic to this medication!')
                    print('\n')
                elif new_med in pa.patients[input_id]['medications']:
                    print('Already in patients medications!')
                    print('\n')
                else:
                    pa.patients[input_id]['medications'].append(new_med)
                    
            while True: # Run until there's no more medication to remove
                print('medication list: ', pa.patients[input_id]['medications'])
                print('Alergies: ', pa.patients[input_id]['allergies'])
                remove_med = input('Remove medication(Digit None to finish): ')
                print('\n')

                if remove_med in pa.patients[input_id]['medications']:
                    pa.patients[input_id]['medications'].remove(remove_med)
                elif remove_med == 'None':
                    print('\n')
                    print ('OVERVIEW') # Just to consolidate previous informations before interrupting
                    print('________________________________________________________')
                    print('Patient: ',pa.patients[input_id]['name'])
                    print(pa.patients[input_id]['age'], ' years old')
                    print('Gender: ',pa.patients[input_id]['gender'])
                    print('________________________________________________________')
                    print('Final Medication list: ', pa.patients[input_id]['medications'])
                    print('________________________________________________________')
                    print('\n')
                    print('Finished! Next Patient')
                    print('\n')
                    print('\n')
                    break
                else:
                    print('Invalid medication!')
                    print('\n')


            print('__________________________________________________________________________________')

        else: # invalid ID in main input
            print('\n')
            print('Wrong ID! Try again!')