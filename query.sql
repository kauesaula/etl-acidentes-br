-- O objetivo desta query é identificar a volumetria diária de acidentes rodoviários em SP utilizando a base limpa da Camada Prata para suporte à tomada de decisão
SELECT 
    data_inversa, 
    COUNT(*) as total_acidentes
FROM 
    acidentes_sp_clean
GROUP BY 
    data_inversa
ORDER BY 
    data_inversa;