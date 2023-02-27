def fill_data(valeurs_entree, synopsis, titre, data):
    for valeur_entree in valeurs_entree:
        for i in data.columns:
            parts = i.rsplit('_', 1)
            if len(parts) == 2 and valeur_entree == parts[1]:
                row_index = 0  # assume there is only one row in the DataFrame
                column_name = i
                data.at[row_index, column_name] = 1

    data['Synopsis'] = synopsis
    data['Title'] = titre

    return data