Ability.txt -> Skills.txt: La tabla "Ability" está relacionada con la tabla "Skills" a través del campo "ONET-SOC Code".
Interest.txt -> WorkActivity.txt: La tabla "Interest" está relacionada con la tabla "WorkActivity" a través del campo "ONET-SOC Code".
Job_zone_reference (SP).txt -> Onetsoc_job_zones.txt: La tabla "Job_zone_reference" está relacionada con la tabla "Onetsoc_job_zones" a través del campo "Job Zone".
Knowledge.txt -> Skills.txt: La tabla "Knowledge" está relacionada con la tabla "Skills" a través del campo "ONET-SOC Code".
Onet_content_model_reference (SP).txt -> Todos los demás archivos: La tabla "Onet_content_model_reference" es una tabla de referencia que explica los diferentes modelos de contenido utilizados en los archivos de O*NET.
Onetsoc_data (SP).txt -> Todos los demás archivos: La tabla "Onetsoc_data" es la tabla principal que contiene información detallada sobre las ocupaciones. Se relaciona con todas las demás tablas a través del campo "ONET-SOC Code".
Onetsoc_job_zones.txt -> Onetsoc_data (SP).txt: La tabla "Onetsoc_job_zones" está relacionada con la tabla "Onetsoc_data" a través del campo "ONET-SOC Code".
Scales_reference (SP).txt -> Todos los demás archivos: La tabla "Scales_reference" es una tabla de referencia que explica las diferentes escalas utilizadas en los archivos de O*NET.
Skills.txt -> Tasks (SP).txt: La tabla "Skills" está relacionada con la tabla "Tasks" a través del campo "ONET-SOC Code".
Tasks (SP).txt -> Onetsoc_data (SP).txt: La tabla "Tasks" está relacionada con la tabla "Onetsoc_data" a través del campo "ONET-SOC Code".
WorkActivity.txt -> WorkContext.txt: La tabla "WorkActivity" está relacionada con la tabla "WorkContext" a través del campo "ONET-SOC Code".
WorkContext.txt -> Onetsoc_data (SP).txt: La tabla "WorkContext" está relacionada con la tabla "Onetsoc_data" a través del campo "ONET-SOC Code".
WorkValue.txt -> Onetsoc_data (SP).txt: La tabla "WorkValue" está relacionada con la tabla "Onetsoc_data" a través del campo "ONET-SOC Code".