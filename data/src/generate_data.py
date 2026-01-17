import random
import csv

file_path = "../data/internship_data.csv"

headers = [
    "cgpa",
    "num_projects",
    "dsa_level",
    "tech_stack_count",
    "hackathon",
    "shortlisted",
]

def decide_shortlisting(cgpa, projects, dsa, tech_stack_count, hackathon):
    score = 0

    if cgpa > 8.0:
        score += 2
    elif cgpa >= 6.5:
        score += 1

    if projects >= 3:
        score += 2
    elif projects >= 1:
        score += 1

    if dsa >= 2:
        score += 2

    if tech_stack_count >= 3:
        score += 1

    if hackathon == 1:
        score += 1

    score += random.choice([0, 1])

    return 1 if score >= 5 else 0


rows = []

for _ in range(200):
    cgpa = round(random.uniform(5.5, 9.5), 2)
    projects = random.randint(0, 5)
    dsa = random.randint(0, 3)
    tech_stack_count = random.randint(1, 6)
    hackathon = random.choice([0,1])

    shortlisted = decide_shortlisting(cgpa, projects, dsa, tech_stack_count, hackathon)

    rows.append([cgpa, projects, dsa, tech_stack_count, hackathon, shortlisted])


with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Dataset generated successfully")

