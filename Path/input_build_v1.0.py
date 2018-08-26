import scipy.io as sio
import pandas as pd
import  numpy as np

file_head = 'simResults_'

def data_build(i) : 
    j = i
    dt = tout[j]-tout[i]
    start_state = state[i]
    u = np.zeros(4)
    while dt<0.02 : 
        j += 1
        dt = tout[j]-tout[i]
        #print(t)
        u += output[j-1]*(tout[j]-tout[j-1])    
    u = u/dt
    target_state = state[j]
    return np.append(np.append(np.append(start_state[0:9], target_state[0:9]),target_state[9:12]-start_state[9:12]), u)


for file_num in range(1,19):
     #   print(i)
    file_name = file_head+'%s'%file_num+'.mat'
    print(file_name)
    mat_data = sio.loadmat(file_name)
    yout = mat_data['yout'].astype('float32')
    tout = mat_data['tout'].astype('float32')
    #print(yout.shape, tout.shape)
    state = yout[:, 0:12]
    output = yout[:, 16:20]
    max_step = tout.shape[0]-1
    while (tout[tout.shape[0]-1]-tout[max_step])<0.02 :
        max_step -= 1
    Input = data_build(0)
    #print("Start Building...")
    for i in range(1,max_step):
        Input = np.vstack((Input, data_build(i)))
        print('\r',"Progress:{0}%".format(round((i + 1) * 100 / max_step)), end='')

    print('\n','Build End')
    print(Input.shape)
    if file_num==1:
        Final_Input = Input
    else:
        Final_Input = np.vstack((Final_Input,Input))
    print(Final_Input.shape)

Inputdf = pd.DataFrame(Final_Input, columns = ['start_P',   'start_Q',   'start_R', 
                                         'start_Phi', 'start_The', 'start_Psi', 
                                         'start_U',   'start_V',   'start_W', 
                                         'target_P',   'target_Q',   'target_R', 
                                         'target_Phi', 'target_The', 'target_Psi', 
                                         'target_U',   'target_V',   'target_W', 
                                         'diffe_X',   'diffe_Y',   'diffe_Z', 
                                         'mc1', 'mc2', 'mc3', 'mc4'])

Inputdf.to_csv('data_s1_t1.csv', index=False)