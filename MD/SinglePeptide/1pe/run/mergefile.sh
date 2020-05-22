#!/bin/bash

i="$IFS";IFS='/';set -f;p=($4);set +f;IFS="$i"
QMREGION=${p[-2]}
if [ ! -f ${1}.${QMREGION}.out ] && ((${5} != "0")) ; then
	echo "" > ${1}.${QMREGION}.out
elif [ ! -f ${1}.${QMREGION}.out ] && ((${5} == "0" && ${3} != "-1")) ; then
	cat ${4}.out > ${3}.${QMREGION}.out
fi
if ((${5} % ${2} == 0 && ${5} != "0")); then
	cat ${4}.out >> ${1}.${QMREGION}.out
fi
#----
if [ ! -f ${1}.${QMREGION}.mgf ] && ((${5} != "0")) ; then
	echo "" > ${1}.${QMREGION}.mgf
elif [ ! -f ${1}.${QMREGION}.mgf ] && ((${5} == "0" && ${3} != "-1")) ; then
	cat ${4}.mgf > ${3}.${QMREGION}.mgf
fi
if ((${5} % ${2} == 0 && ${5} != "0")); then
	cat ${4}.mgf >> ${1}.${QMREGION}.mgf
fi
#-----
if [ ! -f ${1}.${QMREGION}.aux ] && ((${5} != "0")) ; then
	echo "" > ${1}.${QMREGION}.aux
elif [ ! -f ${1}.${QMREGION}.out ] && ((${5} == "0" && ${3} != "-1")) ; then
	cat ${4}.aux > ${3}.${QMREGION}.aux
fi
if ((${5} % ${2} == 0 && ${5} != "0")); then
	cat ${4}.aux >> ${1}.${QMREGION}.aux
fi
#----
if [ ! -f ${1}.${QMREGION}.arc ] && ((${5} != "0")) ; then
	echo "" > ${1}.${QMREGION}.arc
elif [ ! -f ${1}.${QMREGION}.arc ] && ((${5} == "0" && ${3} != "-1")) ; then
	cat ${4}.arc > ${3}.${QMREGION}.arc
fi
if ((${5} % ${2} == 0 && ${5} != "0")); then
	cat ${4}.arc >> ${1}.${QMREGION}.arc
fi
