frase=input("Escribe una frase o palabra")
def reverse_string(string):
    return string[::-1]
print(frase)

#frase inversa
ifrase= reverse_string (frase)

#quitar espacios
frase=frase.replace(" ","")
print(frase)
ifrase=ifrase.replace(" ","")
print(ifrase)

#determinar palindromo
if frase == ifrase:
    print("Es palindromo")
else: 
    frase != ifrase 
    print("No es palindromo")
