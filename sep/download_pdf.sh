#!/bin/zsh
#
#./02_download_pdf.sh
#
cd sep_pdf
scrapy crawl -a mekler=http://www.sep.gob.mx/es/sep1/FAEB#.U_F8AnWx3UY -s MONGODB_COLLECTION=primer_trimestre_2013 sep_crawler_gral
scrapy crawl -a mekler=http://www.sep.gob.mx/es/sep1/Fondo_de_Aportaciones_para_la_Educacion_Basica_y_Normal_FAEB#.U_F_yP6A8qU -s MONGODB_COLLECTION=segundo_trimestre_2013 sep_crawler_gral
scrapy crawl -a mekler=http://www.sep.gob.mx/es/sep1/Fondo_de_Aportaciones_para_la_educacion_Basica_y_Normal_FAEB#.U_GE3f6A8qU -s MONGODB_COLLECTION=tercer_trimestre_2013 sep_crawler_gral
scrapy crawl -a mekler=http://sep.gob.mx/es/sep1/Fondo_de_Aportaciones_para_la_educacion_Basica_y_Normal_FAEB_#.U_GASP6A-Mk -s MONGODB_COLLECTION=cuarto_trimestre_2013 sep_crawler_gral
scrapy crawl -a mekler=http://www.sep.gob.mx/es/sep1/Fondo_de_Aportaciones_para_la_Educacion_Basica_y_Normal_FAEB_2014#.U_F8x3Wx3UY -s MONGODB_COLLECTION=primer_trimestre_2014 sep_crawler_gral

cd ..
for folder in primer_trimestre_2013 segundo_trimestre_2013 tercer_trimestre_2013 cuarto_trimestre_2013 primer_trimestre_2014
do
	mkdir -p $folder
	python 01_get_pdf_from_mongo.py sep_pdf $folder | parallel -j+0 --eta wget -P $folder http://sep.gob.mx{}
done