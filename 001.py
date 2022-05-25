import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# xlsx=pd.ExcelFile('Mieszkania1.xlsx')
# df=pd.read_excel(xlsx,header=0)
# print(df)
# X=np.arange(4)
# grupa1=(df[df['Formy budownictwa']=='indywidualne'])
# grupa2=(df[df['Formy budownictwa']=='spółdzielcze'])
# grupa3=(df[df['Formy budownictwa']=='komunalne'])
# y1=grupa1['Wartość']
# y2=grupa2['Wartość']
# y3=grupa3['Wartość']
# plt.annotate(xy=[0,69000],text='165937')
# plt.bar(X+0.00, y1,color='red',width=0.25,label='indywidualne')
# plt.bar(X+0.25, y2,color='blue',width=0.25,label='spółdzielcze')
# plt.bar(X+0.50, y3,color='green',width=0.25,label='komunalne')
# labelsbar=np.arange(2015,2019)
# plt.xticks(X+0.25,labelsbar)
# plt.legend()
# plt.savefig('zad2.pdf',format='pdf')
# plt.show()

#
# xlsx=pd.ExcelFile('turystyka1.xlsx')
# df1=pd.read_excel(xlsx,header=0)
# df=df1.T
# print(df)
# grouped=df.groupby(0)
# print(grouped)
#
# wykres=grouped.plot.bar()
# plt.show()


# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
# print(df)
#
# dane=df.groupby(['Rok'])
#
# X=list(dane.groups.keys())
# print(X)
# y= list(dane.agg('Liczba').sum())
# plt.bar(X,y)
# plt.show()

# dane={'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#       'Stolica':['Bruksela','New Delshi','Brasilia','Warszawa'],
#       'Populacja':[11190846, 130317035,207847528,38674547],
#       'Kontynent':['Europa','Azja','Ameryka Poludniowa','Europa']
#       }
# df=pd.DataFrame(dane)
# print(df)
# grupa=df.groupby('Kontynent')
# etykiety=list(grupa.groups.keys())
# wartosc=list(grupa.agg('Populacja').sum())
# plt.bar(x=etykiety,height=wartosc,color=['red','green','blue'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja na kontynentach')
# plt.show()
#
# plt.plot([1,2,3,4],[1,4,9,16],'ro:')
# plt.plot([1,2,3,4],[1,4,9,16],'bo')
# plt.axis([0,6,0,20])
# plt.show()
# x1=np.arange(0,2.02,0.02)
# x2=np.arange(0,2.02,0.02)
#
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x1)
#
# fig,axs=plt.subplots(3,2)
# print((type(fig)))
# print(type(axs))
#
# axs[0,0].plot(x1,y1,'-')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x')
# axs[0,0].set_title('wykres sin(x')
#
# axs[1,1].plot(x2,y2,'g-')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('wykres cos(x)')
# fig.delaxes(axs[0,1])
# plt.show()

# df=pd.read_csv('zamowienia.csv',header=0,sep=";",decimal=".")
# print(df)
# seria=df.groupby('Sprzedawca')['Utarg'].sum()
# print(seria)
# seria.plot(kind="pie",subplots="True")
# plt.show()

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
# print(df)
#
# chlopcy=(df[df.Plec=='M'])
# y1=chlopcy.groupby('Rok')['Liczba'].sum()
# dziewczynki=(df[df.Plec=='K'])
# y2=dziewczynki.groupby('Rok')['Liczba'].sum()
# print(y2)
# print(y1)
# x=np.arange(18)
#
# labelsbar=np.arange(2000,2018)
# plt.figure(figsize=(15, 6))
# plt.xticks(x,labelsbar)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

height1=(20,10,30,8,40,0)
height2=(80,60,40,12,0,0)
x=np.arange(0,6)
y=np.arange(0,141)

plt.bar(x,height1)
plt.bar(x,height2,bottom=height1)
y2=[120,120,120,120,120,120]
plt.plot(x,y2)

plt.show()