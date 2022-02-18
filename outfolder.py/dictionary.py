if __name__ == "__main__":
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)

    # Adding elements one at a time
    Dict[0] = 'L'
    Dict[2] = 'G'
    Dict[3] = 1
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    # Adding set of values
    # to a single Key
    Dict['Value_set'] = 2, 3, 4
    print("\nDictionary after adding 3 elements: ")
    print(Dict)

    # Updating existing Key's Value
    Dict[2] = 'Chao'
    print("\nUpdated key value: ")
    print(Dict)

    # Adding Nested Key value to Dictionary
    Dict[5] = {'Nested': {'1': 'Cuộc sống', '2': 'Tươi đẹp'}}
    print("\nAdding a Nested Key: ")
    print(Dict)

    # accessing a element using get()
    # method
    print("Accessing a element using get:")
    print(Dict.get(3))

    # Deleting a Key value
    del Dict[3]
    print("\nDeleting a specific key: ")
    print(Dict)

    # Deleting a Key from
    # Nested Dictionary
    del Dict[5]['Nested']['1']
    print("\nDeleting a key from Nested Dictionary: ")
    print(Dict)
