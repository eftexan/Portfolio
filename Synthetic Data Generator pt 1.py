#Exam 2 pt 1

# Sample lists of first and last names
import csv
import random

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

def generatename(first_names, last_names):
    firstname = random.choice(first_names)
    lastname = random.choice(last_names)
    fullname = lastname + ', ' + firstname
    return fullname
Header = ['Height (in inches)','Weight (in pounds)', 'Sex', 'Age (in years)', 'Name (last and first)', 'Home State (Abbreviation)', 'Annual Purchases']
data = []
lines = random.randint(50,50000)
#create file
file_path = 'synthetic_data.csv'

def generatedata():
    #error handling
    try:
        
        for line in range(lines):
            Height = random.randint(55,80)
            Weight = random.randint(90,300)
            Sex = random.choice(sex)
            Age = random.randint(18,99)
            Name = generatename(first_names, last_names)
            Home_State = random.choice(home_state)
            Annual_Purchases = round(random.uniform(-500.00,5000.00), 2)
            
            # put generated data in a list
            data.append([Height, Weight, Sex, Age, Name, Home_State, Annual_Purchases])
        return data
    except Exception as a:
        print(f'Error: {a}')
   
def buildfile(data):
    with open(file_path, 'w', newline= '') as file: #open file
        
       writer = csv.writer(file) #create writer
       writer.writerow(Header)
       writer.writerows(data) #write the random data into the file

def main():
    synthetic_data = generatedata() #call function to create data
    print(f'{lines} lines entered') #tell user about update

    buildfile(synthetic_data) # call funtion to fill the file

main()

