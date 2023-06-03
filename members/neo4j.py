from py2neo import Graph


graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456789"))
# create (person:person {name:"erfan", age:22})

# names = "soha rahbar"
# ages = 8
# birthdates = "15/8/1379"
# resumes = "E:/programs/w3schqqool django/resume/mahdi goodarzi resume.pdf"
# certificates = "bachelor"
# phone_numbers = 9109255262
# emails = "erfan@gmail.com"
# department = "engineering"

# query = f"""
#     create (person:person {name:'{name}', age:{age}})
#     """
# query = f"""
# CREATE (person:person {{name:'{name}', age:{age}}})
#     """
# print(query)
# props = f"{name: {names}, age: {ages}}"


# match (d:department {department_name: "programming"})
# create (p:person {fullname: "reza sourosh moghadam", age: 22, birthdate: "15/5/1380", certificate: "bachelor", resume: "felanpath2"})-[:applied_to]->(d)


def create_applicant(names, ages, birthdates, resumes, certificates, emails, phone_numbers, department):
    string = f"{{fullname: '{names}', age: {ages}, birthdate: '{birthdates}', email:'{emails}' , resume: '{resumes}', certificate:'{certificates}', phone_number:'{phone_numbers}'}}"
    print(string)
    query = f"""
    MATCH (d:department {{department_name: '{department}'}})
    CREATE (person:person {string})-[:applied_to]->(d)
    """
    print(query)
    m = graph.run(query)
    print(m)

def all_applicants():
    # MATCH (n:person) RETURN n LIMIT 25
    memb = []
    query = "MATCH (n:person) RETURN n.fullname as fullname, n.age as age"
    print(query)
    result = graph.run(query).data()
    for row in result:
        # print(row)
        memb.append(row)
    return memb
