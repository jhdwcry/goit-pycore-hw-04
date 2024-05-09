def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info = {
                    'id': cat_id,
                    'name': cat_name,
                    'age': int(cat_age)
                }
                cats_list.append(cat_info)
    
    except FileNotFoundError:
        print(f"File '{path}' is not found")
    
    return cats_list

cats_info = get_cats_info("cats/cats_info_file.txt")
print(cats_info)
