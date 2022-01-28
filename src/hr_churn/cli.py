import argparse
import logging
import os

from hr_churn.app import app


def cli_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-address',
                        default=os.environ.get('ADDRESS', '0.0.0.0'),
                        type=str,
                        help='App address')
    parser.add_argument('-port',
                        default=os.environ.get('PORT', 8080),
                        type=int,
                        help='App port')
    parser.add_argument('-debug',
                        action='store_true',
                        help='Debug mode for Flask')
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        format="%(asctime)s.%(msecs).3d %(levelname)s %(module)s - %(funcName)s: %(message)s",
        level=logging.INFO,
    )
    args = cli_argument_parser()
    app.run(host=args.address, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
