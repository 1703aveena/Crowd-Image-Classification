# -*- coding: utf-8 -*-
"""Aveena-ML-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PT53hknkx2Ym36oXScLCvBJ3XHExz
"""

# import pandas as pd
import pandas as pd
import numpy as np
import math 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
"""
    One_Nx1=pd.DataFrame( np.ones((n, 1)) )
    O_kx1= pd.DataFrame(np.zeros((k, 1)))
"""
import warnings
warnings.filterwarnings("ignore")

#from google.colab import drive
#drive.mount('/content/drive', force_remount=True)

#train_labels0 = pd.read_csv("/content/drive/My Drive/ML-3/Train_Labels.csv") 
#train_features0 = pd.read_pickle("/content/drive/My Drive/ML-3/Train_Features.pkl") 


#test_features0 = pd.read_pickle("/content/drive/My Drive/ML-3/Test_Features.pkl")

""" train_labels0 = pd.read_csv("/kaggle/input/cse512hw3/Train_Labels.csv")

train_features0 = pd.read_pickle("/kaggle/input/cse512hw3/Train_Features.pkl") 


test_features0 = pd.read_pickle("/kaggle/input/cse512hw3/Test_Features.pkl")

train_featuresdf_T=pd.DataFrame(train_features0).T
train_featuresdf_T.head()

Y_=pd.DataFrame(train_labels0)
Y_.iloc[[8]]## get row
Y_.iloc[8][1]## get cell

#from collections import defaultdict
##new_dic = defaultdict(dict)
#new_dic[1][2]=5


"""


"""
n=train_featuresdf_T.shape[0] ## numer of samples -rows
k=train_featuresdf_T.shape[1] ## number of features - column




One_nx1=np.ones((n, 1))
one_column=pd.DataFrame(One_nx1 , index=train_featuresdf_T.index.values)

X=pd.DataFrame(train_featuresdf_T)


Xbar= concatenateHorizontally(train_featuresdf_T,one_column)

X_=Xbar

print(X_.iloc[[0]])



thetaframes= {}
classes=2
for thetai in range(classes):
  thetaframes[thetai]= θ_1xk=pd.DataFrame( np.ones((1,k+1 )) )
  df=thetaframes[thetai]
  print(df.head())
  print("shape",df.shape)
print ("Before")
print (thetaframes)
class_=1
if class_ in thetaframes:
    del thetaframes[class_] ##Remove from Dict
    

print ("After")
print (thetaframes)
  """
"""
Xnorm=np.linalg.norm(X_)

#print (Xnorm)

X_norm1=X_ / Xnorm
#print(X_norm1.head(1))
k=512
one_=pd.DataFrame(np.zeros((1, k+1)))##X_norm1.iloc[[0]]
two_=X_norm1.iloc[[2]]

sum=np.add(one_.values, two_.values)
print(one_.values)
print(two_.values)
print(sum)
#print(X_.values)


#for i in range(5): 
print(X_.iloc[[i]]) 

* """
"""
permute=np.random.permutation(n)

pd.DataFrame(permute).head()

"""

"""
θ_1xk=pd.DataFrame( np.ones((1, k-1)) )
#print(θ_1xk.values)
classesk=2
rowscolumns=[]
rows=[]
rows.append(1)
rows.append(2)
rows.append(3)
rows.append(4)
rowscolumns.append(rows)
rows=[]
rows.append(5)
rows.append(6)
rows.append(7)
rows.append(8)
rowscolumns.append(rows)

rowscolumns1=[]
rows=[]
rows.append(1)
rows.append(2)
rows.append(3)
rows.append(4)
rowscolumns1.append(rows)
rows=[]
rows.append(5)
rows.append(6)
rows.append(7)
rows.append(8)
rowscolumns1.append(rows)
one=np.concatenate((rowscolumns1, rowscolumns1), axis=1)
one1=[[1],[2]]
if not len(one1):
    print("empty")
else:
    one11=np.concatenate((one, one1), axis=1)
    print(one11)
print(np.shape(one))
print(one[0][4])
"""

