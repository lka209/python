altura = float(input('digite sua altura:(m)'))
peso = float(input('digite seu peso:(kg)'))
imc = peso / (altura ** 2)
print('o imc dessa pessoa é {:.1F}'.format(imc))
if imc < 18.5:
    print('esta pessoa está abaixo do seu peso')
elif 18.5 <= imc < 25:
    print('esta pessoa está no seu peso')
elif 25 <= imc < 30:
    print('esta pessoa está com sobrepeso')
elif 30 <= imc < 40:
    print('esta pessoa está obesa')
elif imc >= 40:
    print('esta pessoa está na obesidade mórbida, atenção!')