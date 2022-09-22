#FAZENDO UMA CONSULTA DE DADOS EM UMA API: O ARQUIVO RETORNA EM FORMATO JSON E CONVERTE PARA UM DICIONARIO
import matplotlib.pyplot as plt
import requests

url= 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)
response_dict = r.json()

########################ISSO RETORNA AS INFORMAÇÕES DENTRO DO MEU DICIONARIO
print("Total de repositorios:",response_dict['total_count'])

respo_dict = response_dict['items']
print("Repositorios retornados:",len(respo_dict))



title= "Projetos favoritos de JS"
plt.title(title)
names,stars = [],[]
x = []
y = []
legenda = []
for repo_dict in respo_dict:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
if len(names) >= 0 and len(stars) <= 30:
    x.append(repo_dict['name'])
    y.append(repo_dict['stargazers_count'])
    legenda.append(repo_dict['html_url'])
plt.ylabel("Estrelas")
plt.legend()
plt.xlabel(legenda)
plt.bar(x,y)
plt.show()
#print("\nChaves:",len(repo_dict))
#for key in sorted(repo_dict.keys()):
 #   print(key)

####################