def concatenateVertically(df1,df2):
    df_concat = pd.concat([df1, df2], axis=0)
    return df_concat

def concatenateHorizontally(df1,df2):
    df_concat = pd.concat([df1, df2], axis=1)
    return df_concat

"""

{(Xi, Yi)}n  i=1 

(for data), m (for batch size), η0, η1 (for step size), max epoch, δ (stopping
criteria)
2: for epoch = 1, 2, ..., max epoch do
3: η ← η0/(η1 + epoch)
4: (i1, ..., in) = permute(1, ..., n)
5: Divide (i1, ..., in) into batches of size m or m + 1
6: for each batch B do
7: Update θ using Eqs. (5) and (7)
8: Break if L(θ new) > (1 − δ)L(θold) // not much progress, terminate

"""
def sgd_function(m_batchsize,  n0, n1 , max_epoch, δ, X_, Y_):
  n=X_.shape[0] ## numer of samples -rows
  k=X_.shape[1] ## number of features - column


  #print (n,k)
    
  thetaframes= {}
  classesk=4
  for thetai in range(1,classesk+1):
    thetaframes[thetai]= pd.DataFrame( np.ones((1,k )) )
    df=thetaframes[thetai]
    #print(df.head())
    #print("shape",df.shape)
  
  ltheta_old = 1000000000
  ltheta_new=0


  LTheta_list=[]
  epochlist=[]
  accuracy_list=[]
  #for thetai in range(classes):
    #thetalog[thetai]= 0
  Xnorm=np.linalg.norm(X_)
  X_norm=X_ / Xnorm
  #print(thetaframes)
  
  for epoch in range(max_epoch):
    nn= n0/(n1 + epoch)
    
    ##Step 4:
    permute=np.random.permutation(n)
    print (permute[0] ,"0")
    
    X_permute=pd.DataFrame()
    Y_permute=pd.DataFrame()
    
    ##X and Y with permute
    for index in range(n):
        Row_=X_norm.iloc[[permute[index] ]] ## get each row of this batch   X
        X_permute=concatenateVertically(X_permute,Row_)##append it to the dataframe
        Row_Y_=Y_.iloc[[permute[index] ]] ## get each row of this batch  Y
        Y_permute=concatenateVertically(Y_permute,Row_Y_)##append it to the dataframe

    X_permute=X_permute.values
    
    ##Y_permute=Y_
    batches=int (n/m_batchsize)   ## 4000/batch-size = number of rows in X for each batch
    start=0
    end=m_batchsize
    print (batches, "batches")
    
    
    X_ThetaProb=[]
    ##divide data into m batches :
    for eachbatch in range(batches):  ##Step 6: for each batch B do
        ##Step 5: Get the permute rows of X-------0
        """
        X_Batch=pd.DataFrame()
        Y_Batch=pd.DataFrame()
        
        
        X_Batch=X_permute.iloc[start:end, :]
        #print("X_Batch",X_Batch.head())
        Y_Batch=Y_permute.iloc[start:end, :]"""
        
        X_Batch=X_permute[start: end, :]
        #print("X_Batch",X_Batch.head())
        Y_Batch=Y_permute.iloc[start: end, :]
        print("start", start)
        print("end", end)
    
       
        #print(permute[index])
      
        
        #Get the permute rows of X-------0

      
        #print("X_Batch",X_Batch.shape)
      
        ##Step 6: Update θs : k times for k classes:
        ##get the exp (θ_1xk_t and Xbar_)
        
      
        ###Update θ using Eqs. (5) and (7)
        ## write code here  
        ##Get the common values of the batch
        b=X_Batch.shape[0]
        
        #print("Before each thetaframes", len(thetaframes))
        #print(thetaframes)
        list_prob_thetas_Xbatch,thetaframes=XiEach(m_batchsize,X_Batch,Y_Batch,thetaframes ,classesk,nn)
        #print(len(list_prob_thetas_Xbatch),"len - list_prob_thetas_Xbatch")
        #print("After each thetaframes", len(thetaframes))

        
        
        start+=m_batchsize; ## for   m=250 :  i=0,250, 500, 750....
        end+=m_batchsize; ## for m=250 :    i=250, 500, 750, 1000....
        
        if not len(X_ThetaProb):
            #print("empty")
            X_ThetaProb=list_prob_thetas_Xbatch
        else:
            X_ThetaProb=np.concatenate((X_ThetaProb, list_prob_thetas_Xbatch), axis=0)
        
        #print(len(X_ThetaProb),"len- X_ThetaProb")

    
        #print(np.shape(X_ThetaProb))
        #print(np.shape(list_prob_thetas_Xbatch))
        #print("each batch loop end itr=",eachbatch)
    ##Each batch loop ends
    #print("Starting for L(θ)")
        ##Step 8 :Break if L(θ new) > (1 − δ)L(θ old) // not much progress, terminate Ltheta
    cols=X_norm.shape[1]
    
    
    ####    Loss_theta_X=[]
    sumProb=0
    for i in range (n):
        #Xi=X_.iloc[[i]]   ##X row
        Yi=Y_.iloc[i][1]## get cell - Y row
        yi=int(Yi)
        #print("Yi",yi)
        #print("i",i)
        probability=X_ThetaProb[i][yi-1]
        #print(probability)
        sumProb=np.add(sumProb,np.log(probability))
    
    print(sumProb)
    n_1=1 / n
    ltheta_new = (-1) * (n_1) * sumProb
        
    print("epoch",epoch)
    epochlist.append(epoch)     
    acc=accuracy(thetaframes, X_norm, Y_, n , k,classesk)
    accuracy_list.append(acc)
    
    print("ltheta_new",ltheta_new)
    print("ltheta_old",ltheta_old)
    if ( ltheta_new > ( (1- δ) * ltheta_old)):
            print("epoch",epoch)
            LTheta_list.append(ltheta_new)
            break ##not much progress, terminate Ltheta
    else:
            ltheta_old=ltheta_new
            LTheta_list.append(ltheta_old)
    
     
    
  return LTheta_list,epochlist,thetaframes,accuracy_list

