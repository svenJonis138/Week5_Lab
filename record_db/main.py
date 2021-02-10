import data_base_controls


def main():
    """main function creates table if not exists and for the sample data uncomment the sample data function"""
    while True:
        data_base_controls.create_table()
        # data_base_controls.insert_sample_data()
        data_base_controls.menu()


main()
