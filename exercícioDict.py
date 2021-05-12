casos = {

'Auxiliar de radiologia' :570,

'Condutor de ambulância' :649,

'Técnicos de laboratórios de saúde e bancos de sangue' :480,

'Terapeutas ocupacionais, ortoptistas e psicomotricistas' :244,

'Biólogos e afins' :192,

'Socorristas (exceto médicos e enfermeiros)' :212,

'Pesquisadores das ciências biológicas' :148,

'Profissionais da biotecnologia' :134,

'Agentes da saúde e do meio ambiente' :147,

'Gestores e especialistas de operações em empresas, secretarias e unidades de serviços de saúde' :146,

'Tecnólogos e técnicos em terapias complementares e estéticas' :123,

'Técnicos em segurança do trabalho' :122,

'Trabalhadores em registros e informações em saúde' :114,

'Professores' :104,

'Trabalhadores de laboratório fotográfico e radiológico':100,

'Outros profissionais de ensino' :110,

'Tecnólogos e técnicos em métodos de diagnósticos e terapêutica' :82,

'Operadores de telefonia' :60,

'Físicos' :31,

'Trabalhadores de atenção, defesa e proteção a pessoas em situação de risco e adolescentes em conflito com a lei' : 40,

'Pesquisadores das ciências da saúde' :32,

'Musicoterapeuta, arteterapeuta, equoterapeuta ou naturólogo' :22,

'Técnicos em próteses ortopédicas' :19,

'Químicos' :24,

'Técnicos em produção, conservação e de qualidade de alimentos': 19,

'Técnicos de imobilizações ortopédicas' :18,

'Técnicos em manutenção e reparação de equipamentos biomédicos' :13,

'Técnicos em óptica e optometria' :15,

'Trabalhadores dos serviços funerários' : 13,

'Doula' :4,

'Técnicos em necrópsia e taxidermistas' : 9,

'Trabalhadores auxiliares dos serviços funerários' :2,

'Técnicos em eletricidade e eletrotécnica' :6,

'Engenheiros de produção, qualidade, segurança e afins' :3,

'Instrutores e professores de cursos livres': 4,

'Técnicos de apoio à biotecnologia' : 5,

'Engenheiros de alimentos e afins': 0,

'Técnicos de apoio à bioengenharia' :2,

'Parteira leiga' :4,

}



print(type(casos))
print(len(casos))
print(casos.keys())
print(casos.values())
print(casos.items())
casos['Médicos'] = 12
print(casos)
del casos['Parteira leiga']
print(casos)

if 'Parteira leiga' in casos.keys():
    casos['Parteira Leiga'] = casos.pop('Parteira leiga')
else:
    print('Não encontrado')
print(casos)


if casos.get('Parteira leiga'):
    casos['Parteira leiga'] = 4.2
print(casos)


if 'Parteira leiga' in casos.keys():
    casos['Parteira Leiga'] = casos.pop('Parteira leiga')
    casos['Parteira Leiga'] = 4.1
print(casos)

print(max(casos.values()))

