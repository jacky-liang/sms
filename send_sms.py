import argparse
from sms.sms import send_sms_via_email


def parse_creds(cred_file_path):
    with open(cred_file_path, "r") as f:
        lines = f.read().splitlines()
        return {
            'email': lines[0],
            'password': lines[1],
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--creds', '-c', type=str, help='credentials file', default='google_app_creds.txt')
    parser.add_argument('--number', '-n', type=str, help='phone number', required=True)
    parser.add_argument('--message', '-m', type=str, help='message', required=True)
    args = parser.parse_args()

    creds = parse_creds(args.creds)

    send_sms_via_email(args.number, args.message, creds['email'], creds['password'])
