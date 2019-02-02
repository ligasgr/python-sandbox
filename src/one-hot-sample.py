import pandas as pd

data_set = pd.read_csv('sample.csv')
unique_values_in_col2 = sorted(data_set.dropna()['col2'].unique().tolist())

print(type(unique_values_in_col2))
print(unique_values_in_col2)


def one_hot_encode(column_for_which_we_will_mark_value_here):
    def one_hot_for_column(actual_column_value_in_this_row):
        return column_for_which_we_will_mark_value_here == actual_column_value_in_this_row

    return one_hot_for_column


for new_column_suffix in unique_values_in_col2:
    data_set['col2_' + new_column_suffix] = data_set['col2'].apply(one_hot_encode(new_column_suffix))

print(data_set)