def indicatorFn(Yi,class_):
  indicatori=0
  #print("Yi=",Yi," class=",class_)
  #print("Yi= =class ",(Yi == class_ ))

  if(Yi == class_ ):
    indicatori=1
  else:
    indicatori=0
    
  return indicatori

def probabilityC_XthetaFn(numerator,denominator): ##Xi_,thetaframes ,classesk,theta_ci,denominator
  
  
  probabilityC_Xthetai= numerator / denominator 
  
  #print("probabilityC_Xthetai")
  #print(probabilityC_Xthetai)
  return probabilityC_Xthetai

def probabilityC_k_XthetaFn(denominator):
    

  probabilityC_Xthetai= 1 / denominator 
  
  #print("probabilityC_Xthetai")
  #print(probabilityC_Xthetai)
  return probabilityC_Xthetai

def XiEach(batchsize,X_b,Y_b,thetaframes ,classesk,nn):

    rows=X_b.shape[0]
    cols=X_b.shape[1]

    denominator=[]
    theta_X_exp=[]
    list_prob_thetas_X=[]
    delta_thetaframes_sum={}
    for thetai in range(1,classesk+1):
        delta_thetaframes_sum[thetai]= pd.DataFrame( np.zeros((1,cols )) )
        df=delta_thetaframes_sum[thetai]
    
    
    for i in range(batchsize):
        #print("i in range",i)
        ##Df Xi_=X_b.iloc[[i]]   ##X row
        Xi_=X_b[i]   ##X row
        Yi=Y_b.iloc[i][1]## get cell - Y row
    
        ##df--Xi_T=Xi_.transpose()
        #print("Xi",len(Xi_))
        #print("Xi_")
        
        Xi_T=np.transpose(Xi_)
        sumthetaj_X=0;
        thetarow_X=[]
        for j in range (1,classesk):
            thetaj=thetaframes[j]
            ##Df- thetaj_X=np.dot(thetaj.values,Xi_T.values)
            thetaj_X=np.dot(thetaj,Xi_T)
            exp_thetaj_X=np.exp(thetaj_X)
            #print("den i ",i , " j",j," thetaj_X",thetaj_X," exp_thetaj_X",exp_thetaj_X)
            #print("thetaj_X",thetaj_X)
            thetarow_X.append(exp_thetaj_X) ##theta_i for Xi 
            sumthetaj_X=np.add(sumthetaj_X,exp_thetaj_X)
            #print("den j",j," sumthetaj_X",sumthetaj_X)
        #print(len(thetarow_X),"thetarow_X")
        #print("thetarow_X",thetarow_X)
        theta_X_exp.append(thetarow_X)   ##All numerators for Xi 
        #print("theta_X_exp for Xi",i, " theta_X_exp[Xi][0]",theta_X_exp[i][0], "theta_X_exp[Xi][1]",theta_X_exp[i][0] )
        den=(1 + sumthetaj_X )
        ##print("j", j ,"den",den)
        ##df -denominator.append( den[0][0] ) ##All denominator for Xi
        
        denominator.append( den ) ##All denominator for Xi
        #print("added to denom sumthetaj_X",den)
        denominatori=denominator[i]
        #print("denominatori",denominatori)

        list_prob_thetas_Xi=[]
        list_deltaLog_thetas_Xi=[]
        list_Loss_thetas_Xi=[]
        
        for classi in range (1,classesk+1):
            ##get 1. Probability for Xi -> classi
            ##    2.Calculate Loss_Theta only if class==Yi
            if(classi == classesk):
                numerator=0
                probabilityC_Xtheta=probabilityC_k_XthetaFn( denominatori)
            else:
                numerator=theta_X_exp[i][classi-1]
                probabilityC_Xtheta=probabilityC_XthetaFn(numerator, denominatori)
            
            #print("Xi=",i," theta j=",classi," numerator",numerator,"  denominatori",denominatori,"   probabilityC_Xtheta",probabilityC_Xtheta)
            #print("probabilityC_Xtheta",probabilityC_Xtheta)

            ##df-list_prob_thetas_Xi.append(probabilityC_Xtheta[0][0])
            list_prob_thetas_Xi.append(probabilityC_Xtheta)
            
            ## get the deltaL_Theta_P using the probability
            deltaLog_thetaC=getDeltaLog_ThetaC(probabilityC_Xtheta, Xi_,Yi,classi)
            sumdeltaLogP_thetai=delta_thetaframes_sum[classi]
            ##df - sum=np.add(deltaLog_thetaC,sumdeltaLogP_thetai.values)
            sum=np.add(deltaLog_thetaC,sumdeltaLogP_thetai)
            if classi in delta_thetaframes_sum:
                del delta_thetaframes_sum[classi]
                
            delta_thetaframes_sum[classi]=sum
        
        ##Loop for classes ends 
        list_prob_thetas_X.append(list_prob_thetas_Xi) ##i = Xi , j=(classi=Yi)
    
    #for loop for batch ends
    
    for classi in range (1,classesk+1):
        ##Calculate thetaC and update thetaC
        thetaC=thetaframes[classi]
        deltaLog_Thetasum=delta_thetaframes_sum[classi]
        batchsize_= 1/ batchsize
        deltaL_Theta_=deltaLog_Thetasum.values * batchsize_
        deltaL_Theta_=deltaL_Theta_ * (-1)## ∂L/∂θc
        ##print("deltaLog_Thetasum.values",deltaLog_Thetasum.values.shape)
        #print(nn,"nn")
        ##print("thetaC",thetaC.shape)
        nn_= 1/ nn
        ##print("nn_",nn_)
        deltaTheta= deltaL_Theta_ * nn_ 
        newTheta_c=np.subtract(thetaC , ( deltaTheta ))
        
        
        ##print("old",thetaC)
        ##print("new",newTheta_c)
        if classi in thetaframes:
            del thetaframes[classi]
            #print("Remove")
        thetaframes[classi]=newTheta_c
        
    ##print("complete batch : thetaframes")
    ##print(thetaframes)
    return list_prob_thetas_X,thetaframes

