TempSegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = TempSegundos // 3600
segundosrestantes = TempSegundos % 3600
minutos = segundosrestantes // 60
segs_final = segundosrestantes % 60
horas_rest = horas % 24
dia = horas // 24
print(dia,"dias",horas_rest,"horas",minutos,"minutos e",segs_final,"segundos.")
 
