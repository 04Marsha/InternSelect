import random
import csv

file_path = "../internship_data.csv"

headers = [
    "cgpa",
    "num_projects",
    "dsa_level",
    "tech_stack_count",
    "hackathon",
    "internship_experience",
    "github_activity",
    "deployed_projects",
    "project_complexity",
    "shortlisted",
]

def decide_shortlisting(cgpa, projects, dsa, tech_stack_count, hackathon, internship, github, deployed, complexity):
    score = 0

    if cgpa > 8.5:
        score += 3
    elif cgpa > 7:
        score += 2
    elif cgpa >= 6:
        score += 1

    if projects >= 3:
        score += 2
    elif projects >= 1:
        score += 1

    if dsa >= 2:
        score += 2

    if tech_stack_count >= 4:
        score += 1

    if hackathon == 1:
        score += 1

    if internship == 1:
        score += 3

    if github > 20:
        score += 2
    elif github > 5:
        score += 1

    if deployed == 1:
        score += 2

    if complexity == 3:
        score += 2
    elif complexity == 2:
        score += 1

    score += random.choice([0, 1])

    return 1 if score >= 8 else 0


rows = []

for _ in range(1000):
    cgpa = round(random.uniform(5.5, 9.5), 2)
    projects = random.randint(0, 5)
    dsa = random.randint(0, 3)
    tech_stack_count = random.randint(1, 6)
    hackathon = random.choice([0,1])
    internship_experience = random.choice([0, 1])
    github_activity = random.randint(0, 50)
    deployed_projects = random.choice([0, 1])
    project_complexity = random.randint(1, 3)

    shortlisted = decide_shortlisting(
        cgpa, 
        projects, 
        dsa, 
        tech_stack_count, 
        hackathon, 
        internship_experience, 
        github_activity, 
        deployed_projects, 
        project_complexity
    )

    rows.append([
        cgpa, 
        projects, 
        dsa, 
        tech_stack_count, 
        hackathon,
        internship_experience, 
        github_activity, 
        deployed_projects, 
        project_complexity, 
        shortlisted
    ])


with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Dataset generated successfully")

