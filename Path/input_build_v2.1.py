import scipy.io as sio
import pandas as pd
import  numpy as np

file_head = 'simResults_'


def data_build(i) : 
    j = i + 1
    dt = (tout[j]-tout[i]).astype('float32')
    while dt==0:
        j+=1
        print(j-i)
        dt = (tout[j]-tout[i]).astype('float32')
        print(dt)
    start_state = state[i].astype('float32')
    u = output[i].astype('float32')
    #while dt<0.02 : 
    #    j += 1
    #    dt = tout[j]-tout[i]
    #    #print(t)
    #    u += output[j-1]*(tout[j]-tout[j-1])
    #    
    #u = u/dt
    target_state = state[j].astype('float32')
    P_t,  Q_t,  R_t,  Phi_t,  The_t,  Psi_t,  U_t,  V_t,  W_t,  X_t,  Y_t,  Z_t  = start_state
    P_t1, Q_t1, R_t1, Phi_t1, The_t1, Psi_t1, U_t1, V_t1, W_t1, X_t1, Y_t1, Z_t1 = target_state
    Phi = Phi_t
    The = The_t
    Psi = Psi_t
    dPhi = (Phi_t1-Phi_t)/dt
    dThe = (The_t1-The_t)/dt
    dPsi = (Psi_t1-Psi_t)/dt
    dx = (X_t1-X_t)/dt
    dy = (Y_t1-Y_t)/dt
    dz = (Z_t1-Z_t)/dt
    dP = (P_t1-P_t)/dt
    dQ = (Q_t1-Q_t)/dt
    dR = (R_t1-R_t)/dt
    dU = (U_t1-U_t)/dt
    dV = (V_t1-V_t)/dt
    dW = (W_t1-W_t)/dt
    return np.array([Phi, The, Psi, dPhi, dThe, dPsi, dx, dy, dz, dP, dQ, dR, dU, dV, dW, u[0], u[1], u[2], u[3]])
'''
i=1
mat_data = sio.loadmat(file_head+'%s'%i+'.mat')
yout = mat_data['yout'].astype('float32')
tout = mat_data['tout'].astype('float32')
print(yout.shape, tout.shape)
state = yout[:, 0:12]
output = yout[:, 16:20]
max_step = tout.shape[0]-1
while (tout[tout.shape[0]-1]-tout[max_step])<1.0 :
    max_step -= 1
Input = data_build(0)
print("Start Building...")
for i in range(1,max_step):
    Input = np.vstack((Input, data_build(i)))
    print('\r',"Progress:{0}%".format(round((i + 1) * 100 / max_step)), end='')

print('\n','Build End')
print(Input.shape)
'''
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
    #while (tout[tout.shape[0]-1]-tout[max_step])<1.0 :
    #    max_step -= 1
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

Inputdf = pd.DataFrame(Final_Input, columns = ['Phi',   'The',   'Psi', 
                                         'Phi_velocity', 'The_velocity', 'Psi_velocity', 
                                         'X_velocity',   'Y_velocity',   'Z_velocity',  
                                         'Phi_acceleration', 'The_acceleration', 'Psi_acceleration',
                                         'X_acceleration',   'Y_acceleration',   'Z_acceleration', 
                                         'mc1', 'mc2', 'mc3', 'mc4'])

Inputdf.to_csv('test2_s1_t1.csv', index=False)                                       