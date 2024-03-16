from scipy.stats import chi2

def Chi2(Forecast):
    """
    Calcule la statistique du chi-deux et la p-value correspondante
    à partir des fréquences observées et attendues.

    Args:
    - data: Une liste ou un tableau numpy contenant les fréquences observées.
    - Forecast: Une liste ou un tableau numpy contenant les fréquences attendues.

    Returns:
    - chi_carre_stat: La valeur de la statistique du chi-deux.
    - p_value: La p-value correspondante.
    """
    dataList = [99.8, 101.0, 89.1, 71.8, 72.3, 78.1, 72.5, 74.1, 80.4, 81.8, 76.9, 80.7, 79.0, 76.8, 84.9, 88.3, 82.9, 85.5, 81.2, 70.3, 72.8, 71.7, 67.4, 70.6, 67.2, 62.8, 59.4, 65.2, 58.4, 50.0, 51.5, 58.2, 58.6, 59.9, 56.8, 59.7, 64.9, 67.0, 62.0, 63.5, 59.2, 64.4, 71.6, 69.5, 68.1, 63.8, 61.3, 69.7, 79.0, 76.9]
    print()
    ForecastList = [76.9, 76.9]
    #float(Forecast)

    print(ForecastList)


    # Calculate chi-square statistic
    dof = len(dataList) - 1
    chi_carre_stat = sum((o - e) ** 2 / e for o, e in zip(dataList, ForecastList))
    
    # Calculate p-value
    p_value = 1 - chi2.cdf(chi_carre_stat, dof)

    print(f"Statistique du Khy² : {chi_carre_stat}")
    print(f"P-value : {p_value}")
    