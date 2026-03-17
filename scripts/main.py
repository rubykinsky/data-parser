import logging
import argparse
import json
import yaml
from data_parser.parsers import ParserFactory
from data_parser.config import Config

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('--config', type=str, help='Path to configuration file')
    parser.add_argument('--input', type=str, help='Path to input file')
    parser.add_argument('--output', type=str, help='Path to output file')
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

    # Load configuration
    config = Config()
    if args.config:
        with open(args.config, 'r') as file:
            if args.config.endswith('.json'):
                config.load_json(json.load(file))
            elif args.config.endswith('.yaml'):
                config.load_yaml(yaml.safe_load(file))

    # Create parser factory
    parser_factory = ParserFactory(config)

    # Parse input data
    parser_factory.parse(args.input, args.output)

if __name__ == '__main__':
    main()