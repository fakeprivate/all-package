import pyfiglet
import shutil
import importlib.metadata

terminal_width = shutil.get_terminal_size().columns
print(pyfiglet.figlet_format("T - tool"))

while True:
	print("="*terminal_width)
	
	v1 = input("Посмотреть все установленые пакеты? [Y/N]:")
	
	if v1 == "Y":
		distributions = importlib.metadata.distributions()
		
		installed_packages_list = []
	
		for dist in distributions:
		    name = dist.metadata.get('Name', 'Unknown')
		    version = dist.version
		    installed_packages_list.append((name, version))
		
		installed_packages_list.sort(key=lambda x: x[0].lower())
		
		package = "\n".join([f"{name}=={version}" for name, version in installed_packages_list])
	
		total = len(installed_packages_list)
	
		print(f"""
	{package}
	
Всего: {total}""")
	else:
		print("Программа завершается...")
		break
