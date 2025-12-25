import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Regular expression for email extraction
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, content)

        # Remove duplicates
        unique_emails = set(emails)

        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"✅ {len(unique_emails)} email(s) extracted successfully.")

    except FileNotFoundError:
        print("❌ Input file not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    extract_emails("input.txt", "extracted_emails.txt")


Contact us at support@example.com or admin@test.org
For queries email john.doe@gmail.com or admin@test.org
