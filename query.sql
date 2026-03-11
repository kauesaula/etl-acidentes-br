SELECT 
    data_inversa, 
    COUNT(*) as total_acidentes
FROM 
    acidentes_sp_clean
GROUP BY 
    data_inversa
ORDER BY 
    data_inversa;