import data_base_controls

"""Just checking check one more thing"""
def main():
    while True:
        data_base_controls.create_table()
        # data_base_controls.insert_sample_data()
        data_base_controls.menu()


main()