def getDeltaLog_ThetaC(probabilityC_Xtheta, Xi,Yi,classi):
    indicator=indicatorFn(Yi,classi)
    #print("probability" ,probabilityC_Xtheta, " indicator " ,indicator)
    prob_indi=indicator - probabilityC_Xtheta
    #print("prob_indi",prob_indi)
    #print("Xi",Xi)
    deltaLog_ThetaC=(prob_indi ) * Xi
    #print("deltaLog_ThetaC:", deltaLog_ThetaC)
    
    return deltaLog_ThetaC

def accuracy(thetaframes, Xj, Y, n , k,classesk):
    
    Xj=Xj.values
    sum=0
    #Xprobabilities=pd.DataFrame(columns=['Id','Category'])
    for i in range(n):
        ##Get the theta1-4 X for all
        #print("Xj",Xj.shape)
        Xi=Xj[i]
        #print("Xi",Xi.shape)
        Xi_T=Xi.transpose()
        sumDenom=0
        numerator=[]
    
        ##Get numerator and denominator
        for j in range(1,classesk):
            thetaj=thetaframes[j]
            theta_X=np.dot(thetaj,Xi_T)
            #theta_X=(thetaj*Xi_T)
            expo_thetaX=np.exp(theta_X)
            #print(expo_thetaX)
            numerator.append(expo_thetaX)
            sumDenom=np.add(sumDenom, expo_thetaX)
     
        denom=1 + sumDenom
        #print("denom",denom)
        ##Get probability of each class and get max
        max=-999999
        maxClass=0
        for j in range(1,classesk+1):
            if(j == classesk):
                prob_thetaj= 1 / denom
            else:
                num=numerator[j-1]
                prob_thetaj= num / denom
            #print("prob_thetaj",prob_thetaj)
            if(prob_thetaj > max):
                max=prob_thetaj
                maxClass=j
        Yi=Y.iloc[i][1]## get cell - Y row
        
        if(Yi == maxClass ):
            sum+=1
    
    accuracy=sum/n
        #Xprobabilities=Xprobabilities.append({'Id': i, 'Category': maxClass}, ignore_index=True)
    ##i finishes
    ##print(Xprobabilities)
    return accuracy

