#Exam 2 pt 2

import csv
from collections import Counter
import random


#initialize empty lists for count
Height = []
Weight = []
Sex = []
Age = []
Name = []
Home_State = []
Annual_Purchases = []

data = []


first_names = [
"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah",
"Ivy", "Jack",
"John", "Kate", "Liam", "Olivia", "Mason", "Sophia", "Noah", "Ava",
"Lucas", "Zoe",
"Emma", "William", "James", "Oliver", "Ella", "Sophia", "Mia",
"Charlotte", "Abigail",
"Ethan", "Daniel", "Michael", "Benjamin", "Matthew", "Alexander",
"Grace", "Lily", "Chloe",
"Emily", "Evelyn", "Scarlett", "Lucy", "Sophie", "Ella", "Liam",
"Noah", "Logan", "Jacob",
"Elijah", "Carter", "Samuel", "Henry", "Sebastian", "David",
"Michael", "Christopher",
"Joseph", "Gabriel", "Daniel", "Anthony", "Isabella", "Sofia", "Aria",
"Grace", "Lily",
"Mia", "Zoe", "Camila", "Emily", "Madison", "Luna", "Ella", "Avery",
"Scarlett", "Lucy",
"Penelope", "Chloe", "Riley", "Evelyn", "Abigail", "Emma",
"Charlotte", "Elijah", "Henry",
"Leo", "James", "Benjamin", "Samuel", "David", "Matthew", "Joseph",
"Daniel", "Nicholas",
"Liam", "William", "Oliver", "Aiden", "Ethan", "Lucas", "Logan",
"Alexander", "Gabriel",
"Jackson", "Sebastian", "Ezekiel", "Daniel", "Eleanor", "Madeline",
"Sophia", "Alice",
"Ella", "Hannah", "Grace", "Lily", "Mia", "Avery", "Charlotte",
"Penelope", "Riley",
]
last_names = [
"Smith", "Johnson", "Brown", "Davis", "Wilson", "Lee", "Wong",
"Taylor", "Clark", "Martin",
"Harris", "Miller", "Anderson", "Jones", "Moore", "Williams", "White",
"Walker", "Thomas", "King",
"Lewis", "Hill", "Young", "Scott", "Green", "Hall", "Adams", "Baker",
"Evans", "Parker",
"Garcia", "Martinez", "Rodriguez", "Hernandez", "Lopez", "Gonzalez",
"Wilson", "Turner", "Robinson", "Perez",
"Thomas", "White", "Anderson", "Jackson", "Harris", "Sanchez",
"Ramirez", "Rivera", "Campbell", "Parker",
"Bennett", "Wood", "Coleman", "Gray", "Mitchell", "Rogers", "Scott",
"Stewart", "Bryant", "Russell",
"Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham", "Sullivan",
"Wallace", "Powell", "Carter",
"Reed", "Morgan", "Cooper", "Murphy", "Reed", "Ross", "Edwards",
"Murray", "Spencer", "Watson",
"Harrison", "Foster", "Morgan", "Simpson", "Dixon", "Neal", "Russell",
"Willis", "Burns", "Howard","Alexander", "Gardner", "Warren", "Carroll", "Hansen", "Black",
"Weaver", "Sharp", "Wheeler", "Collins",
"Price", "Morris", "Murphy", "Bennett", "Wood", "Coleman", "Gray",
"Mitchell", "Rogers", "Scott", "Stewart",
"Bryant", "Russell", "Diaz", "Hayes", "Myers", "Ford", "Hamilton",
"Graham", "Sullivan", "Wallace", "Powell",
"Carter", "Reed", "Morgan", "Cooper", "Murphy", "Reed", "Ross",
"Edwards", "Murray", "Spencer", "Watson",
"Harrison", "Foster", "Morgan", "Simpson", "Dixon", "Neal", "Russell",
"Willis", "Burns", "Howard",
]
home_state = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT',
'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
sex = ['M','F']



def distribution():
    try: #error handling
        with open('synthetic_data-2.csv') as file: #open file
            reader = csv.reader(file, delimiter=',') #read file
            line_count = 0 #initialize line counter
            
            for row in reader: # create loop to go through each row of the file
                data.append(row) # fill list with entire file data
                if line_count == 0: #skip header
                    line_count += 1
                else: #create and fill lists for each field
                    
                    Height.append(row[0])
                    Weight.append(row[1])
                    Sex.append(row[2])
                    Age.append(row[3])
                    Name.append(row[4])
                    Home_State.append(row[5])
                    Annual_Purchases.append(row[6])

            print('Frequency of values: ') #Count values and print frequencies
            Heightc = Counter(Height)
            print(f'Height: {Heightc}')
            Weightc = Counter(Weight)
            print(f'Weight: {Weightc}')
            Sexc = Counter(Sex)
            print(f'Sex: {Sexc}')
            Agec = Counter(Age)
            print(f'Age: {Agec}')
            Home_Statec = Counter(Home_State)
            print(f'Home State: {Home_Statec}')
            Annual_Purchasesc = Counter(Annual_Purchases)
            print(f'Annual Purchases: {Annual_Purchasesc}')
            
            return data, Height, Weight, Sex, Age, Home_State, Annual_Purchases
    except Exception as a:
        print('Error: {a}')

def randsample(): #generate a random sample of data within the range provided
    Height_Sample = random.choice(Height)
    Weight_Sample = random.choice(Weight)
    Sex_Sample = random.choice(Sex)
    Age_Sample = random.choice(Age)
    Home_State_Sample = random.choice(Home_State)
    Annual_Purchases_Sample = random.choice(Annual_Purchases)
    print(Height_Sample)
    print(Weight_Sample)
    print(Sex_Sample)
    print(Age_Sample)
    print(Home_State_Sample)
    print(Annual_Purchases_Sample)
    

def generatename(first_names, last_names): #generate name for additional entries
    firstname = random.choice(first_names)
    lastname = random.choice(last_names)
    fullname = lastname + ', ' + firstname
    return fullname

filepath = 'synthetic_data_set_2.csv' #create new file

def inputrecords(): 
    try: #error handling
        user_input = int(input('How many records would you like to enter? ')) #Ask user how many rows they would like
        if user_input > -0.5:
            for number in range(user_input): #Synthetic data generation copied from pt 1
                Height1 = random.randint(55,80)
                Weight1 = random.randint(90,300)
                Sex1 = random.choice(sex)
                Age1 = random.randint(18,99)
                Name1 = generatename(first_names, last_names)
                Home_State1 = random.choice(home_state)
                Annual_Purchases1 = round(random.uniform(-500.00,5000.00), 2)

                data.append([Height1, Weight1, Sex1, Age1, Name1, Home_State1, Annual_Purchases1])
            return data
        else:
            print('Invalid Input')
    except Exception as a:
        print(f'Error {a}')

def buildfile(data): #Write Synthetic data + Additional rows into new file
    with open(filepath, 'w', newline= '') as file:
        
        writer = csv.writer(file, delimiter=',')
        
        writer.writerows(data)
        print('File Updated')

def main(): #call functions in order
    distribution()
    #print(f'data: {data}')
    print('Random sample:')
    randsample()
    inputrecords()
    buildfile(data)
   
    
    

main() #call main
    
    
            
