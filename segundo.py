segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seg = int(segundos_str)

dias = total_seg // 86400
horas_restantes = total_seg% 86400
horas = horas_restantes // 3600
segundos_restantes = total_seg % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(dias, "dias", horas, "horas", minutos, "minutos e", segundos_restantes_final, "segundos.")