
import matplotlib.pyplot as plt
first_pay = int(input("Enter The Amount You Want to Invest With : >> "))
starting_point =  [first_pay]
Company_profit_month=[]
Ceo = []
technical_manager_ai=[]
technical_manager_web=[]
technical_team=[]
total_input=[]
upwork=[]
#130$ total / Job    5 for every 100
for i in range(6):
    total_input.append(int((starting_point[i] - 20) * 0.05) * 130)
    technical_team.append(int((starting_point[i] - 20) * 0.05) * 130 * 0.4)
    upwork.append(int((starting_point[i] - 20) * 0.05) * 130 * 0.2)
    starting_point.append(int((starting_point[i] - 20) * 0.05) * 130 * 0.18)
    Company_profit_month.append(int((starting_point[i] - 20) * 0.05) * 130 * 0.08)
    Ceo.append(int((starting_point[i] - 20 )* 0.05) * 130 * 0.06)
    technical_manager_ai.append(int((starting_point[i] - 20 )* 0.05) * 130 * 0.04)
    technical_manager_web.append(int((starting_point[i] - 20) * 0.05) * 130 * 0.04)



print("total Money Excpected to Get From Upwork >> " ,total_input)
print("total input in 6 Months >> " ,sum(total_input))

print("=================================================================")

print(f"Money Expected to Have  : - ({first_pay}$ / Month) Investor >> " ,starting_point[1:])
print("Total Investor Profit after 6 Months >> ", sum(starting_point[1:])-(6*first_pay))
print("Net Profit after 6 Months >>",(sum(starting_point[1:])-(6*first_pay))-first_pay)
print("=================================================================")

print("Technical team Money >> ",technical_team)
print("Technical team total Money in 6 Monthes >> ",sum(technical_team))

print("=================================================================")

print("Upwork  >> ",upwork)
print("Total Upwork Money in 6 Monthes >> ",sum(upwork))
print("=================================================================")

print("Company Profit >> ",Company_profit_month)
print("Total Company Money in 6 Monthes >> ",sum(Company_profit_month))
print("=================================================================")

print("Ceo Profit >>  ",Ceo)
print("Total CEO Money in 6 Monthes >> ",sum(Ceo))
print("=================================================================")

print("Technical Manager  >> ",technical_manager_ai)
print("Total Technical Managers Money in 6 Monthes >> ",sum(technical_manager_ai)*2)
print("=================================================================")




plt.plot(starting_point,label="Investor")
#plt.plot(upwork,label="Upwork")
plt.plot(Company_profit_month,label="Company")
plt.plot(Ceo,label="Ceo")
plt.plot(technical_manager_ai,label="Technical Manager")

plt.legend()
plt.xlabel('Months')
plt.ylabel('Profit')
plt.show()
#




