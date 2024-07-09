import json
import argparse
from hyperpyyaml import load_hyperpyyaml


def read_from_json(file_path):
	arg_dict = {}
	with open(file_path) as f:
		data = json.loads(f.read())
	for dicti in data:
		arg_dict = {**arg_dict, **dicti}
	return arg_dict


def read_from_yml(file_path):
    with open(file_path) as f:
        arg_dict = load_hyperpyyaml(f)
    return arg_dict


def read_from_txt(file_path):
	arg_dict = {}
	with open(file_path, 'r') as inf:
		for line in inf.readlines():
			line = line.split(' = ')
			arg_dict[line[0]] = line[-1].removesuffix('\n')
	return arg_dict


def arg_pars(config_path):
	parser = argparse.ArgumentParser()
	parser.add_argument(config_path, type=str, help='file containing all arguments')
	file_path = str(parser.parse_args().config_path)
	if file_path[len(file_path)-3:] == 'txt':
		arg_dict = read_from_txt(file_path)
	elif file_path[len(file_path)-3:] == 'yml':
		arg_dict = read_from_yml(file_path)
	elif file_path[len(file_path)-4:] == 'json':
		arg_dict = read_from_json(file_path) 
	else:
		arg_dict = {}
		print(f'\nНечитаемый формат конфигурации: {file_path[file_path.rfind(".")+1:]}\n')
	return arg_dict
