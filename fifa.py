import random
clubs = ["Arsenal", "Aston Villa", "Leicester City","Chelsea","Everton","Manchester City","Manchester Utd","Spurs","Paris SG","FC Bayern","Dortmund","Inter","juventos","Roma FC","Milan","Lazio",
         "Soccer Aid","adidas All-Star","Barcelona","Atlético de Madrid","Real Madrid"]
NATIONAL=["Argentina","Belgium","Brazil","England","France","Germany","Italy","Portugal","Spain","Uruguay"]
all=['Arsenal', 'Aston Villa', 'Leicester City', 'Chelsea', 'Everton', 'Manchester City', 'Manchester Utd', 'Spurs', 'Paris SG', 'FC Bayern', 'Dortmund', 'Inter', 'juventos', 'Roma FC', 'Milan', 'Lazio', 'Soccer Aid', 'adidas All-Star', 'Barcelona', 'Atlético de Madrid', 'Real Madrid', 'Argentina', 'Belgium', 'Brazil', 'England', 'France', 'Germany', 'Italy', 'Portugal', 'Spain', 'Uruguay']

def club():
    num = random.randrange(0, len(clubs))
    num2 = random.randrange(0, len(clubs))
    print(clubs[num])
    print(clubs[num2])
def NATIONAl():
    num1 = random.randrange(0, len(NATIONAL))
    num3 = random.randrange(0, len(NATIONAL))
    print(NATIONAL[num1])
    print(NATIONAL[num3])
def All():
    num1 = random.randrange(0, len(all))
    num3 = random.randrange(0, len(all))
    print(all[num1])
    print(all[num3])
x=input("please enter a number 1/2/3 1=club||2=country||3=||shufel\n")
if x=="1":
    club()
if x=="2":
    NATIONAl()
if x=="3":
    All()