train_labels0 = pd.read_csv("/kaggle/input/sorteddatasetml3/Train_Labels-sort.csv")
train_features0 = pd.read_csv("/kaggle/input/sortcolumnheader-added/Train_Features-sort1.csv") 

val_labels0 = pd.read_csv("/kaggle/input/sorteddatasetml3/Val_Labels-sort.csv")
val_features0 = pd.read_csv("/kaggle/input/sortcolumnheader-added/Val_Features-sort1.csv") 

test_features0 = pd.read_csv("/kaggle/input/sortcolumnheader-added/Test_Features-sort1.csv")


#n=X_.shape[0] ## numer of samples -rows
#k=X_.shape[1] ## number of features - column
#print(k)
#print(n)

##def getTrainMethod(train_features0,train_labels0):
Y_=pd.DataFrame(train_labels0)
#print(train_labels0)
#print("Y_", Y_.head())
print("Train")
#print(train_features0.head())
#print(train_labels0.head())

    
train_X=pd.DataFrame(train_features0.values)


n=train_X.shape[0] ## numer of samples -rows
k=train_X.shape[1] ## number of features - column


X1_=pd.DataFrame(train_X)

One_nx1=np.ones((n, 1))
one_column=pd.DataFrame(One_nx1)

Xbar= concatenateHorizontally(X1_,one_column)

