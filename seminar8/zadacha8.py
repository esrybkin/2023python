import os
import json
import csv
import pickle

def get_directory_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

def get_directory_info(path):
    results = []
    for root, dirs, files in os.walk(path):
        dirname = os.path.basename(root)
        dirsize = get_directory_size(root)
        results.append({
            'name': dirname,
            'type': 'directory',
            'size': dirsize,
            'parent_directory': os.path.dirname(root),
        })
        for file in files:
            filepath = os.path.join(root, file)
            filesize = get_directory_size(filepath)
            results.append({
                'name': file,
                'type': 'file',
                'size': filesize,
                'parent_directory': os.path.dirname(filepath),
            })
    return results

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

def save_results_to_csv(results, output_file):
    fieldnames = ['name', 'type', 'size', 'parent_directory']
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)

def traverse_directory(path):
    results = get_directory_info(path)
    json_output_file = 'output.json'
    save_results_to_json(results, json_output_file)
    print(f'Saved results to {json_output_file}')
    csv_output_file = 'output.csv'
    save_results_to_csv(results, csv_output_file)
    print(f'Saved results to {csv_output_file}')
    pickle_output_file = 'output.pickle'
    save_results_to_pickle(results, pickle_output_file)
    print(f'Saved results to {pickle_output_file}')