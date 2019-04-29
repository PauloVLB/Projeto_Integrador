#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author isaacmsl
import sys
import os
import xml.etree.cElementTree as ET

def rename():

	param = sys.argv[1:]

	if len(param) == 2:
		antigo_diretorio = os.getcwd() + "/" + param[0]

		if os.path.exists(antigo_diretorio):
			
			novo_diretorio = antigo_diretorio.replace(param[0], param[1]) # muda pra novo diretorio

			try:
				os.rename(param[0], param[1])

				inside = os.path.join(novo_diretorio)

				arquivos = os.listdir(inside)

				indexCMakeLists = arquivos.index("CMakeLists.txt")
				indexPackage = arquivos.index("package.xml")

				cmakelists = open(novo_diretorio+"/"+arquivos[indexCMakeLists], "r")
				package = open(novo_diretorio+"/"+arquivos[indexPackage], "r")
			
				linescmakelists = cmakelists.readlines()
			
				linespackage = package.readlines()

				# CMakeLists editing
				
				try: 
					index = linescmakelists.index("project("+param[0]+")\n")
				except:
					if "project(" in linescmakelists[1]:
						index = 1
					else:
						raise

				linescmakelists[index] = "project("+param[1]+")\n"
							





				
				try:
					index = linescmakelists.index("#  LIBRARIES "+param[0] + "\n")
				except:
					if "#  LIBRARIES " in linescmakelists[104]:
						index = 104
					else:
						raise
				linescmakelists[index] = "#  LIBRARIES "+param[1] + "\n"






				
				try:
					index = linescmakelists.index("#   src/$"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"/"+param[0]+".cpp"+ "\n")
				except:
					if "#   src/$"+u"\u007b"+"PROJECT_NAME"+u"\u007d" in linescmakelists[122]:
						index = 122
					else:
						raise
				linescmakelists[index] = "#   src/$"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"/"+param[1]+".cpp"+ "\n"







				try:
					index = linescmakelists.index("# add_executable($"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"_node src/"+param[0]+"_node.cpp)"+ "\n")
				except:
					if "# add_executable($"+u"\u007b" in linescmakelists[133]:
						index = 133
					else:
						raise
				linescmakelists[index] = "# add_executable($"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"_node src/"+param[1]+"_node.cpp)"+ "\n"






				
				try:
					index = linescmakelists.index("# catkin_add_gtest($"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"-test test/test_"+param[0]+".cpp)"+ "\n")
				except:
					if "# catkin_add_gtest($" in linescmakelists[190]:
						index = 190
					else:
						raise
				linescmakelists[index] ="# catkin_add_gtest($"+u"\u007b"+"PROJECT_NAME"+u"\u007d"+"-test test/test_"+param[1]+".cpp)"+ "\n"
				





				

				# Package editing
				
				arquivo = novo_diretorio+"/"+arquivos[indexPackage]
				tree =  ET.parse(arquivo)
				root = tree.getroot()

				for name in root.iter('name'):
					name.text = param[1]

				tree.write(novo_diretorio+"/"+arquivos[indexPackage])

				
				# Salvando alterações
				gravar = open(novo_diretorio+"/"+arquivos[indexCMakeLists], "w")
				gravar.writelines(linescmakelists)
				gravar.close()
				
				print('Renomeado com sucesso!')
		
			except:
				print('Erro durante o processo. ;-;')
				os.rename(param[1], param[0])
			
		else:
			print("Diretório " + "'" + param[0] + "'" + " não existe.")
	else:
		raise
	
if __name__ == "__main__":
	try:
		rename()
	except:
		print("Erro ao tentar renomear :(")