X_all=Xbar.values
X_=X_all##[0:50, :]
X_=pd.DataFrame(X_)
    
thetaloglist,epochlist,thetaframes,accuracyList = sgd_function(16,  0.1, 1 , 100, 0.00001, X_, Y_)

##m_batchsize=16,  η0, η1 , max_epoch=100, δ

epochlist

val_features0.head()
val_X=val_features0
n=val_X.shape[0] ## numer of samples -rows
k=val_X.shape[1] ## number of features - column


valX1_=pd.DataFrame(val_X)

One_nx1=np.ones((n, 1))
one_column=pd.DataFrame(One_nx1)

valXbar= concatenateHorizontally(valX1_,one_column)

valX_=valXbar
valX_.head()

valY_=pd.DataFrame(val_labels0)


thetaloglist_val,epochlist_val,thetaframes_val = sgd_function(16,  0.1, 1 , 100, 0.00001, valX_, valY_)

classesk=4
print(test_features0.head())
test_X=test_features0
n=test_X.shape[0] ## numer of samples -rows
k=test_X.shape[1] ## number of features - column


testX1_=pd.DataFrame(test_X)

One_nx1=np.ones((n, 1))
one_column=pd.DataFrame(One_nx1)

testXbar= concatenateHorizontally(testX1_,one_column)

testX_=testXbar
testXnorm=np.linalg.norm(testX_)
testX_norm=testX_ / testXnorm
testX=testX_norm
testX=testX.values

print("thetaframes",thetaframes)

Xprobabilities=pd.DataFrame(columns=['Id','Category'])
for i in range(n):
    ##Get the theta1-4 X for all
    Xi=testX[i]
    Xi_T=Xi.transpose()
    sumDenom=0
    numerator=[]
    
    ##Get numerator and denominator
    for j in range(1,classesk):
        thetaj=thetaframes[j]
        theta_X=np.dot(thetaj,Xi_T)
        #theta_X=(thetaj*Xi_T)
        expo_thetaX=np.exp(theta_X)
        print(expo_thetaX)
        numerator.append(expo_thetaX)
        sumDenom=np.add(sumDenom, expo_thetaX)
     
    denom=1 + sumDenom
    print("denom",denom)
    ##Get probability of each class and get max
    max=-999999
    maxClass=0
    for j in range(1,classesk+1):
        if(j == classesk):
            prob_thetaj= 1 / denom
        else:
            num=numerator[j-1]
            prob_thetaj= num / denom
        print("prob_thetaj",prob_thetaj)
        if(prob_thetaj > max):
            max=prob_thetaj
            maxClass=j
    Xprobabilities=Xprobabilities.append({'Id': i, 'Category': maxClass}, ignore_index=True)
##i finishes
print(Xprobabilities)

a=pd.DataFrame(Xprobabilities)
a.to_csv("testLabels1.csv", index = False)

import seaborn as sns; 
sns.set()
import matplotlib.pyplot as plt

##Plot the curve showing L(θ) as a function of epoch
print(thetaloglist)
print(epochlist)



plt.plot(epochlist,thetaloglistn , 'b', linewidth=2, markersize=12,label='L(θ) as a function of epoch')
plt.title('Question1 : L(θ) as a function of epoch')
plt.xlabel('epoch')
plt.ylabel('L(θ)')
 

plt.show()

##Report the values of (η0, η1). How many epochs does it take? What is the final value of L(θ)?

##l=0.2269

plt.plot(epochlist1,thetaloglist_train1 , 'b', linewidth=2, markersize=12,label='L(θ) as a function of epoch')
plt.title('Question2 : L(θ) as a function of epoch')
plt.xlabel('epoch')
plt.ylabel('L(θ)')
 
plt.legend()
plt.show()

##Performance





plt.plot( epochlist1, thetaloglist_train1, markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,label='Training')
plt.plot( epochlist, thetaloglist_train, markerfacecolor='red' ,markersize=12, color='orange', linewidth=3, label='Validation')
plt.legend()