#!/bin/bash

funcion() { 
	
	echo "Por ciclo se le agregará un punto de valor al número que ingreses, hasta que llegue a 10 se imprimirá"
	read -p "ingresa un valor entre 1 y 9: " valor

	while [ $valor -le 10 ]; do
		echo $valor
		valor=$(($valor + 1))
		
	done

	if [[ $valor -eq 10 ]]
	then
		echo "Valor alcanzado: 10"
	fi
}

funcion
